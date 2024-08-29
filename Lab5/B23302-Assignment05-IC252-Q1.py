# 1. For the given file “timeMachine.txt”, do the following:
# (a) Find the frequency (the number of occurrences of all the words) and plot a histogram of the probability distribution of it.
##################################################################################################################################

# libraries 
import matplotlib.pyplot as plt
import re
from collections import Counter

with open('fileA-TimeMachine.txt', 'r', encoding='utf-8') as file: #read file
    given_text = file.read()

given_text = given_text.lower()  #lowercase

words = re.findall(r'\b[A-Za-z]+\b', given_text) 

wordcnt = Counter(words)  #dict{word:number}

for wrd, cnt in wordcnt.items(): #(word:frequency)
   print(f'{wrd}: {cnt}')

total = sum(wordcnt.values())#total words

# probabilty
probab = {wrd: cnt / total for wrd, cnt in wordcnt.items()}

#histogram
plt.figure(figsize=(10, 6))
plt.hist(probab.values(), bins=20, color='orange', edgecolor='black')
plt.title('Probability Distribution of Word Count')
plt.xlabel('Probability')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

probab_words = list(probab.values()) #dict to lists
wrds = list(probab.keys())

plt.figure(figsize=(10, 6))
plt.bar(wrds, probab_words, color='orange')
plt.title('Probability Distribution of Word Count')
plt.xlabel('Words')
plt.ylabel('Probability')
plt.ylim(0.0,0.035)
plt.xticks(rotation=90, ha='right',ticks=wrds[::75])  
plt.grid(linestyle='--', alpha=0.5)   
plt.tight_layout() 
plt.show()

# (b) Find the probability of occurrence of all ordered pairs of letters. Print the probabilities of the top 10 ordered pairs
# (Ignore punctuation and white spaces).
##############################################################################################################################

words_b = re.sub(r'[^a-zA-Z]', '', given_text) #string 

order_pair_cnt = Counter(zip(words_b, words_b[1:]))#ordered pairs

total_pairs = sum(order_pair_cnt.values())#total pairs

# probability
probab_opair = {pair: cnt / total_pairs for pair, cnt in order_pair_cnt.items()}

top_probab_pair = sorted(probab_opair.items(), key=lambda x: x[1], reverse=True)[:10]     #sort

print("Top 10 ordered pairs with probabilities:")
for pair, prb in top_probab_pair:
    print(f"{pair}: {prb:.4f}")

# (c) Repeat b part while ignoring the punctuation but considering the white spaces
####################################################################################################################

words_space = re.sub(r'[^\w\s]', '', given_text)

order_pair_c = [words_space[i:i+2] for i in range(len(words_space)-1)]
pair_cnt = Counter(order_pair_c)

total_pairs = sum(pair_cnt.values())

# probabilities
probab_pair_c = {pair: cnt / total_pairs for pair, cnt in pair_cnt.items()}

top_pairs_c = sorted(probab_pair_c.items(), key=lambda x: x[1], reverse=True)[:10]

for pair, prb in top_pairs_c:
    print(f"Ordered Pair: {pair}, Probability: {prb:.4f}")



