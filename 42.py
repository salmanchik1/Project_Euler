# Get the content from the file
try:
    f = open("42\\p042_words.txt", "r")
except FileNotFoundError:
    print("Couldn't find the file")
    exit()
# Put it into content variable and close
if f.mode == "r":
    contents = f.read()
f.close()
# delete exceeding signs and split the text and make the list
words = contents.replace('"', '').split(',')
# calculate the sums for all the words in the list
words_nums = [sum([ord(letter)-64 for letter in word.upper()]) for word in words]
# calculate the maximum in the sums
max_nums = max(words_nums)
n = 1
# making the list of triangle numbers, the maximum is defined in max_nums
triangle_nums = []
# run through "eternal" loop
while True:
    triangle_nums.append(int((1/2)*n*(n+1)))
    if triangle_nums[-1] > max_nums:
        # if the number is too big - exit from "eternal" loop
        break
    n += 1
# printing out the sum of all triangle numbers in the words_nums list
print("The sum of all the triangle numbered words in the file is:",
      sum([1 for i in words_nums if i in triangle_nums]))
