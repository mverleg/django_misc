
from random import shuffle


'''
	symbols that will be obfuscated (others will remain identical)
'''
ENCCHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,!?_@+-*'


'''
	obfuscate a single letter; not cryptographically strong
	but simple and should be good enough to stop some spam bots  
'''
def obfuscate_letter(letter, pos, encchars = ENCCHARS):
	try:
		nr = encchars.index(letter)
	except ValueError:
		return letter
	newnr = (nr + pos**2 + 42) % len(encchars)
	return encchars[newnr]


''' the inverse is not actually used in python, just js version '''
def deobfuscate_letter(letter, pos, encchars = ENCCHARS):
	try:
		nr = encchars.index(letter)
	except ValueError:
		return letter
	oldnr = (nr - pos**2 - 42) % len(encchars)
	return encchars[oldnr]


if __name__ == '__main__':
	initial = list('~!@#$%^&*()_+`1234567890-=[]\{}|;\':"<>?,./qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
	shuffle(initial)
	initial = ''.join(initial)
	print 'testing obfuscation for %s' % initial
	obfuscated = ''.join(obfuscate_letter(letter, k) for k, letter in enumerate(initial))
	print 'obfuscated: %s' % obfuscated
	restored = ''.join(deobfuscate_letter(letter, k) for k, letter in enumerate(obfuscated))
	print 'restored: %s' % restored
	if restored == initial:
		print 'SUCCESS'
	else:
		print 'FAILED!'


