
#This program will demonstrate the structure and method of
	#SWAPPING ALGORITHMS FOR A CLASS BASED ON USER NEEDS

import abc


#>>> MID-END, as I call it. 2 middle-men between the algorithms and the client. <<<
#This is the strategy abstract class, wrapping the two subclasses that actually contain the algorithms we'll swap between
class Strategy(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def Op_Perform(self):
		pass #This is an abstract method, so there's no implementation...at all. THAT'S done by the subclasses.

#Here's the interface. This thing will act as the ambassador for the strategy and its subclasses.
class Context:
	def __init__(self, strat):
		self.strategy = strat
	def interface(self):
		self.strategy.Op_Perform() #This just runs the Op_Perform. No care for what class ACTUALLY got passed in.




#-------------------------------------------------------------------------------------------------------------------------------------------------------





#>>> THE DIFFERENT STRATEGIES. These are, essentially, the algorithms we swap out. <<<
class True_Strategy_A(Strategy):
	def Op_Perform(self):
		print "Hello From Strategy A! It's hard to prove I'm not cheating just by running this, so look at the source!"

class True_Strategy_B(Strategy):
	def Op_Perform(self:
		print "Hello From Strategy B! Who knows, maybe I just hardcoded all this??? Only way to know is to look at source!"

#Something interesting to note is how the main program is the one making these. It makes a new True_Strategy_A or B and passed it to the interface.
#So this doesn't really eliminate having to make a subclass. What it DOES do is provide a fair amount of decoupling.




#-------------------------------------------------------------------------------------------------------------------------------------------------------



#>>> MAIN PROGRAM <<<
notdone = True #This and
chosen = False #This are just two booleans I'm using for the loop.
print "Type A or B, which determines which strategy the system will use. C to exit."

while notdone:
	x = raw.input("\n") #First, take your simple input
	if x == "A":
		strat_chosen = True_Strategy_A() #We set the chosen strat to True_Strategy_A
		chosen = True #And flag that we've chosen one
	elif x == "B":
		strat_chosen = True_Strategy_B() #Or we do B, who knows.
		chosen = True
	elif x == "C":
		notdone = False #Here's your old quick exit.
	else:
		print "invalid"

	if chosen == True:
		#So, the big idea is that, based on some input, you'll want to alter which strategy you pass into Context.
		#For a bare-bones example (that you ALSO can't prove in runtime, say we have the user input an equation
		#If they put in 2+2, then we could direct the program towards the addition implementation of strategy
		#Alternatively, 2*2 needs the multiplication implementation.

		chosen = False #So, just to make sure we don't always perform an operation, we set this back to false
		context_int = Context(strat_chosen) #So, here, we don't care which strategy we've chosen and put into strat_chosen. Whatever it is, it's
							#getting run...so long as it has an Op_Perform, I assume!
		context_int.interface() #Then, run the context and let it handle everything!





