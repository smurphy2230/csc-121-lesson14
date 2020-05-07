#  write a program to find the largest value of a sequence of random    #  numbers.  A function n_random is defined and used to generate the    #  sequence, and the built-in function max is used to find the largest one
import random


def n_random(n):
    random_list = []
    for i in range(n):
        num = random.randint(1, 1000000000)
        random_list.append(num)
    return random_list


n = int(input("How many random integers do you want?  "))
max_n_random = max(n_random(n))
print(n, "random integers are generated")
print("The largest one is : ", max_n_random)

#  the above code creates a list of 50,000 items. Using a generator
#  eliminates the list, increasing performance and using fewer resources


def m_random(m):
    for i in range(m):
        num = random.randint(1, 1000000000)
        yield num


m = int(input("How many random integers do you want this time? "))
max_m_random = max(m_random(m))
print(m, "random integers are generated")
print("The largest one is: ", max_m_random)
