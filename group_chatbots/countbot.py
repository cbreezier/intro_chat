import re
user, message = raw_input().split(':')

if '@countbot' in message:
    matches = re.search('count to ([0-9]+)', message)
    if matches:
        countTo = int(matches.group(1))
        print 'Counting to', str(countTo) + ':'
        print ', '.join(map(lambda x: str(x), range(1, countTo + 1)))
    else:
        print 'I have no idea what you just asked me to do...'

