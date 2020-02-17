import time
from enum import Enum


class Right(Enum):
	wrong = 1
	partiallywrong = 2
	partialycorrect = 3
	correct = 4
	

class FlashCard:
	def __init__(self, question,answer, num):
		self.question = question
		self.answer = answer
		self.num = num
		self.guess = None
		self.clock = None
		self.asked = False
		self.answered = False
		
	def showQuestion(self):
		return self.question
		
	def showAnswer(self):
		return self.answer
		
	def askQueston(self):
		print(self.showQuestion())
		start = time.time()
		p = input()
		while(p!=''):
			p = input()		
		end = time.time()
		print(self.showAnswer())
		self.clock = end - start 
		self.asked = True
		self.askResult()
		return end-start
		
	def askResult(self):
		print("How well did you answer the question?")
		print("1 for wrong, 2 for partialy correct, 3 partially wrong,4 for correct")	
		p = int(input())
		if(p == 1):
			self.guess = Right.wrong
		if(p == 2):
			self.guess = Right.partialycorrect
		if(p == 3):
			self.guess = Right.partiallywrong
		if(p == 4):
			self.guess = Right.correct
		self.answered = True				
		
		
		
karta1 = FlashCard("How do u do", "Good thanks", 2)
print(karta1.asked)
print(karta1.answered)
karta1.askQueston()
print(karta1.clock)
print(karta1.guess)
print(karta1.asked)
print(karta1.answered)
