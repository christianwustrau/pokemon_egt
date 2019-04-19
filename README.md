# pokemon_egt
Small Pokemon Game Implementation in Python for Evolutionary Game Theory

Pokemon EGT is an implementation of the Hawk-dove game based on Pokemon. Instead of hawk and dove there are 9 different Pokemon:

- Bulbasaur
- Charizard
- Squirtle
- Caterpie
- Pidgey
- Rattata
- Ekans
- Pikachu
- Omanyte

All Pokemon in the structured population start with an initial fitness value which can increase or decrease in fights. At each round active Pokemon fight against one of their active neighbors. After that both Pokemon who fought go passive. Pokemon populations will grow and reproduce based on updates rules.

The game can be started by simply running game.py but no update rules are implemented so the population won't change.
