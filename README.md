# Pokemon Fight App
Este es un proyecto de una aplicación de pelea de Pokémon desarrollado como parte de un curso de Mastermind por Nate Gentile. La aplicación consta de dos archivos principales: Pokemon_fight.py y Pokemon_get.py.

## Descripción
La aplicación simula peleas entre diferentes Pokémon, permitiendo al usuario elegir su Pokémon y participar en combates por turnos contra enemigos generados aleatoriamente.

## Características
- **Elección de Pokémon**: Los usuarios pueden elegir entre diferentes Pokémon disponibles para combatir.
- **Ataques y Estrategia**: Cada Pokémon tiene una serie de ataques con diferentes daños y tipos que el usuario puede seleccionar durante la pelea.
- **Objetos y Capturas**: Los usuarios pueden utilizar pokeballs y pociones de vida para capturar Pokémon enemigos o curar a sus propios Pokémon en medio de la pelea.
## Instrucciones de Uso
1. Clonar el Repositorio

``` bash
git clone https://github.com/tu-usuario/tu-repositorio.git
```
2. Instala dependencias
 ``` bash
pip install requests_html
```

3. Ejecutar la Aplicación

``` bash
python Pokemon_fight.py
```
## Requisitos
- Python 3.x
- Bibliotecas requeridas: requests_html, pickle
## Uso
La aplicación permite a los usuarios participar en peleas por turnos entre Pokémon. A continuación se muestra un ejemplo de la secuencia de una pelea:

1. **Elegir Pokémon**: El usuario elige un Pokémon para la batalla entre los disponibles. Se muestran los detalles del Pokémon, como nivel, experiencia y puntos de salud.

2. **Comenzar el Combate**: Se inicia la pelea mostrando la información sobre los Pokémon enemigos y las opciones disponibles para el usuario, como [A]tacar, [C]ambiar de Pokémon, [I]tems (pociones, pokeballs, etc.).

3. **Ataques**: Durante el combate, el usuario elige un ataque entre las opciones disponibles para su Pokémon. Cada ataque tiene su daño y tipo asociado. Los enemigos también realizan ataques que infligen daño al Pokémon del usuario.

4. **Captura y Derrota**: En el transcurso de la pelea, el usuario tiene la oportunidad de capturar Pokémon enemigos utilizando pokeballs (si las tiene) o derrotar a los Pokémon enemigos para avanzar en el juego.

5. **Uso de Objetos**: Los usuarios pueden utilizar objetos como pociones de vida para curar a sus Pokémon durante la batalla y prolongar su resistencia en el combate. También tienen la opción de utilizar pokeballs para intentar capturar Pokémon enemigos.

6. **Desarrollo de la Batalla**: El combate continúa hasta que uno de los Pokémon es derrotado o el usuario decide cambiar su Pokémon para una estrategia diferente.

7. **Fin del Combate**: Una vez que la pelea concluye, se muestra un resumen del resultado, incluyendo la experiencia obtenida y los objetos ganados (pokeballs, pociones, etc.).

# Obtención de Datos de Pokémon
La información de los Pokémon se adquiere a través de la web utilizando web scraping y la biblioteca **requests_html**. El archivo **Pokemon_get.py** contiene funciones para obtener los detalles de los Pokémon, incluyendo sus nombres, tipos y ataques.

## Descripción del Proceso
El proceso de obtención de datos implica la extracción de información de la página web "https://pokexperto.net/" mediante solicitudes HTTP. Se utiliza un enlace específico para cada Pokémon y se extraen los detalles relevantes de la página web para construir una base de datos de Pokémon.

## Funciones Principales
- **get_pokemon(index)**: Esta función toma un índice que representa el número de Pokemón y realiza una solicitud HTTP para obtener los detalles específicos del Pokémon, como su nombre, tipo y ataques disponibles.

- **get_all_pokemons()**: Esta función verifica si se encuentra el archivo **pokefile.pkl**, que contiene los datos; de lo contrario, recorre una serie de índices de Pokémon (1 a 150) y utiliza la función **get_pokemon(index)** para obtener los detalles de cada Pokémon en una lista.

## Almacenamiento de Datos
Los datos obtenidos se almacenan localmente en un archivo **pokefile.pkl** utilizando la biblioteca **pickle** para evitar solicitudes repetitivas a la página web y mejorar la eficiencia en futuras ejecuciones de la aplicación.

Estos datos almacenados se utilizan en la aplicación principal **Pokemon_fight.py** para proporcionar a los usuarios la posibilidad de elegir entre diferentes Pokémon y llevar a cabo las peleas.

## Contribuciones
Siéntete libre de contribuir al proyecto. Puedes hacerlo a través de:

- Corrección de errores.
- Mejoras en la interfaz de usuario.
- Adición de nuevas características.

Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme: jesus14sf@gmail.com
