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


def get_counts(words):
    # now this can be a bit confusing at first
    # imagine that you assign a variable for counting the given word
    # to count all the occurrences of the word, you would need to iterate through all the words
    # and whenever you meet the same word, you would increase your counter (variable).
    #
    # like this (in this sample we count "the" word):
    # the = 0
    # for word in words:
    #     if word == "the":
    #         the = the + 1
    # print(f"'The' word is used {the} times in the text")
    #
    # the below logic is exactly doing this, but instead of creating a counter (variable) for each word,
    # it is storing them in a map and the map's keys are the counters for words

    word_counts_map = {}
    for word in words:
        if word in word_counts_map:
            word_counts_map[word] = word_counts_map[word] + 1
        else:
            word_counts_map[word] = 1

    return word_counts_map


# download the ebook from the project gutenberg (Leo Tolstoi's "War and Peace")
# after running the project, try with other books in the website
book_text_url = "https://www.gutenberg.org/files/2600/2600-0.txt"
book_text = download_url_as_text(book_text_url)

# extract words by splitting the text, re.sub() is a regex method of splitting into words
all_words = re.sub("[^\w]", " ",  book_text).split()

# convert all words to lowercase, so we can count all cases ("The" and "the" is the same word)
all_words = [word.lower() for word in all_words]

# count word frequencies (occurrence count)
counts = get_counts(all_words)
sorted_by_counts = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)

# extract most common words and combine the rest under "Other words"
top_words_count = 10
most_common_words = sorted_by_counts[:top_words_count]
words_rest = sorted_by_counts[::top_words_count]
most_common_words.append(("Other words", sum(wc[1] for wc in words_rest)))

# convert to donut_chart data format
# see https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36 for formatting
labels = [f"{kv[0]} ({kv[1]})" for kv in most_common_words]
counts = [kv[1] for kv in most_common_words]

charts.draw_donut(labels, counts)
