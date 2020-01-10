# -*- coding: utf-8 -*-
from logging import warning

from xpinyin import Pinyin

xpinyin = Pinyin()


def to_pinyin(cny, delim=None, splitter=' ', tone_marks=True):
	if delim is not None:
		splitter = delim
		warning('"delim" argument is now called "splitter"')
	return xpinyin.get_pinyin(cny, splitter=splitter, tone_marks=tone_marks)


def to_pinyin_ascii(cny, splitter=' ', tone_marks=False):
	return to_pinyin(cny, splitter=splitter, tone_marks=tone_marks)


def to_pinyin_full(cny, splitter='', tone_marks=True):
	return to_pinyin(cny, splitter=splitter, tone_marks=tone_marks)


if __name__ == '__main__':
	print(to_pinyin(u'好奇'))
	# note that this should be 4th-2nd tone


