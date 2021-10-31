def nested_sum(t):


#   adds all the numbers in each list to the sum total
    sumtotal = 0
    for integer in t:
        sumtotal += sum(integer)
    return sumtotal



t = [[100,25,2],[45,6,32]]

#prints sum
print (nested_sum(t))

