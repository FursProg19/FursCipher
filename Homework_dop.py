class Animal:
    def __init__ (self, weight , height, eyesColor):
        self.weight = weight
        self.height = height
        self.eyesColor = eyesColor
    def breath (self):
        pass
    def sleep (self):
        pass
    def vocalize (self, loudness):
        print ('vocalizing with loudness {}'.format(loudness))

class Pet (Animal):
    def __init__(self, name, weight , height, eyesColor):
        super().__init__(weight , height, eyesColor)
        self.name = name
    def breath (self):
        print ('{} is breathing'.format(self.name))
    def vocalize (self, loudness):
        print ('my name is {}'.format(self.name))
        super().vocalize(loudness)
class Cat(Pet):
    def __init__ (self, name, weight , height, eyesColor, tailLenght):
        super().__init__(name, weight , height, eyesColor)
        self.tailLenght = tailLenght
    def vocalize (self, loudness):
        super().vocalize(loudness)
        print ('m{}{}w'.format('e'*loudness,'o'*loudness*2)) 
    


cat = Cat('sirko',5,0.75, 'Blue',0.20)
cat.vocalize(10)








