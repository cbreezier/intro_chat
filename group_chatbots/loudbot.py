user,message = raw_input().split(":")
if "@loudbot" in message:
	print "@" + user + message.upper() 