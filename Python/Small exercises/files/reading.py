#file = open('story.txt')
#print(file.read())
#file.seek(0) #moves cursor to the beginning of the file
#file.readline() #stops when it hits new line character
#file.readlines() #all lines in a list
#file.close()#self explanatory


#preferred syntax:
with open('story.txt') as file:
    print(file.readline())

#file automatically closes with the above