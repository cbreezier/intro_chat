# message format:
# User: hi, i am a person
	
user, message = raw_input().split(":")

if "@jayananth" in message:
    if "v=iyer" in message:
      print"@" + user + "good job, you know where your going with your life."
    elif "jayananth" in message:
      print "@" + user + "on ya mate"
    else:
      print " oi, are you retarded?"
        