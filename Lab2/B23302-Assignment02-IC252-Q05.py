################################## Monty Hall Problem ###########################

#import libraries
import numpy as np
import matplotlib.pyplot as plt

n = 10000  #number of trials
win_switch = 0     #wins if switched
win_stay = 0       #win if stayed
y_value_switch=[]  #y-values list for graph if switched
y_value_stay=[]    #y-values list for graph if stayed
x_values=[]        #x-values list for graph

#print statement 
print("Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, 'Do you want to pick door No. 2?' Is it to your advantage to switch your choice?")

for i in range(1,n+1):   #trials
    x_values.append(i)  
    doors = ['goat', 'goat', 'goat']  #defining doors
    prize_door = np.random.randint(0, 3) #randomly assign prize door
    doors[prize_door] = 'car'

    # Player's initial choice
    player_choice = np.random.randint(0, 3)
    print("Player selected door:", player_choice, end=" ")

    # Host opens a door with a goat
    doors_host = [i for i in range(3) if i != player_choice and doors[i] == 'goat']
    host_door = np.random.choice(doors_host)
    print("Host opened door:", host_door, end=" ")

    # Switch to the remaining unopened door
    switch_choice = [i for i in range(3) if i != player_choice and i != host_door][0]

    if doors[switch_choice] == 'car':            #win if switch
        win_switch += 1
        y_value_switch.append(win_switch/i)     #append probability of win if switch till no of trials done
        y_value_stay.append(win_stay/i)         #append probability of win if stay till no of trials done
        print("Win if switch")
    else:                                        #win if stay
        win_stay += 1
        y_value_stay.append(win_stay/i)         #append probability of win if stay till no of trials done
        y_value_switch.append(win_switch/i)     #append probability of win if switch till no of trials done
        print("Win if stay")

p_win_switch = win_switch/n
p_win_stay = win_stay/n
print("Probability of winning by staying with initial choice:", p_win_stay)
print("Probability of winning by switching doors:", p_win_switch)

#plot-graph
plt.figure(figsize=(8,5))  #graph-size
plt.plot(x_values,y_value_switch,label='Switch')
plt.plot(x_values,y_value_stay,label='Stay')
plt.legend() #print index on plot
plt.xlabel("Number of Trials")
plt.ylabel("Probability")
plt.title("Monty Hall Problem")
plt.grid(True)
plt.tight_layout()

#save/show plot
plt.savefig("Q05_graph.png")
plt.show()


