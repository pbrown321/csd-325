
import json
from os import path
 
filename = 'C:\csd\csd-325\module-8\Student.json'
listObj = []
 
# Check if file exists
if path.isfile(filename) is False:
  raise Exception("File not found")
 
# Read JSON file
with open(filename) as fp:
  listObj = json.load(fp)
 
# Verify existing list
print(listObj)
print(type(listObj))

listObj.append({
  "F_Name": "Phil",
  "L_Name": "Brown",
  "Student_ID": 12,
  "Email": "phbrown@my365.bellevue.edu"
})
 
# Verify updated list
print(listObj)