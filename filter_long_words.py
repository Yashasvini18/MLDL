lst=[]
a=int(input("How many words in list: "))
for i in range(a):
    word=input()
    lst.append(word)
def filter_long_words(list):
    n = int(input("Maximum length of string: "))
    for i in lst:
        if len(i)>n:
            print(i)
    
filter_long_words(lst)
