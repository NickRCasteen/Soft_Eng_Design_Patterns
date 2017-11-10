#Andy Curtis
#This is my implimentation of the State design pattern.

import abc

#The function that can change depending on the state of the program
class Context:
    def __init__(self, state):
        self._state = state

    def doYourThing(self):
        self._state.handle()


#This keeps track of what state the program is in
class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self):
        print("handling the pure state")


#What the function does when in state A
class ConcreteStateA(State):
    def handle(self):
        print("behavior of state A")


#What the function does when in state B
class ConcreteStateB(State):
    def handle(self):
        print("Behavior of state B")


#Here, the out put of changingFunction.doYourThing can change, based
#on the current state of the program. 
def main():
    concrete_state_a = ConcreteStateA()
    concrete_state_b = ConcreteStateB()
    changingFunction = Context(concrete_state_a)
    x = 0
    while(x < 4):
        #The state of the program depends on how far through the loop it is
        if(x < 2):
            changingFunction = Context(concrete_state_a)
        else:
            changingFunction = Context(concrete_state_b)

        #This single function call changes output depending on the state
        changingFunction.doYourThing()
        x += 1

main()
