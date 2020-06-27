def square(num):
    return num * num
print(square(6))

#one line expression that automatically returns. not typically stored in a variable like below
square2 = lambda num: num * num
print(square2(6))

#used if you have code where you need to pass a function into another function as a param and function will never be used again

cube = lambda num: num * num * num

print(cube(8))