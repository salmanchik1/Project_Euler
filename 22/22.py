try:
    f = open("p022_names.txt", "r")
except FileNotFoundError:
    print("Couldn't find the file")
    exit()
if f.mode == 'r':
    contents = f.read()
else:
    print("The file isn't open to read.")
    exit()
f.close()
names = contents[1:len(contents)-1].split('","')
names.sort()
summ = 0
for i in range(len(names)):
    s = 0
    for letter in names[i]:
        s += ord(letter) - 64
    summ += s * (i+1)
print(summ)
