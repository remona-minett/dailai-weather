import os
from random import random
from random import seed

wt = ["sunny", "partly cloudy", "cloudy", "light snow", "snow", "heavy snow"] # weather types
lt = ["bright", "moody", "dim", "dark", "pitchblack"] # light types
st = ["summer", "fall", "winter", "spring"] # season types
tf = [37, -42] # temperature max and min in fahrenheit for all seasons
tc = [3, -41] # temperature max and min in celcius for all seasons
tfsu = [37, 16] # temperature max and min in fahrenheit for summer
tcsu = [] # temperature max and min in celcius for summer
tff = [] # temperature max and min in fahrenheit for fall
tcf = [] # temperature max and min in celcius for fall
tfw = [] # temperature max and min in fahrenheit for winter
tcw = [] # temperature max and min in celcius for winter
tfsp = [] # temperature max and min in fahrenheit for spring
tcsp = [] # temperature max and min in celcius for spring
stdmonths = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
# dlimonths = [] # dailai months
srv = ["aurora", "persephone"]
year = [442, 643] # amount to be added to the current year, to show the correct date
tu = "" # temperature unit - as it is evaluated to lower later, it needs to be initialized rather than None.

os.system('cls||clear')

print(f"Dailai Weather Forecast Generator") # version 1.0.0

rs = input("Enter a seed: ") # seed the generator so you can bring up the same results if you need to regenerate it.
if rs == "": 
    rs = random() # if you don't enter a seed, it'll create one for you.
seed(rs) # set the seed for future use

while tu.lower() not in {'f', 'c'}: # loops you until you declare what temperature variable you want
    tu = input("Select a temperature unit, F or C: ")
tu = tu.lower() # make it lowercase so that it doesn't need to be evaluated as to lower anymore



print(rs)
print(f"EOF")