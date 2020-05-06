#  zip function takes a group of sequences as arguments and aggregates
#  them. Elements that have the same index are combined to form tuples

#  jersey_list = [23, 8, 33]
#  player_list = ["Jordan", "Bryant", "Bird"]
#  z_list = list(zip(jersey_list, player_list))
#  print(z_list)

#  jersey_list = [23, 8, 33]
#  player_list = ["Jordan", "Bryant", "Bird"]
#  team_list = ["Bulls", "Lakers", "Celtics"]
#  z_list = list(zip(jersey_list, player_list, team_list))
#  print(z_list)

#  the shortest sequence passed into the zip function determines the
#  number of tuples created
#  jersey_list = [23, 8, 33]
#  player_list = ["Jordan", "Bryant", "Bird"]
#  team_list = ["Bulls", "Lakers"]
#  z_list = list(zip(jersey_list, player_list, team_list))
#  print(z_list)

#  using zip in dictionary comprehension
#  jersey_list = [23, 8, 33]
#  player_list = ["Jordan", "Bryant", "Bird"]
#  my_dict = {jersey: player for (jersey, player)
#             in zip(jersey_list, player_list)}
#  print(my_dict)

# use * in conjunction with zip to unzip a zipped list
jersey_list = [23, 8, 33]
player_list = ["Jordan", "Bryant", "Bird"]
z_list = list(zip(jersey_list, player_list))
print(z_list)
x, y = zip(*z_list)
print("Jersey numbers: ", list(x))
print("Players: ", list(y))
