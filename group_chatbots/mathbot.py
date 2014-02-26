import re

user, message = raw_input().split(":")
matches = re.search(r'([0-9]+) *([+\-*/%]) *([0-9]+)', message)
if matches:
  expression = ' '.join(matches.groups())
  if ((matches.group(2) == '%' or matches.group(2) == '/') and matches.group(3) == '0'):
    print("@%s I'm not stupid you know, you can't try and break me by making me divide by zero!" % user)
  else:
    print("@%s %s = %f" % (user, expression, eval(expression)))
else:
  print "Sorry, I didn't understand. Maybe I'm too dumb =[ (I can only understand operations with + - * / % with two integers)"