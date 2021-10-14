

print("Exercise 5.1")

import time
import math

#assigns time module to variable
a=time.time()
 
# calculations to determine each part of the current time
days = a//(60*60*24)
hours = (a-days*60*60*24)//3600
minutes = (a-((days*60*60*24)+(hours*3600)))//60
seconds = a-((days*60*60*24)+(hours*3600)+(minutes*60))

#string to display time
print("The time is",int(hours),":",int(minutes),".",int(seconds),"GMT and",int(days),"days since January 1st, 1970")

print ("Exercise 5.2")


def check_fermat(A, B, C, N):
    #checks to see if user inputs pass therom 
	if N > 2 and A**N + B**N == C**N:
		print ("Holy smokes, Fermat was wrong!")
	else:
		print ("No, that doesn’t work.")

#user input requests
A=int(input("Is Fermet's Last Therom True? Input 4 values(a,b,c,n>2) starting with A:"))
B=int(input('B:'))
C=int(input('C:'))
N=int(input('N:'))

check_fermat(A,B,C,N)
       


print("Exercise 6.3")


def is_palindrome(word):
    #tests the first and last characters to see if they are a match
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    #drops the first and last characters and instructs to repeat
    return is_palindrome(word[1:-1])

#test palidromes
print(is_palindrome('Geospatial Programming'))
print(is_palindrome('TorylissssilyroT'))
print(is_palindrome('god dog'))

    






