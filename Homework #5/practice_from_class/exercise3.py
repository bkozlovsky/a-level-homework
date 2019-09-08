import sys
import collections

#initializing sys.argv to catch a file with English text from console
filename = sys.argv[1]

#an empty list to convert text into a list of words
words_list = []

with open(filename, 'r') as f:
    words_list = f.read().split()

#function removes bad chars from words
def remove_chars(word):
    bad_chars = '?!,.”“}{)(*%$@#&'
    word = word.strip(bad_chars).lower()
    return word

#using map() to generate a list of words without bad chars
final_list = list(map(remove_chars, words_list))

def counts_words(wordlist):
    d = collections.Counter(wordlist)
    d = sorted(d.items(), key=lambda i: i[1], reverse=True)
    print(*["A word '{}' occurs {} times\n".format(n[0], n[1]) for n in d])

counts_words(final_list)