# -*- coding: utf-8 -*-

from xpinyin import Pinyin


p = Pinyin()


def to_pinyin(cny, delim = ' '):
	return p.get_pinyin(cny, delim, show_tone_marks = True)

if __name__ == '__main__':
	print to_pinyin(u'好奇')
	# note that this should be 4th-2nd tone


