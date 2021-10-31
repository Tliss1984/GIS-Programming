def cumsum(t):
   
    total = 0
#empty list that is filled by for loop
    assign = []
#for loop that fills empty list with the cumulative sums based on the given list (t)
    for x in t:
        total += x
        assign.append(total)
    return assign


t = [3,1,4,6,4,3]
print (cumsum(t))
