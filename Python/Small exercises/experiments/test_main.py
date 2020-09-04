from test_class import Temp
def main():
    class1 = Temp(98.7)
    print(class1._temperature)
    print(class1.temp)
    class1.temp = 95
    print(class1._temperature)
    print(class1.temp)
    class1.temp = -85
    print(class1._temperature)
    print(class1.temp)

 
    




main()