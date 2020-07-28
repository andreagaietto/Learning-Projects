import pdb

first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)


#import pdb
#pdb.set_trace()

#also commonly on one line:
#import pdb; pdb.set_trace()

#Common pdb commands:
# l (list)
# n (next line)
# p (print) and then type variable name to get value
# c (continue - finishes debugging)
#can type variable names to check values at various times