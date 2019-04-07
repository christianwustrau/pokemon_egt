import random 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation

Bulbasaur = "Bulbasaur"
Charmander = "Charmander"
Squirtle = "Squirtle"
Caterpie = "Caterpie"
Pidgey = "Pidgey"
Rattata = "Rattata"
Ekans = 'Ekans'
Pikachu = "Pikachu"
Omanyte = "Omanyte"
Voltorb = "Voltorb"

#number of colums and rows needs to be equal to remove white spaces
columns = 5
rows = 5

subset = [Bulbasaur,Charmander,Squirtle,Caterpie,Pidgey,Rattata,Ekans,Pikachu,Omanyte]

#colab notebook erstellen


STATUS_ACTIVE = "active"
STATUS_ASLEEP = "passive"

STARTING_FITNESS = 10
WINNER_FITNESS = 3
LOSER_FITNESS = 3

class Pokemon:
    id = 0
    poke_type = None
    status = STATUS_ACTIVE
    fitness = STARTING_FITNESS
    image = None

def init():
    global fig, ax_list, poke_list
    fig = plt.figure()#figsize=(5, 5))

    imgs = []
    poke_list = []
    fitness_list = []
    
    for j in range(10):
        imgs.append(mpimg.imread('Sprites/Pokémon-Icon_'+str(j)+'.png'))
    
    for i in range(columns*rows):
        fig.add_subplot(rows,columns,i+1)
        p = Pokemon()
        p.id = i
        p.poke_type = Bulbasaur
        p.image = imgs[0]
        plt.imshow(p.image)
        poke_list.append(p)
        #plt.axis('off')
    
    fig.subplots_adjust(wspace=0, hspace=0)

    ax_list = fig.get_axes()

    random_update_subplot(imgs)

def random_update_subplot(imgs):
  global fig, ax_list
  for k in range(columns*rows):
      ax_list[k].clear()
      r = random.randint(0,len(subset) - 1)
      poke_list[k].poke_type = subset[r]
      if(poke_list[k].poke_type == Bulbasaur):
          poke_list[k].image = imgs[0]
      elif(poke_list[k].poke_type == Charmander):
          poke_list[k].image = imgs[1]
      elif(poke_list[k].poke_type == Squirtle):
          poke_list[k].image = imgs[2]
      elif(poke_list[k].poke_type == Caterpie):
          poke_list[k].image = imgs[3]
      elif(poke_list[k].poke_type == Pidgey):
          poke_list[k].image = imgs[4]
      elif(poke_list[k].poke_type == Rattata):
          poke_list[k].image = imgs[5]
      elif(poke_list[k].poke_type == Ekans):
          poke_list[k].image = imgs[6]
      elif(poke_list[k].poke_type == Pikachu):
          poke_list[k].image = imgs[7]
      elif(poke_list[k].poke_type == Omanyte):
          poke_list[k].image = imgs[8]
      elif(poke_list[k].poke_type == Voltorb):
          poke_list[k].image = imgs[9]
      ax_list[k].imshow(poke_list[k].image)
      ax_list[k].axis('off')

def update_subplot(substitute, former):
#the pokemon with index former is replaced by the pokemon with the index substitute
    global fig, ax_list
    ax_list[former].clear()
    if(poke_list[substitute].poke_type == Bulbasaur):
        poke_list[former].poke_type = Bulbasaur
        poke_list[former].image = poke_list[substitute].image
    elif(poke_list[substitute].poke_type == Charmander):
        poke_list[former].poke_type = Charmander
        poke_list[former].image = poke_list[substitute].image
    elif(poke_list[substitute].poke_type == Squirtle):
        poke_list[former].poke_type = Squirtle
        poke_list[former].image = poke_list[substitute].image
    elif(poke_list[substitute].poke_type == Caterpie):
        poke_list[former].poke_type = Caterpie
        poke_list[former].image = poke_list[substitute].image
    elif(poke_list[substitute].poke_type == Pidgey):
        poke_list[former].poke_type = Pidgey
        poke_list[former].image = poke_list[substitute].image
    elif(poke_list[substitute].poke_type == Rattata):
        poke_list[former].poke_type == Rattata
        poke_list[former].image = poke_list[substitute].image
    elif(poke_list[substitute].poke_type == Ekans):
        poke_list[former].poke_type = Ekans
        poke_list[former].image = poke_list[substitute].image
    elif(poke_list[substitute].poke_type == Pikachu):
        poke_list[former].poke_type = Pikachu
        poke_list[former].image = poke_list[substitute].image
    elif(poke_list[substitute].poke_type == Omanyte):
        poke_list[former].poke_type = Omanyte
        poke_list[former].image = poke_list[substitute].image
    elif(poke_list[substitute].poke_type == Voltorb):
        poke_list[former].poke_type = Voltorb
        poke_list[former].image = poke_list[substitute].image
    ax_list[former].imshow(poke_list[former].image)
    ax_list[former].axis('off')

def game_function(data):
    global fig, ax_list
    #fighting phase
    fight()
    #reproduction/update phase
    individual, neighbor = update_rule_birth_death()
    update_subplot(individual.id,neighbor.id)
    #prints population each turn in the terminal with id, type and fitness of each pokemon
    #print_output(poke_list)

def update_rule_birth_death():
    #select individual and neighbor and return them
    individual = select_individual(poke_list)
    neighbors = get_neighbors(individual)
    neighbor = select_neighbor(neighbors)
    return individual, neighbor

def select_individual(poke_list):
    return poke_list[random.randint(0,columns*rows-1)]

def select_neighbor(neighbors):
    return neighbors[random.randint(0,len(neighbors)-1)]

def get_neighbors(individual):
    neighbors = []
    column = int(individual.id % columns)
    row = int(individual.id / rows)
    if (row * rows + column - 1) >= 0 and (row * rows + column - 1) < columns*rows-1 and column != 0:
        neighbors.append(poke_list[row * rows + column - 1])
    if (row * rows + column + 1) >= 0 and (row * rows + column + 1) < columns*rows-1 and column != (columns - 1):
        neighbors.append(poke_list[row * rows + column + 1])
    if ((row - 1) * rows + column) >= 0 and ((row - 1) * rows + column) < columns*rows-1:
        neighbors.append(poke_list[(row - 1) * rows + column])
    if ((row + 1) * rows + column) >= 0 and ((row + 1) * rows + column) < columns*rows-1:
        neighbors.append(poke_list[(row + 1) * rows + column])
    return neighbors

def fight():
    for pokemon in poke_list:
        if(pokemon.status == STATUS_ACTIVE):
            neighbors = get_neighbors(pokemon)
            active_neighbors = []
            for neighbor in neighbors:
                if(neighbor.status == STATUS_ACTIVE):
                    active_neighbors.append(neighbor)
            if(len(active_neighbors) > 0):
                enemy = select_neighbor(active_neighbors)
                apply_payoff_matrix(pokemon,enemy)
                enemy.status = STATUS_ASLEEP
            pokemon.status = STATUS_ASLEEP

def apply_payoff_matrix(pokemon,enemy):
    if(pokemon.poke_type == Bulbasaur and (enemy.poke_type == Bulbasaur or
                                           enemy.poke_type == Charmander or
                                           enemy.poke_type == Caterpie or
                                           enemy.poke_type == Pidgey or
                                           enemy.poke_type == Ekans)):
        pokemon.fitness -= LOSER_FITNESS
        enemy.fitness += WINNER_FITNESS
    elif(pokemon.poke_type == Bulbasaur and (enemy.poke_type == Squirtle or
                                             enemy.poke_type == Omanyte)):
        pokemon.fitness += WINNER_FITNESS
        enemy.fitness -= LOSER_FITNESS
    elif(pokemon.poke_type == Charmander and (enemy.poke_type == Charmander or
                                           enemy.poke_type == Squirtle or
                                           enemy.poke_type == Omanyte)):
        pokemon.fitness -= LOSER_FITNESS
        enemy.fitness += WINNER_FITNESS
    elif(pokemon.poke_type == Charmander and (enemy.poke_type == Bulbasaur or
                                           enemy.poke_type == Charmander)):
        pokemon.fitness += WINNER_FITNESS
        enemy.fitness -= LOSER_FITNESS
    elif(pokemon.poke_type == Squirtle and (enemy.poke_type == Bulbasaur or
                                           enemy.poke_type == Squirtle)):
        pokemon.fitness -= LOSER_FITNESS
        enemy.fitness += WINNER_FITNESS
    elif(pokemon.poke_type == Squirtle and (enemy.poke_type == Charmander or
                                           enemy.poke_type == Omanyte)):
        pokemon.fitness += WINNER_FITNESS
        enemy.fitness -= LOSER_FITNESS
    elif(pokemon.poke_type == Caterpie and (pokemon.poke_type == Charmander or
                                           pokemon.poke_type == Pidgey)):
        pokemon.fitness -= LOSER_FITNESS
        enemy.fitness += WINNER_FITNESS
    elif(pokemon.poke_type == Caterpie and (pokemon.poke_type == Bulbasaur or
                                           pokemon.poke_type == Ekans)):
        pokemon.fitness += WINNER_FITNESS
        enemy.fitness -= LOSER_FITNESS
    elif(pokemon.poke_type == Pidgey and (pokemon.poke_type == Bulbasaur or
                                           pokemon.poke_type == Caterpie)):
        pokemon.fitness -= LOSER_FITNESS
        enemy.fitness += WINNER_FITNESS
    elif(pokemon.poke_type == Pidgey and (pokemon.poke_type == Pikachu or
                                           pokemon.poke_type == Omanyte)):
        pokemon.fitness += WINNER_FITNESS
        enemy.fitness -= LOSER_FITNESS
    elif(pokemon.poke_type == Rattata and (pokemon.poke_type == Omanyte)):
        pokemon.fitness -= LOSER_FITNESS
        enemy.fitness += WINNER_FITNESS
    elif(pokemon.poke_type == Ekans and (pokemon.poke_type == Bulbasaur or
                                           pokemon.poke_type == Caterpie)):
        pokemon.fitness -= LOSER_FITNESS
        enemy.fitness += WINNER_FITNESS
    elif(pokemon.poke_type == Ekans and (pokemon.poke_type == Ekans or
                                           pokemon.poke_type == Omanyte)):
        pokemon.fitness += WINNER_FITNESS
        enemy.fitness -= LOSER_FITNESS
    elif(pokemon.poke_type == Pikachu and (pokemon.poke_type == Bulbasaur or
                                           pokemon.poke_type == Pikachu)):
        pokemon.fitness -= LOSER_FITNESS
        enemy.fitness += WINNER_FITNESS
    elif(pokemon.poke_type == Pikachu and (pokemon.poke_type == Squirtle or
                                           pokemon.poke_type == Pidgey)):
        pokemon.fitness += WINNER_FITNESS
        enemy.fitness -= LOSER_FITNESS
    elif(pokemon.poke_type == Omanyte and (pokemon.poke_type == Charmander or
                                           pokemon.poke_type == Caterpie or
                                           pokemon.poke_type == Pidgey)):
        pokemon.fitness += WINNER_FITNESS
        enemy.fitness -= LOSER_FITNESS

def print_output(poke_list):
    for i in range(rows):
        row = []
        for j in range(columns):
            current_pokemon = [poke_list[i*rows+j].id,poke_list[i*rows+j].poke_type, poke_list[i*rows+j].fitness]
            row.append(current_pokemon)
        print(row)
    print('---------------------------------------------------------')

def start():
    ani = animation.FuncAnimation(fig, game_function, interval=25,save_count=25)
    
    #update_rule_birth_death(1)
    #update_rule_birth_death(1)
    #update_rule_birth_death(1)
    
    plt.show()


if __name__ == '__main__' :
    init()
    start()
