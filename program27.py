n = input("Enter a text of numbers : ")
list = n.split()
sum = 0
for num in list:
    sum = sum + int(num)
print(sum)

numofWords = 0
numofLetters = 0
numofDigits = 0

text = input("Enter a text of numbers : ")
for s in text:
    s = s.lower()
    if s >= 'a' and s <= 'z':
        numofLetters = numofLetters + 1
    elif s >= '0' and s <= '9':
        numofDigits = numofDigits + 1
    elif s == " " :
        numofWords = numofWords + 1
print("Number of letters : ",numofLetters)
print("Number of digits : ",numofDigits)
print("Number of words : ",numofWords)
