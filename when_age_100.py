#char input to get year when they will turn 100 
name=input("Enter your name:")
age=int(input("Enter age:"))
year=int(input("enter current year:"))
year_turn_100=year+(100-age)
print("{},you will turn 100 in the year {}".format(name,year_turn_100))
