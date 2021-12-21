#finding whether a number/string is a palindrome
number = input("Enter the number: ")
number_str = str(number)
length = len(number_str)
print(length)
index = list(range(0, length, 1))
print(index)
number_str2 = str()
index2 = list(range(-1, (length+1)*-1, -1))
print(index2)
for i in index2:
    number_str2 = number_str2 + number_str[i]
print(number_str2)
if number_str == number_str2:
    print("The number", number, " is a palindrome")
else:
    print("The number is not a palindrome")

#farenheit to celsius
#int() to convert a string to integer
temp_farenheit = int(input("Enter the temperature in Farenheit: "))
temp_celsius = (5/9) * (temp_farenheit - 32)
#round() to round off the value to decimals
temp_celsius_rounded = round(temp_celsius, 1)
print("The temperature in celsius is", temp_celsius_rounded)

#Converting a text into another code (leetspeak example)
leetspeak = {"O":"0", "I":"1", "L" : "1", "Z" : "2", "R" : "2", "E" : "3", "A" : "4", "S" : "5", "G" : "6", "B" : "8", "T": "7", "P": "9"}
print(leetspeak)
keys = leetspeak.keys()
print(keys)
text_input = input("Enter the text here: ")
length = len(text_input)
print(length)
converted_text = str()
for i in range(length):
    character_original = text_input[i]
    print(character_original)
#<dict>.get(<character to replace>, <character to retain>) can be used for swapping characters based on keys in dictionary
    character_converted = leetspeak.get(character_original, character_original)
    print(character_converted)
    converted_text = converted_text + str(character_converted)

print("The converted text is: ", converted_text)

#checking whether two words are rhyming or not based on last 3 letters
word1 = input("Enter the first word: ").upper()
word2 = input("Enter the second word: ").upper()
first_3 = str()
second_3 = str()
for i in [-3, -2, -1]:
    character_1 = word1[i]
    character_2 = word2[i]
    first_3 = first_3 + character_1
    second_3 = second_3 + character_2
print(first_3, "vs", second_3)
if first_3 == second_3:
    print("The words", word1, "and", word2, "rhyme")
else:
    print("The words are not rhyming")

#counting number of characters in a string (13th prob in page 86)
protein_seq = input("Enter the protein sequence in one-letter code: ").upper()
character_query = input("Enter the amino acid to query: ").upper()
character_count = protein_seq.count(character_query)
character_percent = (character_count/len(protein_seq)) * 100
print(len(protein_seq), character_query, character_count)
print("The % of", character_query, "in", protein_seq, "is", character_percent)


#rosalind prob:conditions and loops in python village
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
range_numbers = list(range(number1, number2+1))
print(range_numbers)
odd_list = list()
index = len(range_numbers)
print(index)
for i in range(0, index, 1):
    j = range_numbers[i]
    print(j)
    if j % 2 != 0:
        odd_list.append(j)

sum = 0
index2 = len(odd_list)
for k in range(0, index2, 1):
    l = odd_list[k]
    sum = sum + int(l)
print(odd_list)
print(sum)


#rosalind: python dict prob in python village
text = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
#split the text using .split()
text_list = list(text.split())
print(text_list)
#create a set of unique words
unique_words = list(set(text_list))
print(unique_words)
index = len(unique_words)
print(index)
print(unique_words, index)
#call unique words in the text
for i in range(0, index):
    word = unique_words[i]
    count = text_list.count(word)
    print(word, " ", count)


#rosalind: extracting alternate lines in a text file
fh = open("input.txt", "r")
fo = open("output.txt", "w")
text_input = fh.readlines()
length = len(text_input)
i = range(1,length,2)
for index in i:
    line_input = text_input[index]
    if line_input=="":
        break
    else:
        fo.write(line_input)
fo.close()
fh.close()

#book problem 9: detect lines with 2 consecutive identical words
#sample text file: test.txt
fh = open("test.txt")

input_lines = fh.readlines()
length_input = len(input_lines)
index = range(0, length_input)
for i in index:
    line_input = input_lines[i]
    words_input = line_input.split()
    number_words = len(words_input)
    index1 = range(0, number_words)
    for j in index1:
        k = j + 1
        if k == max(index1):
            break
        word1 = words_input[j]
        word2 = words_input[k]
        if word1 == word2:
            print("line ", i, " has 2 same consecutive words ", word1, " and ", word2)
           
        else:
            j += 1


#TEMPERATURE CONVERSION
celcius = float(input("Enter temperature in degrees C: "))
def convert_cel_to_far(celcius):
    """convert celcius to farenheit"""
    farenheit = round(((celcius*9)/5) + 32, 2)
    return farenheit
farenheit = convert_cel_to_far(celcius)
print(f"{celcius} degrees C = {farenheit} degrees F")

#checking for even or odd numbers - while + function
num = int(input("Enter the number: "))
def even_or_odd(num):
    y = num % 2
    while y == 0:
        return f"The number {num} is even"
    return f"The number {num} is not even"
y = even_or_odd(num)
print(y)

#doubling a number function and looping the function
x = int(input("Enter the number: "))

def doubles(x):
    """Doubles a given number"""
    y = x * 2
    return y

i = range(1, 4) # doubling three times
for a in i:
    z = doubles(x)
    print(z)
    x = z

#invest.py program in page 160 (first book)
amount = float(input("Enter the amount: "))
rate = float(input("Enter the interest rate: "))
years = int(input("Enter the number of years: "))

def invest(amount, rate, years):
    interest = round((amount * rate)/100, 2)
    value = amount + interest
    return value

index = range(1, years+1)
for i in index:
    final = invest(amount, rate, years)
    print(f"year {i}: ${final}")
    amount = final

#quit a loop when user enters q or Q
# while true statement at the beginning will create an infinite loop
while True:
    user_input = input('Type "q" or "Q" to quit: ')
    if user_input.upper() == "Q":
        break

#check if any four points are vertices of a square or not
##logic: all 4 sides equal and diagonals equal
points = ["1.6,0.7", "0.8,3.3", "4.5,13.2", "3.6,9.5", "-2,1.6", "8.5,16.2", "6,0.7", "10.7,-0.5", "11.1,2.2", "7.5,9.2",
         "10.25,4.75", "6.08,4.02", "10.5,15.3", "10.1,-5", "20,5", "20.8,15.75", "11.5,12.2", "14,6", "10,2", "14,2.5"]

def dist(a,b,c,d):
    """find distances with coordinates a,b and c,d"""
    distance = (((c-a)**2) + ((d-b)**2))**0.5
    return distance

distances = list()
squares = list()
length = len(points)
for i in range(0,length):
    coordinate1 = points[i].split(",")
    for j in range(0, length):
        if j!= i:
            coordinate2 = points[j].split(",")
            for k in range(0, length):
                if k != i and k != j:
                    coordinate3 = points[k].split(",")
                    for l in range(0, length):
                        if l != i and l != j and l != k:
                            coordinate4 = points[l].split(",")
                            x1 = float(coordinate1[0])
                            y1 = float(coordinate1[1])
                            x2 = float(coordinate2[0])
                            y2 = float(coordinate2[1])
                            x3 = float(coordinate3[0])
                            y3 = float(coordinate3[1])
                            x4 = float(coordinate4[0])
                            y4 = float(coordinate4[1])
                            ab = dist(x1,y1,x2,y2)
                            bc = dist(x2,y2,x3,y3)
                            cd = dist(x3,y3,x4,y4)
                            ad = dist(x4,y4,x1,y1)
                            ac = dist(x1,y1,x3,y3)
                            bd = dist(x2,y2,x4,y4)
                            if ab == bc == cd == ad and ac == bd:
                              squares.append(coordinate1)
                              squares.append(coordinate2)
                              squares.append(coordinate3)
                              squares.append(coordinate4)
                              squares.append(";")
            continue
print(squares)

#8.7: prob 1 in realpython book
while True:
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Try again")
        continue
    print(number)

#coin flipping
def toss(flip):
    """output the result of a random toss event"""
    import random as rd
    flip = rd.randint(0,1)
    if flip == 0:
        return "Heads"
    else:
        return "Tails"
heads = 0
tails = 0
for i in range(0,1000000):
    result = toss(i)
    if result == "Heads":
        heads += 1
    else:
        tails += 1
print(heads/tails)

#list comprehension
text = "eggs, fruit, orange juice"
breakfast = text.split(",")
print(type(breakfast))
lengths = [len(a) for a in breakfast] #list comprehension by using for statement
print(lengths)

#double index notation - to access lists within a lists; indexing starts from "0"
a = [[21,32],[4,10]]
element = a[1][1] #returns 2nd element of 2nd list in the nested list "a"

#always use slice notation to copy a list to another list; THIS DOESNT WORK FOR REPLACING AN ELEMENT IN THE LIST
list1 = [1,2,3,4,5]
list2 = list1[:] #copies all elements of list1 into list2
list2.append(10) #or else both list1 and list2 get appended with new value here
list2[2]=6 #at index 2, in both list1 and list2 the element is changed to "6" ("SHALLOW COPYING"). Use deep copying to prevent this
#deep copying can be done using deepcopy() in "copy" module
list2 = copy.deepcopy(list1) #copies all elements into a new list via deep copying

#sorting a list
num = [1,3,5,4,2]
num_copy = num[:] #shallow copying
print(num_copy)
num_copy.sort() #sorts values and saves in original list "num_copy"
print(num_copy) #output - sorted list
z = sorted(num_copy) #sorts values and saves in a new list "z"
print(z)

#challenge 9.4 in real python bool - list of lists
universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]
def enrollment_stats(name, noStudents, tutionFee):
    return list(noStudents, tutionFee)
def mean_new(variable_list):
    n = len(variable_list)
    sum = 0
    for i in range(0, n):
        sum += variable_list[i]
    return float(sum/n)
def median_new(variable_list):
    n = len(variable_list)
    x = sorted(variable_list)
    if n % 2 != 0:
        index = round((n+1)/2)
        median = x[index]
    else:
        index = n/2
        median = x[index]
    return median

univ = list()
fee = list()
students = list()
number = len(universities)
for i in range(0, number):
    univ.append(universities[i][0])
    fee.append(universities[i][2])
    students.append(universities[i][1])
print(univ)
print(students)
print(fee)

mean_students = mean_new(students)
mean_fee = mean_new(fee)
sum_students = sum(students)
sum_fee = sum(fee)

median_students = median_new(students)
median_fee = median_new(fee)

print("*******************************************************")
print(f"Total students: {sum_students:,}") #"," here prints "," after every 1000th value
print(f"Total tuition: $ {sum_fee:,}")
print(f"Student mean: {round(mean_students, 2):,}") # {mean_students:,2f} also rounds off to 2 decimals and "," after every 1000th value
print(f"Student median: {median_students:,}")
print(f"Tuition mean: $ {round(mean_fee, 2):,}")
print(f"Tuition median: $ {median_fee:,}")
print("******************************************************")

# challenge 9.5 real python book - wax poetic
nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango",
"extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows",
"explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant",
"exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon",
"for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly",
"furiously", "sensuously"]

def random_sel(data, iter):
    import random as rd
    value = list()
    i = 1
    while i <= iter:
        value.append(rd.choice(data))
        i += 1
    return value

def pickoverPoem(noun,verb,adjectives,prepositions,adverbs):
    nouns = random_sel(noun, 3)
    verbs = random_sel(verb, 3)
    adj = random_sel(adjectives, 3)
    prep = random_sel(prepositions, 2)
    adv = random_sel(adverbs, 1)
    text = nouns + verbs + adj + prep + adv
    print(f"The selected words are {text}")
    print (f"A {text[6]} {text[0]}", sep = '\n')
    print(f"A {text[6]} {text[0]} {text[3]} {text[9]} the {text[7]} {text[1]}", sep = '\n')
    print(f"{text[11]}, the {text[1]} {text[4]}", sep = '\n')
    print(f"the {text[1]} {text[5]} {text[10]} a {text[8]} {text[2]}")

pickoverPoem(nouns,verbs,adjectives,prepositions,adverbs)

#page 274 prob in real python book
capitals = {}
capitals["Enterprise"] =  'Picard'
capitals["Voyager"] = 'Janeway'
capitals["Defiant"] = 'Sisko'
print(capitals)
if ("Enterprise" in capitals) == False:
    capitals["Enterprise"] = "unknown"
if ("Discovery" in capitals) == False:
    capitals["Discovery"] = "unknown"

print(capitals)
for ship in capitals:
    print(f"The {ship} is captained by {capitals[ship]}")
del capitals["Discovery"]
print(capitals)

#9.7 challenge in real python book
capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}
import random as rd
districts = list(capitals_dict.keys())
print(districts)
district = rd.choice(districts)
while True:
    response = input(f"Enter the capital for {district}: ")

    if response.lower() == capitals_dict[district].lower():
        print("Guessed correct!")
        break
    elif response.lower() != capitals_dict[district].lower() and response.lower() != "exit":
        continue
    elif response.lower() == "exit":
        print("Goodbye")
        break


#10.4 real python challenge - farm

class Animal:
    def __init__(self, name, food, sleep, litter):
        self.name = name
        self.food = food
        self.litter = litter
        self.sleep = sleep
    def Activity(self):
        return f"{self.name} eats {food} and gives birth to {litter}"

class Cow(Animal):
    def __init__(self, name):
        self.food = "hay"
        self.sleep = "farm"
        self.litter = 1
        self.name = name

    def Activity(self):
            return f"{self.name} eats {self.food}"

class Pig(Animal):
    def __init__(self, name):
        self.name = name
        self.food = "bio"
        self.sleep = "pen"
        self.litter = 10
    def Activity(self):
        return f"{self.name} gives birth to {self.litter}"

class Hen(Animal):
    def __init__(self, name):
        self.food = "grains"
        self.sleep = "basket"
        self.litter = 12
        self.name = name
    def Activity(self):
        return f"{self.name} eats {self.food} and gives birth to {self.litter}"

animal1 = Cow("dodo")
print(animal1.Activity())


#creating package and module
#main.py - this file has the main script
#create __init__.py file in my_package folder. Add "#__init__.py" in this file
#my_package folder should be in the current directory. This folder should have all the modules

import my_package.module1 as m1
import my_package.module2 as m2
print(m1.greet("Murthy"))
print(m2.bye("Sreeram"))

#file paths exercise in realpython 12.2
import pathlib as pt
file_path = pt.Path.home() / "Desktop" / "Murthy" / "my_file.txt"
print(file_path)
print(file_path.exists())
print(file_path.parent.name)


#12.5 realpython challenge
import pathlib
path = pathlib.Path.cwd()
file_new = path / "starship.txt"
#file_new.touch()
lines = """Discovery
Enterprise
Defiant
Voyager"""
with file_new.open(mode='w') as file:
    file.write(lines)
with file_new.open(mode='r') as file2:
    line = file2.readlines()
    for n in lines:
        print(n, end = "")

with file_new.open(mode='r') as file3:
    line = file3.readlines()
    print(line)
    print(type(line))
    for ship in line:
        if ship[0] == "D":
            print(ship)


#review exercises 1-4 in realpython 12.6
import csv
numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    ]
import pathlib
#writing the csv file
file_path = pathlib.Path.home() / "Desktop" / "Murthy" / "numbers.csv"
file = file_path.open(mode='w')
writer = csv.writer(file)
writer.writerows(numbers)
file.close()
data = []
file_read = file_path.open(mode='r')
reader = csv.reader(file_read)

for num in reader:
    if num != []:
        data.append(num)
print(data)
file_read.close()


file = file_path.open(mode = 'w')
favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
    ]
writer = csv.DictWriter(file, fieldnames = ["name", "favorite_color"])
writer.writeheader()
writer.writerows(favorite_colors)
file.close()
#12.7 realpython - find highest score and the person with it

file = file_path.open(mode='r')
lines = file.readlines()
for data in lines:
    if data != "\n":
        print(data, end = "")
file.close()

file = file_path.open(mode='r')
reader = csv.DictReader(file)

for data in reader:
    print(data, end = "\n")
file.close()


#12.7 realpython - to find the highest score and the person with it
file_path = pathlib.Path.home() / "Desktop" / "Murthy" / "scores.csv"
file = file_path.open(mode = 'r')
lines = file.readlines()
scores = []
#finding maximum score
for line in lines[1:]:
    data = line.split(",")
    #print(data[1])
    score = data[1]
    scores.append(int(score))
print(scores)
file.close()
max_value = max(scores)
print(max_value)
#finding the person with max score
file1 = file_path.open(mode = 'r')
reader = csv.DictReader(file1)
print(type(reader))
dict_values = [] #has only the names and scores as a single list
for data in reader:
    for key, value in data.items():
        dict_values.append(value)
print(dict_values)
names = [] #all names here
indexes = [] #index value(s) for highest score(s)
for i in dict_values:
    if i == str(max_value):
        indexes.append(dict_values.index(i) - 1) #indexing norm
for j in indexes:
    names.append(dict_values[j]) #finding the name corresponding to an index
print(f"The highest scorers are {names} with score {max_value}")
file.close()

# script for renaming strain ids in fasta file
# run the following cmd in linux
# cat *.fasta >> sequences.fasta ##check file extension of the assembled genomes
# cat sequences.fasta | grep ">" >> seqids.txt

# navigating to a working directory from the current directory
import os
print(os.getcwd())
os.chdir('C:/Users/USER/Desktop/Murthy/spn_assemblies')
print(os.getcwd())

# get the strain names or ids from the seqids.txt file
# open a file handle
input_file = open('seqids.txt', mode='r')
lines = input_file.readlines()
# print(lines)
# print(len(lines))
ids = []
for line in lines:
    new_line = line.split()
    ind_val = new_line.index("pneumoniae") + 1
    if new_line[ind_val] != "strain":
        id1 = new_line[ind_val]
    else:
        ind_val += 1
        id1 = new_line[ind_val]
    if id1[-1] == ",":
        id1 = id1[:-1]
    ids.append(id1)
# print(ids)
print(len(ids))
input_file2 = open('seqids.txt', mode='r')
output_file = open('spn_full_assemblies_cleaned.txt', mode='w')
source_file = open('spn_full_assemblies.fasta', mode='r')
source_lines = source_file.readlines()
id_lines = input_file2.readlines()
for all_line in id_lines:
    index_val = id_lines.index(all_line)
    next_id_index = index_val + 1
    # print(all_line, index_val, next_id_index)
    if next_id_index < len(id_lines):
        ind1 = source_lines.index(all_line)
        ind2 = source_lines.index(id_lines[next_id_index])
    # print(ind1, ind2)
        id_new = ids[index_val]
        print(id_new)
        output_file.write(str(">" + id_new + "\n"))
        output_lines = source_lines[ind1+1: ind2]
        out_seq = ''.join(output_lines)
        output_file.write(out_seq)
input_file.close()
output_file.close()
source_file.close()

import os
import subprocess

os.chdir("C:/Users/USER/Downloads")
Counting DNA Nucleotides ROSALIND
file_in = open("rosalind_dna (1).txt", mode='r')
seq = file_in.readlines()
A=0
T=0
G=0
C=0
for bp in seq[0]:
    if bp == "A":
        A+=1
    elif bp == "T":
        T+=1
    elif bp == "G":
        G+=1
    elif bp == "C":
        C += 1
print(A,C,G,T)

Transcribing DNA into RNA ROSALIND
file_in = open("rosalind_rna.txt", mode='r')
seq = file_in.readlines()[0]
new_seq = seq.replace("T", "U")
print(new_seq)

rev complement ROSALIND
file_in = open("rosalind_revc (8).txt", mode='r')
seq = file_in.readlines()[0].strip()
# print(len(seq))
# rev=["None"] * len(seq)
# print(len(rev))
rev_comp = ["None"] * len(seq)
complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
rev = seq[::-1]
print(seq)
# for i in range(len(seq)):
#     print(i)
#     ind = i - len(seq) + 2
#     print(ind)
#     rev_comp[i] = complement[seq[ind]]

# reverse = ''.join(rev)
# print(reverse)
for j in range(len(rev)):
    rev_comp[j] = complement[rev[j]]
# print(rev_comp)
sequence = ''.join(rev_comp)
print(sequence)
print(len(sequence), len(seq))

Rabbits and Recurrence Relations ROSALIND
file_in = open("rosalind_fib.txt", mode='r')
data = file_in.readline().strip().split()
n = int(data[0])
k = int(data[1])
print(n,k)
# n = 5
# k = 3
result = [1, 1]
i1, i2 = result[0], result[1]
if n > 2:
    for j in range(3, n+1):
        res = result[j-2] + (result[j-3] * k)
        result.append(res)
print(result)

Computing GC ContentComputing GC Content ROSALIND
file_in = open("rosalind_gc (3).txt", mode='r')
file_out = open("result.txt", mode='w')
data = file_in.readlines()
GC_data = []
# print(len(data))
print(data)
acc_list = []
data_dict = {}
sequences = []
for k in data:
    if k[0] == ">":
        acc_list.append(k)
# print(acc_list)
for i in range(len(acc_list)-1):
    acc = acc_list[i]
    next_acc = acc_list[i+1]
    # print(acc,next_acc)
    begin = data.index(acc) + 1
    end = data.index(next_acc)
    seq = data[begin:end]
    # print(seq)
    sequence = str()
    for bp in seq:
        sequence += bp.strip()
    sequences.append(sequence)
    # print(begin,end)
    # print(sequence)
last_acc = acc_list[-1]
sequence_last = data[data.index(last_acc)+1:]
sequence_last_joined = ''.join(sequence_last)
sequences.append(sequence_last_joined)

print(sequences)
for nuc in sequences:
    # print(len(nuc))
    G = nuc.count("G")
    C = nuc.count("C")
    GC = ((G+C) / len(nuc)) * 100
    GC_data.append(GC)
    # print(GC)
    file_out.write(nuc)
    file_out.write("\n")
    file_out.write(str(GC))
    file_out.write("\n")
max_gc = max(GC_data)
max_gc_seq = acc_list[GC_data.index(max_gc)]
print(max_gc_seq[1:].strip())
print(max_gc)
file_in.close()
file_out.close()

ROSALIND Counting Point Mutations
file_in = open("rosalind_hamm.txt", mode='r')
sequence = file_in.readlines()
sequences = []
for seq in sequence:
    sequences.append(seq.rstrip())
seq1 = sequences[0]
seq2 = sequences[1]
dist = 0
for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        dist += 1
print(dist)

Mendel's First Law ROSALIND incomplete
file_in = open("rosalind_hamm.txt", mode='r')

Translation ROSALIND
codon_table = {"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V","UUC":"F","CUC":"L", "AUC" : "I", "GUC" : "V",
               "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V", "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
               "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A", "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
               "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A", "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
               "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D", "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
               "UAA" : "Stop", "CAA" : "Q", "AAA" : "K", "GAA" : "E", "UAG" : "Stop", "CAG" : "Q", "AAG" : "K",
               "GAG":"E", "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G", "UGC" : "C", "CGC" : "R", "AGC" : "S",
               "GGC" : "G", "UGA" : "Stop", "CGA" : "R", "AGA" : "R", "GGA" : "G", "UGG" : "W", "CGG" : "R",
               "AGG" : "R", "GGG" : "G"}

file_in = open("rosalind_prot.txt", mode='r')
nuc_seq = file_in.readlines()[0].rstrip()
print(nuc_seq)
aa_seq = str()
for i in range(0,len(nuc_seq),3):
    j = i + 3
    codon = nuc_seq[i:j]
    print(codon)
    aa = codon_table[codon]
    aa_seq += aa
print(aa_seq)

Finding a Motif in DNA ROSALIND
file_in = open("rosalind_subs (1).txt", mode='r')
data = file_in.readlines()
print(data)
mystring = data[0].strip()
query = data[1].strip()
print(query)
result = []
for i in range(0, (len(mystring)-len(query)-1)):
    j = i + len(query)
    print(i,j)
    print(mystring[i:j])
    if query == str(mystring[i:j]):
        result.append(i+1)
print(result)

Consensus and Profile ROSALIND
formatting error
file_in = open("rosalind_cons (3).txt", mode='r')
file_out = open("rosalind_cons_result.txt", mode='w')
data = file_in.readlines()
seq = []
A_result = ["A:"]
T_result = ["T:"]
G_result = ["G:"]
C_result = ["C:"]
acc_list = []
sequences = []
for k in data:
    if k[0] == ">":
        acc_list.append(k)
print(acc_list)
for i in range(len(acc_list)-1):
    acc = acc_list[i]
    next_acc = acc_list[i+1]
    # print(acc,next_acc)
    begin = data.index(acc) + 1
    end = data.index(next_acc)
    seq = data[begin:end]
    sequence = ''.join(a.strip() for a in seq)
    # print(sequence)
    sequences.append(sequence)
    # print(seq)
last_acc = acc_list[-1]
sequence_last = data[data.index(last_acc)+1:]
sequence_last_joined = ''.join(sequence_last)
sequences.append(sequence_last_joined)
print(sequences)
k = len(sequences)
print(k)
j = len(sequences[0])
print(j)
consensus_seq = str()
for m in range(0,j):
    seq_con = []
    for n in range(0, k):
        bp = sequences[n][m]
        # print(bp)
        seq_con.append(bp.strip())
    # print(seq)
    A_count = seq_con.count("A")
    T_count = seq_con.count("T")
    G_count = seq_con.count("G")
    C_count = seq_con.count("C")
    A_result.append(A_count)
    T_result.append(T_count)
    G_result.append(G_count)
    C_result.append(C_count)
    Counts = [A_count, T_count, G_count, C_count]
    consensus = max(Counts)
    con_ind = Counts.index(consensus)
    if con_ind == 0:
        app_bp = "A"
    elif con_ind == 1:
        app_bp = "T"
    elif con_ind == 2:
        app_bp = "G"
    elif con_ind == 3:
        app_bp = "C"
    consensus_seq += app_bp
consensus_seq += "\n"
print(consensus_seq)
# for b in "ACGT":
#     result = b + "_result"
#     print(b + ":" + " ".join(str(x) for x in result))

A_result = " ".join(str(x) for x in A_result) + '\n'
C_result = " ".join(str(x) for x in C_result) + '\n'
G_result = " ".join(str(x) for x in G_result) + '\n'
T_result = " ".join(str(x) for x in T_result) + '\n'
print(A_result.strip())
print(C_result.strip())
print(G_result.strip())
print(T_result.strip())
file_out.write(consensus_seq)
file_out.write(A_result)
file_out.write(C_result)
file_out.write(G_result)
file_out.write(T_result)

file_in.close()
file_out.close()

Mortal Fibonacci Rabbits ROSALIND incomplete
file_in = open("rosalind_fibd (1).txt", mode='r')
data = file_in.readline().strip().split()
n = int(data[0])
m = int(data[1])
print(n,m)
# n = 5
# k = 3
result = [1, 1, 2, 2, 3, 4] # 1st 6 months as base case
if n <= 6:
    print(result[n-1])
else:
    for i in range(6, n+1):
        new_ones = result[i-1] - result[i-2]
        old_ones = result[i-2] - result[i-3]
        res = new_ones - old_ones
        result.append(res)

print(result[-1])

Finding a Shared Motif ROSALIND
file_in = open("rosalind_lcsm (2).txt", mode='r')
file_out = open("result.txt", mode='w')
data = file_in.readlines()
acc_list = []
sequences = []
for k in data:
    if k[0] == ">":
        acc_list.append(k)
print(len(acc_list))
for i in range(len(acc_list)-1):
    acc = acc_list[i]
    next_acc = acc_list[i+1]
    # print(acc,next_acc)
    begin = data.index(acc) + 1
    end = data.index(next_acc)
    seq = data[begin:end]
    sequence = ''.join(a.strip() for a in seq)
    # print(sequence)
    sequences.append(sequence)
    # print(seq)
last_acc = acc_list[-1]
sequence_last = data[data.index(last_acc)+1:]
sequence_last_joined = ''.join(sequence_last)
sequences.append(sequence_last_joined)
# print(sequences)
print(len(sequences))
small_seq = min(sequences)
print("The smallest seq is ", small_seq)
sequences.remove(small_seq)
strings_list = []
for j in range(len(small_seq)):
    for k in range(-1, -len(small_seq[j:])+1, -1):
        sequence_string = small_seq[j:k]
        strings_list.append(sequence_string)
# print(strings_list)
string_list_new = sorted(strings_list, key=len, reverse=True)
print(string_list_new)
lcs = []

for l in range(-1, -len(string_list_new), -1):
    comp = string_list_new[l].rstrip()
    result = []
    for seq in sequences:
        if comp in seq:
            result.append(1)
        else:
            break
    # print(result)
    if sum(result) == len(result):
        lcs.append(comp)

# print("The longest sequences are :", lcs)
# for bp in lcs:
#     bp_new = bp + "\n"
#     file_out.write(bp_new)
#     file_out.write("\n")
# # print("The longest common substring is: ")
def substring(all_seq,all_substring):
    global x
    if all([x in all_seq for x in all_substring]):
        return x




substr = substring(sequences, string_list_new)
print(substr)
file_in.close()
file_out.close()


Open Reading Frames ROSALIND
file_in = open("rosalind_fibd.txt", mode='r')
seq = file_in.readlines()[1].strip()
codon_table = {"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V","UUC":"F","CUC":"L", "AUC" : "I", "GUC" : "V",
               "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V", "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
               "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A", "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
               "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A", "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
               "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D", "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
               "UAA" : "Stop", "CAA" : "Q", "AAA" : "K", "GAA" : "E", "UAG" : "Stop", "CAG" : "Q", "AAG" : "K",
               "GAG":"E", "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G", "UGC" : "C", "CGC" : "R", "AGC" : "S",
               "GGC" : "G", "UGA" : "Stop", "CGA" : "R", "AGA" : "R", "GGA" : "G", "UGG" : "W", "CGG" : "R",
               "AGG" : "R", "GGG" : "G"}
seq.replace("T", "U")
# print(seq)
seq_complement = seq[::-1]
print(seq_complement)

Creating a linked list
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()
    def append(self, value):
        new_node = Node(value)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.value)

        print(elements)

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list)
my_list.display()

class linked list practice
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = Node()


    def attach(self, new):
        new_node = Node(new)
        cur_node = self.head
        while cur_node.next != None:
                cur_node = cur_node.next
        cur_node.next = new_node


    def printlist(self):
        list_new = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            list_new.append(cur_node.data)
        print(list_new)


node1 = "Ram"
print(node1)
my_list = linkedlist()
my_list.attach(node1)
my_list.printlist()
node2 = "Sree"
print(node2)
my_list.attach(node2)
my_list.printlist()

problems in python DSA Goodrich
2.4
class Flower:
    def __init__(self, name, petal_no, price):
        self.name = str(name)
        self.petal_no = int(petal_no)
        self.price = float(price)

    def getdata(self, search):
        search = search.lower()
        search = search.replace(" ", "")
        if search == "name":
            return self.name
        elif search == "petalnumber":
            return self.petal_no
        else:
            return self.price


data = Flower("Daisy", 10, 10.25)
name = data.getdata("Name")
print(name)
print(data.getdata("Petal Number"))

Creating a vector class
class Vector:
    def __init__(self, x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def print_vector(self):
        return self.x, self.y, self.z

    def __iter__(self):
        return self.x, self.y, self.z

    def addvector(self, other):
        first_vector = list(self.__iter__())
        other_vector = list(other.__iter__())
        if len(first_vector) == len(other_vector):
            print(f"Adding {first_vector} and {other_vector}")
        # print(type(first_vector))
            new_vector = [0] * len(first_vector)
            for i in range(0, len(first_vector)):
                new_vector[i] = first_vector[i] + other_vector[i]
            return new_vector
        else:
            return "Vectors should be of equal dimensions"

    def subvector(self, other):
        first_vector = list(self.__iter__())
        other_vector = list(other.__iter__())
        if len(first_vector) == len(other_vector):
            print(f"Subtracting {first_vector} and {other_vector}")
            # print(type(first_vector))
            new_vector = [0] * len(first_vector)
            for i in range(0, len(first_vector)):
                new_vector[i] = first_vector[i] - other_vector[i]
            return new_vector
        else:
            return "Vectors should be of equal dimensions"


vector1 = Vector(1,0,5)
vector2 = Vector(3,0,7)
print(vector1.print_vector())
print(vector2.print_vector())
added = vector1.addvector(vector2)
print(added)
subtracted = vector1.subvector(vector2)
print(subtracted)


filter vcf csv files for removing synonymous snps
import os
import pandas as pd
print(os.getcwd())
os.chdir("C:/Users/USER/Desktop/Murthy/gpsc_project/clean-reads/SRR8879299")
# navigate to the specific folder with snippy-results
print(os.getcwd())
# # acc_list=["ERR3227767", "ERR3227769", "ERR3227771", "ERR3227773", "ERR3227775", "ERR3227779", "ERR3227781", "ERR3227783",
# #           "ERR3227784", "ERR3227834", "ERR4784547", "ERR4784551", "ERR4784605", "ERR4784667", "ERR4784676", "ERR4784684",
# #           "ERR4784688", "ERR4784692", "ERR4784696"]
# use this in loop to remove all synonymous snps in the csv file
file_in = open("SRR8879299.csv",mode='r')
file_out = open("SRR8879299_clean3.csv", mode='w')
data = file_in.readlines()
header = data[0]
vcf_data = data[1:]
data_new = [header]
j = 0
for line in vcf_data:
    # print(line)
    if "synonymous_variant" in line:  # some combos with synonymous variants seen in the file
        data_1 = list(line.split(","))  # split all columns
        if len(data_1) >= 11: # some columns have very little data
            effect = data_1[10]
            eff = effect.split(" ")  # a list with split on EFFECT column
            # print(eff)
            if eff[0] != "synonymous_variant":
                data_new += line
                j += 1
        # elif len(data_1) == 6:
        #     data_new += line
        #     j += 1
    else:
        data_new += line
        j += 1
# print(len(data_new))
for i in data_new:
    file_out.write(i)
print(j)  # number of non-synonymous mutations

to combine gff files and fna files in ncbi dataset
import os
os.chdir("C:/Users/USER/Desktop/Murthy/data")
file_in1 = open("assemblies.txt", mode='r')
file_in2 = open("gff_files.txt", mode='r')
file_out = open("output_parser.sh", mode='w')
assemblies = file_in1.readlines()
gff_files = file_in2.readlines()
# print(assemblies)
# print(gff_files)
for acc in assemblies:
    for gff in gff_files:
        acc_1 = acc.strip('\n')
        ids = gff[:15].strip('\n')
        # print(acc_1)
        # print(ids)
        if acc_1 == ids:
            # subprocess.Popen("cp", gff, acc_1)
            line = 'mv {} {}'.format(gff.strip('\n'), acc_1)
            # print(line)
            file_out.write(line)
            file_out.write("\n")

file_in1.close()
file_in2.close()
file_out.close()

# !/bin/python3

acc_list = ["ERR2090225", "ERR3227834", "ERR4784551", "ERR4784667", "ERR4784547", "ERR4784688", "ERR4784684",
            "ERR4784692", "ERR4784605", "ERR3227765", "ERR4784676", "ERR4784696", "SRR8879299", "ERR3227775",
            "ERR3227773", "ERR3227779", "ERR3227784", "ERR3227767", "ERR3227746", "SRR8879297", "SRR8879296",
            "ERR3227783", "ERR3227781", "SRR8879298", "ERR3227771"]
# strains = ["SF1916", "SF1927", "3277", "3690", "6487", "2585", "1192", "2445", "A308", "EX3714", "P276", "6800", "1453",
           "927", "SF4850", "P766", "P20011", "A2258", "A1645", "P924", "SF621", "A1917", "P776", "7484", "7861"]
out_file = open("copier.sh", mode='w')
# r1="_1_paired.cor.fq.gz"
# r2="_2_paired.cor.fq.gz"
# f1=".notCombined_1.fastq.gz"
# f2=".notCombined_2.fastq.gz"
# fl=".extendedFrags.fastq.gz"
for acc in acc_list:
    # strain = strains[acc_list.index(acc)]
    # acc_r1=acc+r1
    # acc_r2=acc+r2
    # acc_f1=acc+f1
    # acc_f2=acc+f2
    # acc_fl=acc+fl
    # acc_out=acc+"_shovill"
    acc_pr = acc + "_prokka"
    acc_prot = acc + ".faa"
    acc_prot_fasta = acc + "_prot.fasta"
    # cmd1 = "flash -m 20 -M 100 -d $PWD -o {} -z {} {}".format(acc, acc_r1, acc_r2)
    # out_file.write(cmd1)
    # out_file.write('\n')
    # cmd2 = "spades.py --pe1-1 {} --pe1-2 {} --pe1-m {} --only-assembler --isolate --tmp-dir /tmp/{} -k 21,33,43,53,63,75 --threads 6 -o {}".format(acc_f1,acc_f2,acc_fl,acc,acc_out)
    # out_file.write(cmd2)
    # out_file.write('\n')
    # cmd3 = "prokka --centre KIMS --outdir {} --genus Streptococcus --species pneumoniae --strain {} --prefix {} {}/contigs.fasta".format(acc_pr, strain, acc, acc_out)
    # out_file.write(cmd3)
    # out_file.write('\n')
    # cmd4 = "cp {}/{} files_panaroo/".format(acc_pr,acc_gff)
    # out_file.write(cmd4)
    cmd5 = "cp {}/{} protein_sequences/{}".format(acc_pr, acc_prot, acc_prot_fasta)
    out_file.write(cmd5)
    out_file.write('\n')

out_file.close()
