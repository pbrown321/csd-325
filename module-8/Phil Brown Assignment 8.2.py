#Use the JSON load() function to load the file into a Python class list.
#Create a function that loops through the .json class list and prints out each value, should look something like:
#Ripley, Ellen : ID = 45604 , Email = eripley@gmail.com
#Output notification to the user that this is the original Student list.
#Call your print function.
#Add your last name, first name, fictional ID, and email to the class list using append().

#Output notification to the user that this is the updated Student list.
#Call your print function.
#Use the JSON dump() function to append the new data to the .json file.
#Output notification to the user that the .json file was updated.


#Import section of code modified from:
#https://oxylabs.io/blog/python-parse-json
import json

with open('student.json') as f:
  data = json.load(f)

#print(type(data)) check data type for first bullet point in assignment
def print_output():
  for item in data:
    print(f"\t{item['L_Name']}, {item['F_Name']} : ID = {item['Student_ID']}, Email : {item['Email']}")
#Ripley, Ellen : ID = 45604 , Email = eripley@gmail.com


print('This is the original student list.')
print_output()


#Append section of code modified from 
#https://howtodoinjava.com/python-json/append-json-to-file/

#import json
from os import path
 
filename = 'C:\csd\csd-325\module-8\Student.json'
listObj = []
 
# Check if file exists
if path.isfile(filename) is False:
  raise Exception("File not found")
 
# Read JSON file
with open(filename) as fp:
  data = json.load(fp)
 

data.append({
  "F_Name": "Phil",
  "L_Name": "Brown",
  "Student_ID": 12,
  "Email": "phbrown@my365.bellevue.edu"
})
 
# Verify updated list
print("This is the updated student list.")
print_output()

with open(filename, 'w') as json_file:
    json.dump(data, json_file, 
                        indent=4,  
                        separators=(',',': '))
 
print('Successfully appended to the JSON file')
