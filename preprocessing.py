
#LIBRARIES
import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from matplotlib import pyplot


#PRE-PROCESSING DATASET #1

#READING IN THE DATA FILES
file_names = ['2014_Registered_Foreclosure_Properties.csv', '2015_Registered_Foreclosure_Properties.csv',
               '2016_Registered_Foreclosure_Properties.csv', '2017_Registered_Foreclosure_Properties.csv',
               '2018_Registered_Foreclosure_Properties.csv', '2019_Registered_Foreclosure_Properties.csv']

column_names = ['APN','Registered Date','Property Type','Property Address', 'Property City',
               'Property State', 'Property Zip', 'Council District', 'Lender', 'Lender Contact'
                'Lender Contact Phone', 'Property Management', 'Property Management Contact', 'Property Management Address',
               'Property Mgmt Contact Phone']

dataset = {}
final = None
for file in file_names:
    
    temp = []
    yearly = []
    
    data_df = pd.read_csv(file)

    temp.append(data_df)
    final = pd.concat(temp, axis=0, ignore_index=True)
 
    yearly = pd.concat(temp,axis=0, ignore_index=True)
    dataset[file[:4]] = yearly
    
print(final.head())

#CHARACTERISTICS OF THE DATA

#DROP COLUMNS NOT IMPORTANT TO THIS STUDY
final.drop(['Council District','Lender', 'Lender Contact', 'Lender Contact Phone', 'Property Management', 'Property Management Contact',  'Property Management Address', 'Property Management Contact Phone'], axis=1, inplace=True)
print(final.head())

print('DATA TYPES FOR VARIABLES IN DATASET:', '\n')
final.info()



#DATA VISUALIZATION
#How many property types do we have per year
year = {}

for k,v in dataset.items():
    counter  = {}
    tracker = 0
    for item in v['Property Type']:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item]+= 1
        tracker = tracker + 1
    year[k]= tracker
    print("Propery Type Count In", k)
    print(counter, '\n')
   
print("Total Foreclosed Property Count Per Year")
print(year)

#2014 -- 7599
#2015 -- 8255
#2016 -- 7638
#2017 -- 1754
#2018 -- 3112
#2019 -- 3317


#Plotting property foreclosure count per year
x1 = ['2014', '2015', '2016', '2017', '2018', '2019']
y1 = [1254, 1236, 1123, 247, 447, 459]
y2 = [6272, 5936, 6411, 1479, 2511, 2781]
y3 = [17, 21, 32, 19, 29, 45]
y4 = [56, 62, 72, 9, 25, 33]

  
# Plotting the Data
plt.plot(x1, y1, label='Multi-Family')
plt.plot(x1, y2, label='Single Family')
plt.plot(x1, y3, label='Vacant Residential')
plt.plot(x1, y4, label='Non-Residential')

plt.xlabel('Year')
plt.ylabel('Total Count')
plt.title("Foreclosures Based on Property Type")
  
plt.plot(y1, 'o:g', linestyle='--', linewidth='1')
plt.plot(y2, 'o:b', linestyle='--', linewidth='1')
plt.plot(y3, 'o:y', linestyle='--', linewidth='1')
plt.plot(y4, 'o:r', linestyle='--', linewidth='1')
  
plt.legend()


#Counting the most frequent foreclosed properties per year
print('\n')
print('Top Zip Codes Experiencing Foreclosure')
for k,v in dataset.items():
    counter  = {}
    for item in v['Property Zip']:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item]+= 1
    
    counter = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1])}
    
    els = list(counter.items())
    last_zip = (els[-10:])       
    
    back = dict(last_zip)
    
    print('Zip Codes experencing highest foreclosure rates in Los Angeles in', k)
    print(back, '\n')


#Plotting zipcode freuqency
x1 = ['2014', '2015', '2016', '2017', '2018', '2019']

#91344
y1 = [169, 191, 209, 56, 95, 86]
#91335
y2 = [169, 165, 167, 45, 91, 88]
#90019
y3 = [207, 163, 0, 0, 0, 0]
#90043
y4 = [207, 193, 183, 0, 75, 87]
#90011
y5 = [225, 202, 176, 37, 69, 0]
#91331
y6 = [231, 274, 225, 60, 101, 124]
#90003
y7 = [225, 218, 196, 0, 69, 73]
#91342
y8 = [245, 287, 261, 62, 112, 121]
#90044
y9 = [266, 264, 263, 58, 106, 95]
#90047
y10 = [231, 254, 245, 53, 97, 105]



# Plotting the Data
plt.plot(x1, y1, label='91344')
plt.plot(x1, y2, label='91335')
plt.plot(x1, y3, label='90019')
plt.plot(x1, y4, label='90043')
plt.plot(x1, y5, label='90011')
plt.plot(x1, y6, label='91331')
plt.plot(x1, y7, label='90003')
plt.plot(x1, y8, label='91342')
plt.plot(x1, y9, label='90044')
plt.plot(x1, y10, label='90047')


plt.xlabel('Year')
plt.ylabel('Total Count')
plt.title("Foreclosures Based on Zip Code")
  
plt.plot(y1, 'o:g', linestyle='--', linewidth='1')
plt.plot(y2, 'o:b', linestyle='--', linewidth='1')
plt.plot(y3, 'o:y', linestyle='--', linewidth='1')
plt.plot(y4, 'o:r', linestyle='--', linewidth='1')
plt.plot(y5, 'o:r', linestyle='--', linewidth='1')
plt.plot(y6, 'o:r', linestyle='--', linewidth='1')
plt.plot(y7, 'o:r', linestyle='--', linewidth='1')
plt.plot(y8, 'o:r', linestyle='--', linewidth='1')
plt.plot(y9, 'o:r', linestyle='--', linewidth='1')
plt.plot(y10, 'o:r', linestyle='--', linewidth='1')

plt.legend()

final.to_csv('foreclosed.csv')

#PRE-PROCESSING DATASET #2

headerList = ['DR_NO', 'Date Rptd', 'DATE OCC', 'TIME OCC', 'AREA', 'AREA NAME', 'Rpt Dist No', 'Part 1-2','Crm Cd', 'Crm Cd Desc', 'Mocodes', 'Vict Age', 'Vict Sex', 'Vict Descent', 'Premis Cd', 'Premis Desc', 'Weapon Used Cd', 'Weapon Desc','Status', 'Status Desc','Crm Cd 1', 'Crm Cd 2','Crm Cd 3','Crm Cd 4','LOCATION', 'Cross Street','LAT','LON']

with open('Crime_Data_from_2010_to_2019.csv', 'r', encoding='utf-8') as inp, open('first_edit.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(headerList)

    for row in csv.reader(inp):
        row_to_str = str(row[2])
        if "2014" in row_to_str:
            writer.writerow(row)
        elif "2015" in row_to_str:
            writer.writerow(row)
        elif "2016" in row_to_str:
            writer.writerow(row)
        elif "2017" in row_to_str:
            writer.writerow(row)
        elif "2018" in row_to_str:
            writer.writerow(row)
        elif "2019" in row_to_str:
            writer.writerow(row)



#Read in the file
dataset2_df = pd.read_csv('first_edit.csv')


#Dropping Columns that aren't important for this study
dataset2_df.drop(['Part 1-2', 'Date Rptd',  'TIME OCC', 'Vict Age', 'Vict Sex', 'Vict Descent', 'Status', 'Status Desc', 'Weapon Desc', 'Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4', 'Mocodes'], axis=1, inplace=True)
print('DATA TYPES FOR VARIABLES IN DATASET:', '\n')
#dataset2_df.info()
#print(dataset2_df.head())

#DATA VISUALIZATION
#Crime rates per year

year_count = dict.fromkeys(['2014', '2015', '2016', '2017', '2018', '2019'], 0)
for date in dataset2_df['DATE OCC']:
    hold = str(date)
    if "2014" in hold:
        year_count["2014"] += 1
    elif "2015" in hold:
        year_count["2015"] += 1
    elif "2016" in hold:
        year_count["2016"] += 1
    elif "2017" in hold:
        year_count["2017"] += 1
    elif "2018" in hold:
        year_count["2018"] += 1
    elif "2019" in hold:
        year_count["2019"] += 1

#print(year_count)


#sampling the dataset
lines = []
count_2014 = 0
count_2015 = 0
count_2016 = 0
count_2017 = 0
count_2018 = 0
count_2019 = 0

for item, row in dataset2_df.iterrows():
    date = str(row['DATE OCC'])
    if "2014" in date and count_2014 != 2000:
        lines.append(row)
        count_2014 += 1

    elif "2015" in date and count_2015 != 2000:
        lines.append(row)
        count_2015 += 1

    elif "2016" in date and count_2016 != 2000:
        lines.append(row)
        count_2016 += 1

    elif "2017" in date and count_2017 != 2000:
        lines.append(row)
        count_2017 += 1

    elif "2018" in date and count_2018 != 2000:
        lines.append(row)
        count_2018 += 1
    
    elif "2019" in date and count_2019 != 2000:
        lines.append(row)
        count_2019 += 1

df = pd.DataFrame (lines, columns = dataset2_df.columns)

df.to_csv('crime_data2.csv')
#dataset2_df.to_csv('crime_data.csv')


#Visualization of crime rates



#Crime rates per zip code



#Crime rates based on premise description


