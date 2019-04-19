import setup
import update

import random 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def game_function(data):
    global fig, ax_list
    wake_up_population()
    #fighting phase
    fight()
    
    #reproduction/update phase
    individual, neighbor = update.update_rule()
    if(individual != None and individual.poke_type != neighbor.poke_type):
      setup.update_subplot(individual.grid_id,neighbor.grid_id)
      
    #prints population each turn in the terminal with id, type and fitness of each pokemon
    #print_output(setup.poke_list)

def fight():
     counter = 0
     while(counter < int(np.sqrt(setup.columns*setup.rows))):
         r = random.randint(0,len(setup.poke_list)-1)
         if(setup.poke_list[r].status == setup.STATUS_ACTIVE):
             neighbors = update.get_neighbors(setup.poke_list[r])
             active_neighbors = []
             for neighbor in neighbors:
                 if(neighbor.status == setup.STATUS_ACTIVE):
                     active_neighbors.append(neighbor)
             if(len(active_neighbors) > 0):
                 enemy = active_neighbors[random.randint(0,len(active_neighbors)-1)]
                 apply_payoff_matrix(setup.poke_list[r],enemy)
                 enemy.status = setup.STATUS_ASLEEP
             setup.poke_list[r].status = setup.STATUS_ASLEEP
             counter+=1

def wake_up_population():
    for pokemon in setup.poke_list:
        pokemon.status = setup.STATUS_ACTIVE

def apply_payoff_matrix(pokemon,enemy):
    pokemon.fitness += setup.payoff_matrix[pokemon.matrix_id][enemy.matrix_id]
    enemy.fitness += setup.payoff_matrix[enemy.matrix_id][pokemon.matrix_id]

def print_output(poke_list):
    for i in range(setup.rows):
        row = []
        for j in range(setup.columns):
            current_pokemon = [setup.poke_list[i*setup.columns+j].grid_id,setup.poke_list[i*setup.columns+j].poke_type, setup.poke_list[i*setup.columns+j].fitness]
            row.append(current_pokemon)
        print(row)
    print('---------------------------------------------------------')

def start():
    ani = animation.FuncAnimation(setup.fig, game_function, interval=25,save_count=25)
    
    plt.show()

if __name__ == '__main__' :
    setup.init()
    start()
