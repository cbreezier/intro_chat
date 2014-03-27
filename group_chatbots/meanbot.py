# message format:
# User: i, i am a person

user, message = raw_input().split(":")

if "@meanbot" in message:
	if "hi" in message:
		print "@" + user + ", Hi? Is that the bounds of your vocabulary"
	elif "you are mean" in message:
		print "@" + user + ", Well you look terribe today."
	else:
		print "@" + user + ", You know... I think you look like a beaver. But not just any beaver, a ugly one. In fact so ugly that when a mirror looks at you in crys and calls over the tissues so it can whipe up its tears. Your hair causes me pain by the way, I feel that you must connect with things of your nature... like maybe an ant. Yes an ant, a lifeless ground-dwelling ant."	