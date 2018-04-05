'''
Closet program
'''
from enum import Enum
from random import randint


class Material(Enum):
    WOOD = 'Wood'
    CARBON = 'Carbon'
    GLASS = 'Glass'


class Wardrobe:

    def __init__(self, name = '', material = '', opened = False, occupied = False, broken = False):
        self.name = name
        self.opened = opened
        self.occupied = occupied
        self.broken = broken
        if isinstance(material, Material):
            self.material = material
        else:
            raise Exception("Valid values for materials are: Material.WOOD, Material.CARBON, Material.GLASS")


    def open(self):
        if not self.opened:
            self.opened = True
            print("You have opened the wardrobe.")
        else:
            print("The wardrobe is already open.")

    def close(self):
        if self.opened:
            self.opened = False
            print("You have closed the wardrobe.")
        else:
            print("The wardrobe is already closed.")

    def get_in(self):
        if self.opened and not self.occupied:
            self.occupied = True
            print("You stepped into the wardrobe.")
        elif not self.opened:
            print("You need to open the wardrobe before you can get in.")
        elif self.occupied:
            print("You are already in the wardrobe!")

    def get_out(self):
        if self.opened and self.occupied:
            self.occupied = False
            print("You got out of the wardrobe.")
        elif not self.opened and self.occupied:
            print("You need to open the door before you can get out.")
        elif not self.occupied:
            print("You are not in the wardrobe!")

    def kick(self):
        if self.material == Material.CARBON:
            if randint(1,1000) == 666:
                self.broken = True
                print("Wow! That broke the wardrobe! Are you Bruce Lee?")
            else:
                print("Ouch! That hurt your foot!")
        elif self.material == Material.WOOD:
            if randint(1,100) == 69:
                self.broken = True
                print("Woops, that broke the wardrobe!")
            else:
                print("It's sturdy wood, the wardrobe is fine")
        elif self.material == Material.GLASS:
            if randint(1,10) == 8:
                self.broken = True
                print("That broke it. What idiot would kick a glass wardrobe?!")
            else:
                print("You lucky bastard, the glass is still in one piece")


kast = Wardrobe('klerekast', Material.GLASS)

# kast.open()
# kast.open()
# kast.get_out()
# kast.get_in()
# kast.close()
# kast.get_out()
# kast.open()
# kast.get_out()
# kast.close()

kast.kick()
