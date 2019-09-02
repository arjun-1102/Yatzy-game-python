import random

class Die:
	def __init__(self, sides = 2, value = 0):
		if not sides >=2:
			raise ValueError("Must have at least 2 sides")
		if not isinstance(sides, int):
			raise ValueError("Side must be whole number")
		if not isinstance(value, int):
			raise TypeError("Value must be whole number")
		self.value = value or random.randint(1,sides)
		
	def __int__(self):
		return self.value
	
	def __eq__(self, other):
		return int(self) == other
		
	def __ne__(self, other):
		return int(self) != other
		
	def __gt__(self, other):
		return int(self) > other
		
	def __lt__(self, other):
		return int(self) < other
		
	def __ge__(self, other):
		return int(self) > other or int(self) == other
		
	def __le__(self, other):
		return int(self) < other or int(self) == other
		
	def __add__(self, other):
		return int(self) + other
		
	def __radd__(self, other):
		return self + other
		#return int(self) + other
		
	def __repr__(self):
		return str(self.value)
	
class D6(Die):
	def __init__(self, value=0):
		super().__init__(sides = 6, value = value)

# ##--- Part 1	
# import dice
# d6 = dice.D6()
# d6.value
#objs = list()
#for i in range(10):
#    objs.append(MyClass())

# ##--- Part 2
# from dice import D6
# d6 = D6()
# int(d6)
# d6 < 2
# d6 > 2
# d6 <=2
# d6 ==4
# d6 != 5
# d6 == 6

