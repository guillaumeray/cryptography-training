from itertools import permutations

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

list = permutations(my_list)

cnt=0
for p in list:
    cnt+=1

print(len(my_list),cnt)

"""
We can see that the time complexity grows insanely high after 11 permutations
With high number, we have to count milliard of milliard and it becomes almost impossible for a simple computer
That's why the key space is important, longer is the key, more complicated it will be for a computer to break it
"""