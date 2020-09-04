class Temp:

    def __init__(self, temperature):
        self._temperature = temperature


    def to_celsius(self):
        return (self._temperature - 32) / 1.8

    @property
    def temp(self):
        print("@property")
        return self._temperature

    @temp.setter
    def temp(self, temp):
        print("setter")
        if temp > 120:
            raise ValueError("That's way too hot")
        elif temp < -20:
            raise ValueError("That's way too cold")
        else:
            self._temperature = temp

   
