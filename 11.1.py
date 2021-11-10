def words_dict(test):

#opens file and creates a new dictionary
    wordstxt={}
    dictionary = open("words.txt")
    
#takes words from words.txt and places them in empty dictionary as keys with values of 1
    for word in dictionary:
       wordstxt[word.strip()]=1


# tests to see if word is in dictionary
       
    if test in wordstxt:
        print (True)
    else:
        print(False)
  

    print(wordstxt['hello'])
    
words_dict("hello")
