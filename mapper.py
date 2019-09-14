#!/usr/bin/env python
import sys
from sklearn.feature_extraction import stop_words
import string

stopwords = set(stop_words.ENGLISH_STOP_WORDS)

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower().translate(None, string.punctuation)

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stopwords:
            print '%s\t%s' % (word, "1")
