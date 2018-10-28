

trigger = True


class car():


    def __init__(self,color,money):
        self.color = color
        self.money = money

    def incAmount(self):
        global trigger

        for x in range(10):
            if trigger == True:
                print('trigger is true')
                trigger = False
            if self.money == 8:
                trigger = True
            self.money = self.money + 1
            print(self.money)

xyz = car('blue',3)

xyz.incAmount()
