# This program is made in Python 3.7
def round_down(value):
    if value - int(value) <= 0.5:
        return int(value)
    else:
        return int(value + 1)


a, b = 999, 999  # Begin running the loop from the largest numbers
s = ""
stop = False
while not stop:
    t = round_down((b-a) / 2)  # Temporary variable to find the middle between a and b
    for i in range(t, -1, -1):
        # Begin running from the middle between a and b,
        # because it gives the largest multiplication
        a1 = a + i
        b1 = b - i
        s = str(a1 * b1)  # Save the multiplication as a string
        if s == s[::-1]:  # If the multiplication is a palindrome
            print("The largest palindrome for {} and {} is: {}".format(a1, b1, s))
            stop = True  # Stop running the loop
            break
    a -= 1


