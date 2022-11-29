
#linear regression

import numpy as np
import pandas as pd
import numpy as np

from scipy.stats.stats import pearsonr   

foreclosed_dataset = pd.read_csv("foreclosed_4.csv")
crime_dataset = pd.read_csv("crime_data.csv")

count = {}
count["2014"] = 0
count["2015"] = 0
count["2016"] = 0
count["2017"] = 0
count["2018"] = 0
count["2019"] = 0


holder = foreclosed_dataset['Registered Date']


for i in range(len(holder)):
    pos = holder[i]
    digits = pos[-2:]

    if digits == '14':
        old_str = pos[:len(pos)-2]
        new_str = old_str + "2014"
        holder[i] = new_str
    elif digits == '15':
        old_str = pos[:len(pos)-2]
        new_str = old_str + "2015"
        holder[i] = new_str
    elif digits == '16':
        old_str = pos[:len(pos)-2]
        new_str = old_str + "2016"
        holder[i] = new_str
    elif digits == '17':
        old_str = pos[:len(pos)-2]
        new_str = old_str + "2017"
        holder[i] = new_str
    elif digits == '18':
        old_str = pos[:len(pos)-2]
        new_str = old_str + "2018"
        holder[i] = new_str
    elif digits == '19':
        old_str = pos[:len(pos)-2]
        new_str = old_str + "2019"
        holder[i] = new_str
    
foreclosed_dataset["Registered Date"] = holder

for date in foreclosed_dataset['Registered Date']:

    if "2014" in date:
        count["2014"] += 1
    elif "2015" in date:
        count["2015"] += 1
    elif "2016" in date:
        count["2016"] += 1
    elif "2017" in date:
        count["2017"] += 1
    elif "2018" in date:
        count["2018"] += 1
    elif "2019" in date:
        count["2019"] += 1

print(count)


crime = {}
crime["2014"] = 0
crime["2015"] = 0
crime["2016"] = 0
crime["2017"] = 0
crime["2018"] = 0
crime["2019"] = 0


for date in crime_dataset['DATE OCC']:
    
    if "2014" in date:
        crime["2014"] += 1
    elif "2015" in date:
        crime["2015"] += 1
    elif "2016" in date:
        crime["2016"] += 1
    elif "2017" in date:
        crime["2017"] += 1
    elif "2018" in date:
        crime["2018"] += 1
    elif "2019" in date:
        crime["2019"] += 1


x = ([*count.values()])
y = ([*crime.values()])




r = pearsonr(x, y)
variance = r[0] ** 2
print(variance)
print(r)


