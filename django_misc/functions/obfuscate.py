

'''
	obfuscate a single letter; not cryptographically strong
	but simple and should be good enough to stop some spam bots  
'''
def obfuscate_letter(letter, pos, mi, ma):
	nr = ord(letter)
	if mi <= nr <= ma:
		return chr((nr - mi + pos ** 2) % (ma - mi) + mi)
	return letter


''' the inverse is not actually used in python, just js version '''
def deobfuscate_letter(letter, pos, mi, ma):
	nr = ord(letter)
	if mi <= nr <= ma:
		return chr((nr - mi - pos ** 2) % (ma - mi) + mi)
	return letter


