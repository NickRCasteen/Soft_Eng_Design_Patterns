#Andy Curtis
#This is my implimentation of the facade data pattern.

class Facade:

    def __init__(self):
        self._part_1 = Part1()
        self._part_2 = Part2()

    def performSpeach(self):
        self._part_1.giveIntroduction()
        self._part_1.byCalling()
        self._part_2.weCan()
        self._part_2.ofMult()


class Part1:
    def giveIntroduction(self):
        print("This is an example of a facade.")

    def byCalling(self):
        print("By calling only the single facade class,")


class Part2:
    def weCan(self):
        print("we can use different functions")

    def ofMult(self):
        print("of multiple classes absorbed by the facade")


def main():
    facade = Facade()
    facade.performSpeach()


main()
