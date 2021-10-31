#function to see if theres an e in a word
def has_no_e(word):
	if "e" not in word:
		return True
	else:
		return False
	
#function that keeps track of how many non-e words have been discovered
def aretherees(f):
#tally of how many no-e words and total words have been scanned
    no_e = 0
    all_words = 0
    file = open(f)
# for loop that increases tally and prints non-e words
    for line in file:
        all_words += 1
        word = line.strip()
        if has_no_e(word):
             print (word)
             no_e += 1
# calculates and prints percentage
    print (no_e / all_words*100)


aretherees('words.txt')
