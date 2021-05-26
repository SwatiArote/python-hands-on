list = [1,2,99,0,-5]
print(list.reverse())
print(list)
print(list.sort())
print(list)

#method changes or iteract with objcts
#import matplotlib.pyplot as plt

class Circle(object):
    def __init__(self,radious,color):
        self.radious = radious
        self.color = color

    def addRadiaus(self, r):
        self.radious = self.radious + r

    # def drawCircle(self):
    #     plt.gca().add_patch(plt.Circle((0, 0), radious=self.radious, fc=self.color))
    #     plt.axis('scaled')
    #     plt.show()

class Sqaure(object):
    def __init__(self,side,color):
            self.side = side
            self.color = color




RedCirecle = Circle(4,'red')
print(RedCirecle.color, RedCirecle.radious)
RedCirecle.color = 'yellow'
print(RedCirecle.color, RedCirecle.radious)
RedCirecle.addRadiaus(8)
print(RedCirecle.radious)

redSqaure = Sqaure(2,'blue')
print(redSqaure.side,redSqaure.color)
print(dir(RedCirecle))

# Find out the methods can be used on the object RedCircle

class analysedText(object):
    def __init__(self, text):
        formatedText = text.replace(',', '').replace('.', '').replace('!', '').replace('?', '')
        formatedText = formatedText.lower()
        self.fmtText = formatedText

    def freqAll(self):
        words = self.fmtText.split(' ')
        dir = {}
        for word in set(words):
            dir[word] = words.count(word)
        return dir

    def freqOf(self, word):
        frq = self.freqAll
        if (word in frq):
            return frq[word]
        else:
            return 0

