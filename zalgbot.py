# ZalgBot
# (c) 2017 Koen Bolhuis

import random

zalgo_up = [
	'\u030d', '\u030e', '\u0304', '\u0305', 
	'\u033f', '\u0311', '\u0306', '\u0310', 
	'\u0352', '\u0357', '\u0351', '\u0307', 
	'\u0308', '\u030a', '\u0342', '\u0343', 
	'\u0344', '\u034a', '\u034b', '\u034c', 
	'\u0303', '\u0302', '\u030c', '\u0350', 
	'\u0300', '\u0301', '\u030b', '\u030f', 
	'\u0312', '\u0313', '\u0314', '\u033d', 
	'\u0309', '\u0363', '\u0364', '\u0365', 
	'\u0366', '\u0367', '\u0368', '\u0369', 
	'\u036a', '\u036b', '\u036c', '\u036d', 
	'\u036e', '\u036f', '\u033e', '\u035b', 
	'\u0346', '\u031a'
]

zalgo_mid = [
	'\u0315', '\u031b', '\u0340', '\u0341', 
	'\u0358', '\u0321', '\u0322', '\u0327', 
	'\u0328', '\u0334', '\u0335', '\u0336', 
	'\u034f', '\u035c', '\u035d', '\u035e', 
	'\u035f', '\u0360', '\u0362', '\u0338', 
	'\u0337', '\u0361', '\u0489' 
]

zalgo_down = [
	'\u0316', '\u0317', '\u0318', '\u0319', 
	'\u031c', '\u031d', '\u031e', '\u031f', 
	'\u0320', '\u0324', '\u0325', '\u0326', 
	'\u0329', '\u032a', '\u032b', '\u032c', 
	'\u032d', '\u032e', '\u032f', '\u0330', 
	'\u0331', '\u0332', '\u0333', '\u0339', 
	'\u033a', '\u033b', '\u033c', '\u0345', 
	'\u0347', '\u0348', '\u0349', '\u034d', 
	'\u034e', '\u0353', '\u0354', '\u0355', 
	'\u0356', '\u0359', '\u035a', '\u0323' 
]

zalgo_chars = set(c for c in (zalgo_up + zalgo_mid + zalgo_down))

def random_char(chars):
	"""
	returns a random zalgo character from the given list
	"""
	
	idx = random.randint(0, len(chars) - 1)
	return chars[idx]

def zalgo_text(text, amount=1, up=True, down=True, mid=True):
	"""
	amount can be 0, 1 or 2
	"""
	
	new_text = []
	
	for c in text:
		if c in zalgo_chars:
			continue
		
		new_text.append(c)
		
		num_up = random.randint(0, 15) // 2 + 1
		num_mid = random.randint(0, 5) // 2
		num_down = random.randint(0, 15) // 2
		
		if amount == 0:
			num_up = random.randint(0, 7)
			num_mid = random.randint(0, 1)
			num_down = random.randint(0, 7)
		elif amount == 2:
			num_up = random.randint(0, 63) // 4 + 3
			num_mid = random.randint(0, 15) // 4 + 1
			num_down = random.randint(0, 63) // 4 + 3
		
		if up:
			for i in range(num_up):
				new_text.append(random_char(zalgo_up))
		if mid:
			for i in range(num_mid):
				new_text.append(random_char(zalgo_mid))
		if down:
			for i in range(num_down):
				new_text.append(random_char(zalgo_down))
	
	return ''.join(new_text)

# Bot functionality

TOKEN = ''

with open('assets/token.txt', 'r') as token_file:
	TOKEN = token_file.read()

if TOKEN == '':
	print('Could not read token (assets/token.txt)')


