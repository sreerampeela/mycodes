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

   
