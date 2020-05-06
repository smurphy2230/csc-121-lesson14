#  this module is part of Python's standard library. It supplies classes
#  for manipulating dates and times.
from datetime import datetime, timedelta

#  datetime requires 3 parameters (year, month, day)
#  checkout = datetime(2019, 7, 4)
#  print("Checkout Date:")
#  print("Year: ", checkout.year)
#  print("Month: ", checkout.month)
#  print("Day: ", checkout.day)
#  print("Hour: ", checkout.hour)
#  print("Minute: ", checkout.minute)
#  print("Second: ", checkout.second)
#  print("Microsecond: ", checkout.microsecond)
#  print()

#  checkout = datetime(2019, 7, 4, 14, 2, 5, 1234)
#  print("Checkout Date:")
#  print("Year: ", checkout.year)
#  print("Month: ", checkout.month)
#  print("Day: ", checkout.day)
#  print("Hour: ", checkout.hour)
#  print("Minute: ", checkout.minute)
#  print("Second: ", checkout.second)
#  print("Microsecond: ", checkout.microsecond)
#  print()

#  checkout = datetime(2019, 7, 4, 14, 2, 5, 1234)
#  print(checkout)
#  print()
#  #  use strftime method to control output format MM-DD-YY
#  print(checkout.strftime("%m-%d-%y"))
#  print()
#  #  use Y for four digit year format YYYY/MM/DD
#  print(checkout.strftime("%Y/%m/%d"))
#  print()
#  print(checkout.strftime("%Y/%m/%d %H:%M:%S"))
#  print()
#  #  for 12 hour time:
#  print(checkout.strftime("%Y/%m/%d %I:%M:%S %p"))
#  print()

#  use strptime method to extract data from a string and create
#  datetime object strptime has two parameters, a string and format
#  str_dob = input('Enter date of birth [mm/dd/yy]: ')
#  #  %y at end of line requires 2 digit year input. %Y requires 4 digit
#  dob = datetime.strptime(str_dob, "%m/%d/%y")
#  print("Date of birth:", dob)
#  print()
#  str_dt = input("Enter date and time: [yyyy-mm-dd hh:mm:ss]: ")
#  dt = datetime.strptime(str_dt, "%Y-%m-%d %H:%M:%S")
#  print("Date time: ", dt)
#  print()

#  #  now methon of datetime class returns a datetime object that
#  #  stored current date and time
#  checkout = datetime.now()
#  print(checkout)
#  print()

#  replace method can be used to change attributes of a datetime object
#  checkout = datetime.now()
#  print("Current Time: ", checkout)
#  checkout = checkout.replace(month=5, day=24)
#  print("Happy Birthday to me!!: ", checkout)
#  print()

#  comparing two dates
#  str_due_date = input("Enter due date in yyyy-mm-dd format: ")
#  due_date = datetime.strptime(str_due_date, "%Y-%m-%d")
#
#  str_submit_date = input("Enter submission date in yyyy-mm-dd format: ")
#  submit_date = datetime.strptime(str_due_date, "%Y-%m-%d")
#
#  print("Due date:", due_date)
#  print("Submission date:", submit_date)
#
#  if submit_date <= due_date:
#      print("Assignment submitted on time")
#  else:
#      print("Assignment submitted after deadline")
#  print()

#  compare the difference between two dates
#  start_date = datetime(2017, 4, 5)
#  end_date = datetime(2017, 6, 8)
#  timespan = end_date - start_date
#  print("Timespan: ", timespan.days, " days")
#  print()
#  # compare with more accuracy
#  start_date = datetime(2017, 4, 5, 16, 2, 20)
#  end_date = datetime(2017, 4, 7, 18, 21, 14)
#  timespan = end_date - start_date
#  print("Timespan: ", timespan)
#  print()

#  use timedelta to find the difference of two dates. A timedelta
#  represents a duration

#  start_time = datetime(2019, 7, 4, 5, 16, 2, 20)
#  end_time = datetime(2019, 9, 8, 3, 16, 5, 15)
#  length = end_time - start_time
#  print("Length: ", length.days, "days")

checkout_date = datetime.now()
due_date = checkout_date + timedelta(days=14)
print("Checkout date: ", checkout_date.strftime("%m/%d/%Y"))
print("You must return the book within 14 days.")
print("Due date: ", due_date.strftime("%m/%d/%Y"))

start_time = datetime.now()
deadline = start_time + timedelta(hours=2, minutes=30)
print("Test start time: ", start_time.strftime("%I:%M:%S %p"))
print("You have 2 hours 30 minutes to complete the exam.")
print("Submit the test by: ", deadline.strftime("%I:%M:%S %p"))
