#  the sorted function takes a sequence as an argument and returns a
#  sorted list
#  my_list = [17, 4, 26, 2]
#  #  must use an assignment to function. without assigning to a variable  #  #  the function won't work
#  my_list2 = sorted(my_list)
#  print("Sorted list: ", my_list2)
#
#  my_tuple = (17, 4, 26, 2)
#  #  even though a tuple is passed as an argument a list is produced
#  result = sorted(my_tuple)
#  print("Elements of tuple sorted: ", result)

#  sort characters in a string
course = "CSC121"
result = sorted(course)
print("Characters sorted: ", result)

pairs = [(23, "Jordan"), (8, "Bryant"), (33, "Bird")]
pairs2 = sorted(pairs, key=lambda item: item[0])
print(pairs2)
