a = "Hello"
b = "world"
c = a + " " + b + "!"  # "Hello world!"
print(a)
print(b)
print(c)

print(c[1:7])  # print the 2nd through 7th characters (indicies 1-5) "ello w"
print(c[:5])  # print from the beginning of c to the 5th character (indicies 0-4) "Hello"
print(c[-6:])  # print from the 6th to last character to the end of c (indicies 7-12) "world!"
print(c[::2])  # print every other letter from c (indicies 0,2,4,6,8,10,12) "Hlowrd"

c = c.replace("l", "x")  # change all the "l"s to "x"s
print(c)
c = c.upper()  # convert the string to uppercase
print(c)

longstring = """
this
is
on
many
lines
"""
print(longstring)
input("Press enter to close")