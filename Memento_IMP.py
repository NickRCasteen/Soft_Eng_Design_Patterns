
#This program will demonstrate the structure and method of:
	#CREATING A CLASS AND STORING THE CLASS STATE TO BE ROLLED BACK TO THAT STATE,

import pickle


#The originatpr class. This is the class whose states we'll save as we perform operations. We'll do a few operations here, 2 just to prove it's real
class Origin:
	def __init__(self):
		self.bol = False #This and
		self.total = 0 #this are the values we change. Simple operations just to show off the different states.

	def create_state(self):
		return pickle.dumps(vars(self)) #Here we dump all the variables from the object and return it. It'll be pushed onto our state stack.

	def restore_state(self, state):
		prev_state = pickle.loads(state) #For the passed in state, we load
		vars(self).clear() #We clear
		vars(self).update(prev_state) #We apply. Vars has an update function that can use what pickle.loads returned.


#A STACK CLASS Wholesale copy/pasted from http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html
#because I didn't want to require you to install numpy. Though, looking at it, I could've just simulated a stack with the built-in
#append and pop list functions but, eh, live and learn.
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


#MAIN PROGRAM
print "Type 1 to add a number to total, Type 2 to switch the Boolean, Type 3 to Undo, Type 4 to quit. Undo can be applied multiple times."

states = Stack()
notdone = True
org = Origin()

while notdone:
	print "Total is:"
	print org.total
	print "bol is:"
	print org.bol
	x = raw_input("\n") #Take input!
	if x == "1":
		print"type num to add to total. No error checking on input."
		y = raw_input("\n")
		try:
			
			z = int(y) #So we got cheeky and added a try/catch. This is the part that might fail.
			states.push(org.create_state()) #After that, save the state BEFORE changing.
			org.total += z #and THEN change/
		except ValueError:
			print "Please enter valid number."

	elif x == "2":
		states.push(org.create_state()) #Again, save the state BEFORE changing, because if we want to undo an action, we have to know what to pull.
		if org.bol == False:
			org.bol = True
		else:
			org.bol = False #So we switch a boolean. Hoo-ray.

	elif x == "3":
		if states.isEmpty():
			print "No states to load." #A little check, don't want to go overboard.
		else:
			x = states.pop()
			org.restore_state(x) #I know this might seem random to you, but this is to reprimand me: Do mind you ()s on your method calls.
	elif x == "4":
		notdone = False
	else:
		print "invalid"





