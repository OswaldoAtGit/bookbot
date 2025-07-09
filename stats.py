import re

def get_num_words(text):
    # match all non whitespace words
    return len(text.split())
    # the following gives a +1 then the above
    # len(re.split("\S+")) # count all non-whitespace 

def get_histogram(text):
    histogram = {}
    for c in text.lower():
        if c in histogram:
            histogram[c] +=1
        else:
            histogram[c] = 1
    return histogram

def get_sort_histogramlist(histo):
    sorted = []
    for kv in histo:
        sorted.append( {"char":kv, "num":histo[kv]})
    
    sorted.sort(reverse=True,key=lambda itm: itm["num"])
    return sorted
    
