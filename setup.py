import random 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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

#number of colums and rows
rows = 7
columns = 5

#subset of pokemon occuring in the population, voltorb not implemented
subset = [Bulbasaur,Charmander,Squirtle,Caterpie,Pidgey,Rattata,Ekans,Pikachu,Omanyte]

STATUS_ACTIVE = "active"
STATUS_ASLEEP = "passive"

STARTING_FITNESS = 10
BREEDING_FITNESS = 12
NEWBORN_FITNESS = 6

imgs = []
ax_list = []
poke_list = []
payoff_matrix = []

fig = plt.figure()#figsize=(5, 5))

class Pokemon:
    grid_id = 0
    matrix_id = 0
    poke_type = None
    status = STATUS_ACTIVE
    fitness = STARTING_FITNESS
    image = None

def init():
    global fig, ax_list, poke_list, payoff_matrix

    payoff_matrix = np.genfromtxt('Payoff_Matrix.csv',delimiter=',')
    
    for j in range(10):
        imgs.append(mpimg.imread('Sprites/Pokémon-Icon_'+str(j)+'.png'))
    
    for i in range(columns*rows):
        fig.add_subplot(rows,columns,i+1)
        p = Pokemon()
        p.grid_id = i
        p.fitness = STARTING_FITNESS
        r = random.randint(0,len(subset) - 1)
        p.poke_type = subset[r]
        if(p.poke_type == Bulbasaur):
            p.image = imgs[0]
            p.matrix_id = 0
        elif(p.poke_type == Charmander):
            p.image = imgs[1]
            p.matrix_id = 1
        elif(p.poke_type == Squirtle):
            p.image = imgs[2]
            p.matrix_id = 2
        elif(p.poke_type == Caterpie):
            p.image = imgs[3]
            p.matrix_id = 3
        elif(p.poke_type == Pidgey):
            p.image = imgs[4]
            p.matrix_id = 4
        elif(p.poke_type == Rattata):
            p.image = imgs[5]
            p.matrix_id = 5
        elif(p.poke_type == Ekans):
            p.image = imgs[6]
            p.matrix_id = 6
        elif(p.poke_type == Pikachu):
            p.image = imgs[7]
            p.matrix_id = 7
        elif(p.poke_type == Omanyte):
            p.image = imgs[8]
            p.matrix_id = 8
        elif(p.poke_type == Voltorb):
            p.image = imgs[9]
            p.matrix_id = 9
        plt.imshow(p.image)
        poke_list.append(p)
        plt.axis('off')
    
    fig.subplots_adjust(wspace=0, hspace=0)

    ax_list = fig.get_axes()

def update_subplot(substitute, former):
#the pokemon with index substitute reproduces and his offspring replaces the pokemon with index former
    ax_list[former].clear()
    poke_list[substitute].fitness -=6
    poke_list[former].fitness = NEWBORN_FITNESS
    poke_list[former].matrix_id = poke_list[substitute].matrix_id
    poke_list[former].poke_type = poke_list[substitute].poke_type
    poke_list[former].image = poke_list[substitute].image
    ax_list[former].imshow(poke_list[former].image)
    ax_list[former].axis('off')
