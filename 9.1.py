

def read(words):
#opens word list    
    txt = open(words)
#for loop to see if words are more than 20 characters
    for line in txt:
        a = line.strip()
        if len(a) > 20:
#prints words
            print (a)
			
read('words.txt')

