input_list = ["abc","wxyz","pq"]
length = []
def return_length(list):
    for i in list:
        n=len(i)
        length.append(n)
    print(length)
return_length(input_list)
