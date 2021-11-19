


#original string and the string to replace it with
pattern = 'original'
replace = 'replacement'

#paths of txt file that is opened and created
fileread = 'Untitled.txt'
filewrite = 'filewrite.txt' 

#function that opens text file, finds a defined string, and creates a new txt file with the found string replaced with a new one
def sed(pattern, replace, source, dest):
 
    txt1 = open(fileread, 'r')
    txt2 = open(filewrite,'w' )

    for string in txt1:
        string = string.replace(pattern, replace)
        txt2.write(string)
        
    #properly closes txt files
    txt1.close()
    txt2.close()

#calls the function
sed(pattern, replace, fileread, filewrite)





