a = "Harry is a good boy and Harry is 18 years old"
print(a.upper())
# Strings are immutable
# a.upper() will create an another string
print(a.lower())
str1 = "Hello !!!"
print(str1.rstrip("!")) # will remove trailing characters of string 1
print(a.replace("Harry", "Vrund"))
# will replace all occurences of string 1 to string 2
print(a.split(" "))
# it splits the string 'a' into list elements which are separated by blankspace
blogheading = "welcome TO rld"
print(blogheading.capitalize())
# It will convert only first letter of string to capital and any other capital letters to small
print(str1.center(50)) # it will leave 50 spaces while printing str1
print(len(str1))
print(len(str1.center(50))) 
print(a.count("Harry"))
print(str1.endswith("!"))

str2 = "Welcome to RLD Academy RLD Academy is best "
print(str2.endswith("to", 4, 10))
# It will check within the given set of indices if the given string ends with it or not
print(str2.find("RLD"))
# it will return first occurence of a given word
# if word does not exists then it will return -1
# print(str2.index("Jai"))
# it will return ValueError if the given substring is not found
print(a.isalnum())
# it will return True if only alphanumeric characters
# also spaces should not be present
b = "Bark12345"
print(b.isalnum())
c = "Poping"
print(c.isalpha())
# it will return true if only alphabetic characters are present
str3 = "mera naam joker"
print(str3.islower())
str4 = "MAIN HU BALWAN"
print("Checking if letters are capital or not")
print(str4.isupper())
str5 = "We wish you a merry christmas \n"
print(str5.isprintable())
# \n is an escape sequence and is not printable
str6 = "          " # using spacebar
print(str6.isspace())
str7 = "                    " # using tab
print(str7.isspace())
print("Checking title")
# it will return true when only if the first letter of every word is capital
# for example World Health Organization is title
# but To kill a mocking bird isn't a title
str8 = "To Kill A Mocking Bird"
print(str8.istitle())
str9 = "Python is my favourite language"
print(str9.startswith("Pyth"))
# return true if the Given string is first word of string
str10 = "Python is a High Level Language"
print(str10.swapcase())
# it swaps lowercase to uppercase and vice versa
str11 = "This is my first blog and welcome to my channel"
print(str11.title())
# It will convert every first letter of word into capital
# for example jai swaminarayan to Jai Swaminarayan

