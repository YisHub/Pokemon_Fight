import random
from pprint import pprint
from Pokemon_get import get_all_pokemons


def get_player_profile(pokemon_list):
    return {
        "player_name": "Seba",  # input("Cual es tu nombre?\n"),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0,
    }


def any_player_pokemon_lives(player_profile):
    for index in range(len(player_profile["pokemon_inventory"])):
        if player_profile["pokemon_inventory"][index]["current_health"] < 0:
            player_profile["pokemon_inventory"][index]["current_health"] = 0

    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def choose_pokemon(player_profile):
    chosen = None
    while not chosen:
        print("Elige con que pokemon lucharás!")
        for index in range(len(player_profile["pokemon_inventory"])):
            print("{} - {}".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index])))
        try:
            return player_profile["pokemon_inventory"][int(input("Cual eliges? \n"))]
        except (ValueError, IndexError):
            print("Opcion invalida")


def get_pokemon_info(pokemon):
    return "{} | lvl {} | {} xp |hp {}/{}".format(pokemon["name"],
                                           pokemon["level"],
                                           pokemon["current_exp"],
                                           pokemon["current_health"],
                                           pokemon["base_health"])


def choose_attack(player_pokemon):
    chosen = None
    while not chosen:
        print("Elige el ataque!")
        for index in range(len(player_pokemon["attacks"])):
            #print(int(int(player_pokemon["attacks"][index]["min_level"])/10), int(player_pokemon["level"]))
            if player_pokemon["attacks"][index]["min_level"]  != "" and int(int(player_pokemon["attacks"][index]["min_level"])/10) <= int(player_pokemon["level"])  :
                
                if int(player_pokemon["attacks"][index]["damage"]) == 0:
                    
                    player_pokemon["attacks"][index]["damage"] = 25

                print("{} - {}".format(index, get_pokemon_attacks(player_pokemon["attacks"][index])))
        try:
            return player_pokemon["attacks"][int(input("\nCual eliges? \n"))]
        except (ValueError, IndexError):
            print("Opcion invalida")


def get_pokemon_attacks(attack):
    return "{} | daño {} | tipo {}".format(attack["name"],
                                           attack["damage"],
                                           attack["type"])


def player_attack(player_pokemon, enemy_pokemon):

    attack = choose_attack(player_pokemon)

    message_combat(player_pokemon, enemy_pokemon, attack)


def enemy_attack(enemy_pokemon, player_pokemon):

    attack = enemy_pokemon["attacks"][random.randint(0, len(enemy_pokemon["attacks"]) - 1)]

    message_combat(enemy_pokemon, player_pokemon, attack)


def message_combat(attacker, victim, attack):
    print("{} ataca con {}! ".format(attacker["name"], attack["name"]))

    print("-{} para {}!".format(attack["damage"], victim["name"]))

    victim["current_health"] -= attack["damage"]


def fight(player_profile, enemy_pokemon):
    print("\n--- NUEVO COMBATE ---\n")

    attack_history = []

    player_pokemon = choose_pokemon(player_profile)

    print("Contrincantes: {} VS {}".format(get_pokemon_info(player_pokemon),
                                           get_pokemon_info(enemy_pokemon)))

    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0:
        
        action = None

        while action not in ["A", "P", "V", "C", "I"]:

            action = input("¿Que deseas hacer?: [A]tacar, [C]ambiar, [I]tems, [P]okeball, Poción de [V]ida\n")

        if action == "A":
            
            if player_pokemon["current_health"] > 0: 

                player_attack(player_pokemon, enemy_pokemon)

            attack_history.append(player_pokemon)



        elif action == "V":
            
            
            #Si el usuario tiene curas en el inventario, se aplica 50, hasta llegar a 100ps

            #Si el usuario no tiene no cura

            cure_pokemon(player_profile, player_pokemon)

        elif action == "P":

            #pruebas(player_profile, enemy_pokemon)
            #Si el usuario tiene pokeballs en el inventario, capturara, con cierta probabilidad

            #relativa a la salud restante del pokemon, cuando se captura, pasa al inventario con la misma salud y toh.

            capture_with_pokeball(player_profile, enemy_pokemon)



        elif action == "C":

            player_pokemon = choose_pokemon(player_profile)

        elif action == "I":
            print("Tienes {} pokeballs y {} pociónes de vida".format(player_profile["pokeballs"],player_profile["health_potion"]))

        if enemy_pokemon["current_health"] > 0:
            
                enemy_attack(enemy_pokemon, player_pokemon)

        if player_pokemon["current_health"] == 0 and any_player_pokemon_lives(player_profile):

            player_pokemon = choose_pokemon(player_profile)

        


    if enemy_pokemon["current_health"] <= 0:

        print("\n{} es derrotado!!".format(enemy_pokemon["name"]))

        item_lottery(player_profile)    

        assign_exp(attack_history)
       




#        if enemy_pokemon["current_health"] <= 0:
#            print("\n{} es derrotado!!".format(enemy_pokemon["name"]))
#            item_lottery(player_profile)
    
    print("\n--- FIN DEL COMBATE ---\n")

    input("Preciona ENTER para continuar...")

    return player_profile


def item_lottery(player_profile):
    choice = random.choice(["pokeballs", "health_potion", "health_potion"])
        
    player_profile[choice] +=  1

    if choice == "pokeballs":
        item = "pokeball"
    else:
        item = "pocion de vida"


    print("\nHas obtenido una {}!! ".format(item))
    return player_profile


def assign_exp(attack_history):

    

    for pokemon in attack_history:

        points = random.randint(1, 5)

     

        pokemon["current_exp"] += points

    if pokemon["current_exp"] > 20:

        pokemon["current_exp"] -= 20

        pokemon["level"] += 1

        pokemon["current_health"] = pokemon["base_health"]

        print("Tu pokemon ha subido al nivel {}".format(get_pokemon_info(pokemon)))


def cure_pokemon(player_profile, player_pokemon):

    if player_profile["health_potion"] > 0:
        player_pokemon["current_health"] += 50
        if player_pokemon["current_health"] > player_pokemon["base_health"]:
            player_pokemon["current_health"] == player_pokemon["base_health"]
        player_profile["health_potion"] -= 1
        print("\nHas usado una pocion de vida! +50 para {}".format(player_pokemon["name"]))

        return player_pokemon, player_profile
    else:
        print("No Tienes Poción")


def capture_with_pokeball(player_profile, enemy_pokemon):
    
    if player_profile["pokeballs"] > 0:
        random_num = random.randint(1, 64)
    
        if enemy_pokemon["current_health"] <= 35 and random_num == 1 \
            or enemy_pokemon["current_health"] <= 30 and random_num <= 2 \
            or enemy_pokemon["current_health"] <= 25 and random_num <= 4 \
            or enemy_pokemon["current_health"] <= 20 and random_num <= 8 \
            or enemy_pokemon["current_health"] <= 15 and random_num <= 16 \
            or enemy_pokemon["current_health"] <= 10 and random_num <= 32 \
            or enemy_pokemon["current_health"] <= 5 and random_num <= 64 :
            print("Lo has capturado!")
            player_profile["pokemon_inventory"] += enemy_pokemon.copy(),
            enemy_pokemon["current_health"] = 0
            return player_profile
           
        else:
            print("Fallaste")
    
            pass

        player_profile["pokeballs"] -= 1
    else:
        print("No Tienes pokeballs")


def pruebas(player_profile, enemy_pokemon):
    #    pprint(player_profile)
    # Buscamos los datos del pokemon
    # pprint(player_profile["pokemon_inventory"])
    # obtenemos uno solo
    """  for h in range(len(player_profile["pokemon_inventory"])):
        print("\nLa vida actual del pokemon {} es {}".format(player_profile["pokemon_inventory"][h]["name"], player_profile["pokemon_inventory"][h]["current_health"]))



        ataques = []
        for i in range(len(player_profile["pokemon_inventory"][h]["attacks"])):

            ataques.append(player_profile["pokemon_inventory"][h]["attacks"][i]["name"])
            
            


        print("y sus ataques son {}".format(",".join(ataques)))
        print("\n")
    """
    
def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)

    # enemy_pokemon = random.choice(pokemon_list)

    # pruebas(player_profile, enemy_pokemon)
    
    while any_player_pokemon_lives(player_profile):

        while True:
            enemy_pokemon = random.choice(pokemon_list)
            if enemy_pokemon["current_health"] > 0:
                break
        fight(player_profile, enemy_pokemon)


if __name__ == "__main__":
    main()
