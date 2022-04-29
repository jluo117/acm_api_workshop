#create a list of all the numbers in range from 1 to 100
my_list = list(range(1,101))
print(my_list)
#2sums in O(n)
def two_sums(my_list,x):
    my_set = set()
    for i in my_list:
        if x-i in my_set:
            return True
        my_set.add(i)
    return False
        
    