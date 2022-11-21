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
    return "{} | lvl {} | hp {}/{}".format(pokemon["name"],
                                           pokemon["level"],
                                           pokemon["current_health"],
                                           pokemon["base_health"])


def choose_attack(player_pokemon):
    chosen = None
    while not chosen:
        print("Elige el ataque!")
        for index in range(len(player_pokemon["attacks"])):
            print("{} - {}".format(index, get_pokemon_attacks(player_pokemon["attacks"][index])))
        try:
            return player_pokemon["attacks"][int(input("Cual eliges? \n"))]
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
    print("--- NUEVO COMBATE ---\n")

    player_pokemon = choose_pokemon(player_profile)
    print("Contrincantes: {} VS {}".format(get_pokemon_info(player_pokemon),
                                           get_pokemon_info(enemy_pokemon)))

    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0:
        if player_pokemon["current_health"] <= 0:
            break
        player_attack(player_pokemon, enemy_pokemon)

        enemy_attack(enemy_pokemon, player_pokemon)
        if enemy_pokemon["current_health"] <= 0:
            print("\n{} es derrotado!!".format(enemy_pokemon["name"]))
            item_lottery(player_profile)
    input("Preciona ENTER para continuar...")

    print("--- FIN DEL COMBATE ---\n")

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

        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile, enemy_pokemon)


if __name__ == "__main__":
    main()
