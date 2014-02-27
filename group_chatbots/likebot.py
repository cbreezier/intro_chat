user, message = raw_input().split(":")

if ' like ' in message:
  likeableObject = message.split(' like ')[1]
  print '@'+user, 'I like', likeableObject, 'too!' 