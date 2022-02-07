# this program counts the frequency of characters on a string.
from cgitb import text
import pprint as pp 

text = "Yunnan University is the one of the biggest universities in Yunnan province."

letters = {}

for i in text:
    letters.setdefault(i, 0)
    letters[i] = letters[i]+1

pp.pprint(letters)
