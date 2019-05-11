import re

from blingfire import *

text = 'This is the Bling-Fire tokenizer'
output = re.sub("[^\w]", " ",  text_to_words(text)).split()

print(output)
