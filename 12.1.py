#function to create a dictionary that keeps track of how many letters are in a given string
def histogram(test):
#if a letter is not in the dictionary it is put inside it with the value of one. If the letter is already inside it's value is increased by one.  
    dictionary = {}
    for letter in test:
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1
    print(dictionary)    
    return dictionary
#creates a tuple out of the dictionary and sorts it into decending frequency. 
def most_frequent(test):
    freq=histogram(test)
    dict2 = {}
    for letter, dictionary in freq.items():
        dict2[dictionary] = letter
    for letter in sorted(dict2,reverse=True):
        reverse=( dict2[letter])
        print (reverse)
test='aaabbbbbnnnnnnjjjjjjjjjjjjuuuuuuuuuuuuuuag'
most_frequent(test)
