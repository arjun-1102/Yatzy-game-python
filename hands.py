from dice import D6

class Hand(list):
	def __init__(self, size = 0, die_class=None, *args, **kwargs):
		if not die_class:
			raise ValueError("You must provide a die class")
		super().__init__()
		
		for _ in range(size):
			self.append(die_class())
		self.sort()
	
	def _by_balue(self, value):
		dice = []
		for die in self:
			if die == value:
				dice.append(die)
		return dice

class YatzyHand(Hand):
	def __init__(self, *args, **kwargs):
		super.__init__(size = 5, die_class=D6, *args, **kwargs)
		
	@property
	def ones(self):
		return self._by_balue(1)
		
	@property
	def twos(self):
		return self._by_balue(2)
		
	@property
	def threes(self):
		return self._by_balue(3)
		
	@property
	def fours(self):
		return self._by_balue(4)
		
	@property
	def fives(self):
		return self._by_balue(5)
		
	@property
	def sixes(self):
		return self._by_balue(6)

	@property
	def _sets(self):
		return{
			1: len(self.ones),
			2: len(self.twos),
			3: len(self.threes),
			4: len(self.fours),
			5: len(self.fives),
			6: len(self.sixes)
		}
##-----
#import dice, hands
#hand = hands.Hand(size = 5, die_class=dice.D6)
#hand
#len(hand)
#hand[0].value
			
##---- 

#from hands import YatzyHand
#yh = YatzyHand()
#yh

