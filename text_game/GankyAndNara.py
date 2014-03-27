print "welcome to this game!"
print "do you want to go left or right?"
response = raw_input()
if response == "left":
    print "you went left!"
    print "you encountered a dragon! do you want to fight it?"
    hp = 50
    print 'hp is', hp
    response = raw_input()
    while response == "no":
        hp -= 10
        if hp <= 0:
            print "you died. you fail at life"
            exit()
        else:
            print 'you lo5t some hp, your hp is now', hp
            print "you can't escape!"
            print "you encountered a dragon! do you want to fight it?"
        response = raw_input()
    print "The Dragon shit itself. it doesnt wanna fight"
    print "You Won bitch"
    exit()


elif response == "right":
    print "you went up!"
    print "a wild sphinx! what do you want to do? tackle, run"
    hp = 50
    print 'your hp is', hp
    response = raw_input()
    sphynxHP = 80
    while sphynxHP != 0:
        while response != 'tackle' and response != 'run':
             print "you can only run or tackle. WHat do you want to do?"
             response = raw_input()
        while response == "tackle" and sphynxHP > 0:
            print "you used tackle. It's Super Effective"
            sphynxHP -= 20
            print "sphynx's hp is", sphynxHP
            hp -= 5
            print "the sphynx attacked, your hp is", hp
            response = raw_input()
        while response == "run":
            print "sphinx's arena trap prevents escape!"        
            hp -= 10
            if hp <= 0:
                print "you died. you fail at life"
                exit()
            else:
                print 'you lo5t some hp, your hp is now', hp
                print "you can't escape!"
                print "The sphynx became angry! do you want to fight it?"
            response = raw_input()
    
    print "The sphynx blew itself up. It can't fight"
    print "You Won bitch"
    exit()

else:
    print "Learn some English fag"
