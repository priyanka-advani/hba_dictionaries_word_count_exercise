# put your code here.

from sys import argv


def count_words(txt_file):
    """Count words function will read a text file input and print each word and
    that word's count"""

    opened_file = open(txt_file)
    word_count = {}

    read_opened_file = opened_file.read()
    read_opened_file = read_opened_file.split()

    for word in read_opened_file:
        word = word.rstrip('?,.;!:"_')
        word_count[word.lower()] = word_count.get(word.lower(), 0) + 1

    for word, count in word_count.iteritems():
        print word, count

    opened_file.close()

count_words(argv[1])
