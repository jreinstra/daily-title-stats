from utils import correlation

import json

data = json.loads(open("titles.json").read())

counts = [x["count"] for x in data]
lengths = [len(x["title"]) for x in data]
words = [x["title"].count(" ") for x in data]
word_lengths = [len(x["title"])/x["title"].count(" ") for x in data]
colons = [1 if ":" in x["title"] else 0 for x in data]

with_colon = 0
with_num = 0
wo_colon = 0
wo_num = 0

for entry in data:
    if ":" in entry["title"]:
        with_colon += entry["count"]
        with_num += 1
    else:
        wo_colon += entry["count"]
        wo_num += 1

print "Correlation between length and count:", correlation(lengths, counts)
print "Correlation between num words and count:", correlation(words, counts)
print "Correlation between avg word length and count:", correlation(word_lengths, counts)
print "Correlation between colon and count:", correlation(colons, counts)

print "Avg count with colon:", with_colon / with_num
print "Avg count without colon:", wo_colon / wo_num