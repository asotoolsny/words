import re
from collections import Counter

import urllib3

import charts


def download_url_as_text(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    http = urllib3.PoolManager()
    response = http.request("GET", url)
    contents = response.data.decode("utf-8")

    return contents


# download the ebook from the project gutenberg (Leo Tolstoi's "War and Peace")
# after running the project, try with other books in the website
book_text_url = "https://www.gutenberg.org/files/2600/2600-0.txt"
book_text = download_url_as_text(book_text_url)

# extract words by splitting the text, re.sub() is a regex method of splitting into words
all_words = re.sub("[^\w]", " ",  book_text).split()

# convert all words to lowercase, so we can count all cases ("The" and "the" is the same word)
all_words = [word.lower() for word in all_words]

# count word frequencies (occurrence count)
word_counter = Counter(all_words)

# extract top words and combine the rest under "Other words"
most_common_words = word_counter.most_common(10)
# most_common_words.append(("Other words", sum(word_counter.values())-sum(wc[1] for wc in top_words2)))

print(most_common_words)
print(sum(wc for wc in word_counter.values()))

# prepare data for donut chart
# labels are in "word (count)" format, e.g. "the (35000)"
# see https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36 for formatting
top_words_labels = [f"{kv[0]} ({kv[1]})" for kv in most_common_words]
top_words_counts = [kv[1] for kv in most_common_words]

charts.draw_donut(top_words_labels, top_words_counts)
