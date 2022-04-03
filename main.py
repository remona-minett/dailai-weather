import os
import math
import random
from random import seed
from datetime import datetime

wt = ["sunny", "partly cloudy", "cloudy", "light snow", "snow", "heavy snow"] # weather types
lt = ["bright", "moody", "dim", "dark", "pitchblack"] # light types
st = ["summer", "fall", "winter", "spring"] # season types349
stdmonths = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
# dlimonths = [] # dailai months
srv = ["aurora", "persephone"]
year = [442, 643] # amount to be added to the current year, to show the correct date
tu = "" # temperature unit - as it is evaluated to lower later, it needs to be initialized rather than None.
sc = "" # server choice - affects what year is shown
cd = datetime.now().day # current dmy for weather times
cm = datetime.now().month
cy = datetime.now().year
temp_scale = 100
temp_offset_x = -14
temp_offset_y = -20
i = 0
tl = [] # temp list init
wl = [] # weather list init
ll = [] # light list init

os.system('cls||clear')

print(f"Dailai Weather Forecast Generator") # version 1.0.0

rs = input("Enter a seed: ")
if rs == "": 
    rs = random() # if you don't enter a seed, it'll create one for you.
seed(rs) # set the seed for future use



while tu.lower() not in {'f', 'c'}:
    tu = input("Select a temperature unit, F or C: ")
tu = tu.lower() # make it lowercase so that it doesn't need to be evaluated as to lower anymore

while sc.lower() not in {'a', 'p', 'aurora', 'persephone'}: # affects what year is shown
    sc = input("Select a server, Persephone or Aurora: ")
if sc.lower() == 'persephone' or 'p': 
    cy = cy + 643
else:
    cy = cy + 442

while i < 7: # assigning a var in a list to each day's temperature
    temp_random = random.randint(-5, 5)
    current_temperature = temp_scale*(math.sin((temp_offset_x+(cm*math.pi))/6)/math.pi)+temp_offset_y+temp_random # generate temperature scale
    if tu == 'c':
        var = (current_temperature - 32) * 5.0 / 9.0 # f -> c conversion
    else: var = (current_temperature)
    var = math.trunc(var) # remove the decimals
    tl.append(var)
    i += 1

i = 0
while i < 7: # assigning a var in a list to each day's weather
    var = (random.choice(wt))
    wl.append(var)
    i += 1

print(f"{cd} {cm} {cy}") # debugging stuff
print(f"{tl}")
print(f"{wl}")