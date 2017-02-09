#will contain utility functions(different from those in views)

import re
import math


def word_count(html_string):
    matching_words = re.findall(r'\w+', html_string)
    count = len(matching_words)
    return count


def reading_time(html_string):
    words = word_count(html_string)
    read_time_min = math.ceil(words/200.0)#assuming 200 words/min reading speed
    return int(read_time_min)
