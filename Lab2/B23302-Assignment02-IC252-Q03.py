####################### De Montmort’s Matching Problem #######################################

################## by performing  trials ########################
#importing libraries
import random
import matplotlib.pyplot as plt

def play_game(n):           #shufffles the deck and matches ith card with i
    deck = list(range(1, n+1))
    random.shuffle(deck)
    for i, card in enumerate(deck, start=1):
        if i == card:
            return True
    return False
x_values=[]           #x-values list for graph
y_values=[]           #y-values list for graph
max=0                 #max probability
out=0                 #number of cards at max probability
n = 100               # Max Number of cards
num_trials = 10000    # Number of trials

for i in range(2,n+1):   #number of cards from 2 to n
    x_values.append(i)
    wins = 0
    for j in range(num_trials):
        if play_game(i):
            wins += 1
    probab=wins/num_trials #probability of match
    if(max<probab):
        max=probab
        out=i
    y_values.append(probab)

print("max value =",max,"and number of cards =",out)  #print the point of maximum probability
#plot-graph
plt.figure(figsize=(8,5))  #graph-fig-size
plt.plot(x_values,y_values)
plt.xlabel("Number of cards")
plt.ylabel("Probability of Winning")
plt.title("Probability of Win(Label of ith card mathches with i) as the number of cards change")
plt.plot(out,max,marker='o')    #mark the point of maximum probability
plt.annotate(f"Maximum probability to Win:{out,max}", (out, max),textcoords='offset points',xytext=(5, 5), bbox=dict(boxstyle='round,pad=0.1', fc='yellow', alpha=0.4),arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-0.5', color='black'))
plt.grid(True)
plt.tight_layout()

#save/show
plt.savefig("Q03_derangement_theorem_graph.png")
plt.show()


################################ values tend to 1-(1/e) ###### as number of cards increase  

#################################################################################################

#################using derangement formula##############
#importing libraries
import numpy as np
import matplotlib.pyplot as plt

def facto(k):    #factorial calculator
    if k==0:
        fact=1
        return fact
    else:
        fact=1
        for i in range(1,k+1):
            fact=fact*i
        return fact

n = 100                         #number of cards
cards = list(range(1, n + 1))
x_values=cards[1:]                         #x-values list for graph
np.random.shuffle(cards)        #shuffle the cards

y_values=[]                                #y-values list for graph
def derange_probab(n): #calculation of probability using derangement formula
    global max                 #max probability
    global out                 #number of cards at max probability
    max=0
    for i in range(2,n+1):
        k=1
        for j in range(0,i+1):
            k+=(pow(-1,j-1)/facto(j))
        if(k>max):
            max=k
            out=i
        y_values.append(k)

derange_probab(n)

print("max value =",max,"and number of cards =",out)  #print the point of maximum probability
#plot-graph
plt.figure(figsize=(8,5))  #graph-fig-size
plt.plot(x_values,y_values)
plt.xlabel("Number of cards")
plt.ylabel("Probability of Winning")
plt.title("Probability of Win(Label of ith card mathches with i) as the number of cards change")
plt.plot(out,max,marker='o')    #mark the point of maximum probability
plt.annotate(f"Maximum probability to Win:{out,max}", (out, max),textcoords='offset points',xytext=(5, 5), bbox=dict(boxstyle='round,pad=0.1', fc='yellow', alpha=0.4),arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-0.5', color='black'))
plt.grid(True)
plt.tight_layout()

#save/show
plt.savefig("Q03_derangement_theorem_graph.png")
plt.show()
