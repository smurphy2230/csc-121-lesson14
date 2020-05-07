#  lambda function
#  def double(x): return x * 2
#
#
#  print(double(10))
#
#
#  def increment_by_n(n):
#      return lambda x: x + n
#
#
#  inc = increment_by_n(3)
#  print(inc(1))
pairs = [(23, "Jordan"), (8, "Bryant"), (33, "Bird")]
pairs.sort(key=lambda item: item[0])
print(pairs)
