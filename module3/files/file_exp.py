"""
open(file, mode="rt")
r - read, default
t - text, default
w - write, if file exist (:> file in bash) || if not exist - create file
x - create if not exist
a - append (add to end of file)
b - binary (00100101)
+ - read write
"""


"""
with open(path + filename, 'r')
as f:
    data = f.read()

откроет и автоматом закроет
"""

import json

"""
Python  JSON
dict    object
list,tuple  array
str string
int,long    number
True    true
False   false
None    null
"""

with open('1.txt', 'a') as f:
    f.write('hello')

data = [1, 2, 3]

# Write
#with open('1.json', 'w') as f:
#    json.dump(data, f)

# Read
with open('1.json', 'r') as f:
    data1 = json.load(f)
print(data == data1)
