"""

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name 
score.

For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN 
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open(r'C:\Users\Christopher\Documents\GitHub\project-euler\p022_names.txt') as file_object:
    text = file_object.readlines()[0]
    name_list = text.replace('"', '').split(',')
    name_list.sort()

total = 0

for name in name_list:
    name_score = 0
    for letter in name:
        name_score += alphabet.index(letter) + 1
    name_score *= name_list.index(name) + 1
    total += name_score
    
print(total)