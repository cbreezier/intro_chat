from random import randint
import time

print 'SUP MANG, Welcome do DA WORLD OF MANG'
time.sleep(1)
print 'What DIFFICULTY do you want to play?'
difficulty = raw_input()

if difficulty == 'MANG' or difficulty == 'mang':
	print 'Smart choice.'
else:
	print "That's too easy mang, time to change the difficulty to MANG."
time.sleep(1)
print 'You see a mysterious building in front of you, do you wish to enter?'
action1 = raw_input()
if 'y' in action1 or 'Y' in action1:
	print 'The building is old and worn out...'
	time.sleep(1)
	print 'You take a wrong step and it collapses on you!'
	time.sleep(1)
	print 'You are dead.'
	time.sleep(1)
	print 'GG'
else:
	print 'The building collapses as you walk past it, barely escaping injury.'
	time.sleep(1)
	print 'You see a magical pony deity floating in front of you, do you want to make a wish?'
	pony = raw_input()
	
	if 'y' in pony or 'Y' in pony:
	
		print 'You get scammed by the pony as it takes all of your money!'
		time.sleep(1)
		print 'You die of starvation :('
		time.sleep(1)
		print 'GG'
	else:
		print 'The pony looks hurt as it flies away :('
		time.sleep(1)
		print 'The legendary dice roller MANG appears in front of you!'
		time.sleep(1)
		print 'He ROLLS the dice.'
		time.sleep(1)
		print 'Guess his number, from 1-6.'

		dice = randint(1,6)

		
		guess = int(raw_input())

		

		print 'You guessed', guess
		time.sleep(1)
		print 'The correct number was', dice
		time.sleep(1)
		while guess == dice:
			
			print 'Congratulations MANG, you win'
			time.sleep(0.5)

		if dice != guess:
			print 'Bad luck MANG, you lose'
		

