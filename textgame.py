print 'welcome to the game! do you want to go left or right?'
response1 = raw_input()
if response1 == 'left':
    # something here
    print 'you found a burger! do you want to eat it?'
    response2 = raw_input()
elif response1 == 'right':
    # something else here
    print 'you died. sorry.'
    exit() # this command exits the program. try it out!

if response2 == 'yes':
    print 'you ate the burger. unfortunately it was poisoned and you died. sorry.'
    exit()
elif response2 == 'no':
    print 'you didn\'t eat the poisonous burger! do you want to keep walking?'
    response3 = raw_input()

if response3 == 'yes':
    print 'you kept on walking and found a phone. do you want to eat it?'
    # some things here
    response4 = raw_input()
    if response4 == 'yes':
        print 'you choke on it but you live.'
    elif response4 == 'no':
        print 'you pick the phone up and put it in your pocket'
        
elif response3 == 'no':
    print 'you stood still. now are you going to keep walking?'
    
