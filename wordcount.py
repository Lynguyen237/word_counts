# put your code here.
#import pdb
from collections import Counter

# def sort_by_alphabetic():

def sort_by_value(tup):
    return tup[0]

def word_count(filename):
    count = Counter()    
    #pdb.set_trace()

    with open(filename) as text_file:
    
    #file will be closed after the for loop
        for line in text_file:
            line = line.lower().rstrip().split(' ')
            count.update(line)
        # print(count) 
        d = dict(count)
        return sorted(d.items(), key = sort_by_value)
        #     for word in line:
        #         word = word.rstrip()
        #         word = word.lower()
        #         if word.isalnum() == False:
        #             word = word[:-1]
        #             count[word] = count.get(word,0) + 1
        #         else:
        #             count[word] = count.get(word,0) + 1
        
        # sorted_count = sorted(count)
        # new_count = {}
        # for i in sorted_count:
        #     new_count[i] = count[i]
        # return new_count
        
        # return sorted(count, key = wordcount)
        # for i in (count.items()):-
        #     print (i)
    # word_count('twain.txt')

    
print(word_count('test.txt'))
# print(len(word_count('test.txt')))