from collections import Counter
from operator import itemgetter

#######################Determining the most frequently occuring items in a sequence ######################

words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]

word_counts=Counter(words)
print(word_counts)
#Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})

morewords = ['why','are','you','not','looking','in','my','eyes']

#####첫번째 방법 #####

for word in morewords:
    word_counts[word]+=1

print(word_counts)

#####두번째 방법 #####

word_counts.update(morewords)
print(word_counts)

################## Sorting a list of dictionaries by a common key ###########################

rows = [
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
 {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname=sorted(rows,key=itemgetter('fname'))
rows_by_uid=sorted(rows,key=itemgetter('uid'))
rows_by_lfname=sorted(rows,key=itemgetter('lname','fname'))

print(rows_by_fname)
print(rows_by_lfname)
print(rows_by_uid)

#itemgetter()의 기능은 lambda 표현으로 대체되기도 한다

rows_by_fname=sorted(rows,key=lambda r:r['fname'])
rows_by_fname=sorted(rows,key=lambda r:(r['lname'],r['fname']))

print(rows_by_fname)
print(rows_by_fname)

print(min(rows,key=itemgetter('uid')))
print(max(rows,key=itemgetter('uid')))

