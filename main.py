import os
import math
import random
import calendar
from datetime import datetime
from random import seed


wt = ["sunny", "partly cloudy", "cloudy", "light snow", "snow", "heavy snow"] # weather types
lt = ["bright", "moody", "dim", "dark", "pitchblack"] # light types
stdmonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
stdmonthsabbr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# dlimonths = [] # dailai months
srv = ["aurora", "persephone"]
year = [442, 643] # amount to be added to the current year, to show the correct date
tu = "" # temperature unit - as it is evaluated to lower later, it needs to be initialized rather than None.
sc = "" # server choice - affects what year is shown
cd = datetime.now().day # current dmy for weather times
cm = datetime.now().month
cy = datetime.now().year
dim = calendar.monthrange(cy, cm)[1] # days in month
temp_scale = 100
temp_offset_x = -14
temp_offset_y = -20
tl = [] # temp list init
wl = [] # weather list init
ll = [] # light list init
dl = [] # day list - next calendar days
nm = False # roll over to next month in text

os.system('cls||clear')

print(f"Dailai Weather Forecast Generator") # version 1.0.0

rs = input("Enter a seed: ")
if rs == "": 
    rs = random.random() # if you don't enter a seed, it'll create one for you.
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

i = 0
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

i = 0
while i < 7:
    var = (random.choice(lt))
    ll.append(var)
    i += 1
    
i = 0
while i < 7:
    var = cd
    dl.append(var)
    cd += 1
    if cd > dim: # don't have a 32nd day, etc.
        cd = 1
        nm = True
    i += 1
    

cm = stdmonths[cm - 1] # grab the current month
print(f"Forecast beginning {cm} {cd} {cy}")
if nm == True: # if we need to roll over to the next month also some last 6 days of december specific code
    cm = datetime.now().month + 1
    if cm == 13: # no 13th month
        cm = 1
    cm = stdmonths[cm - 1] # grab the next month
    print(f"As well as the beginning of {cm}")

dl.insert(0, 'Day:')
tl.insert(0, 'Temperature:')
wl.insert(0, 'Weather:')
ll.insert(0, 'Light Level:')

data = [dl, tl, wl, ll] # organize data for displaying in table

# first map each string to formatted string with white space 
lists = [list(map(lambda item: f'{item:<15}', inner_list)) for inner_list in data]
#then join them 
lists = [''.join(item) for item in lists]
print('\n'.join(lists))