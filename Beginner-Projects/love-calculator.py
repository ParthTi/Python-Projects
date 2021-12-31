print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

n1 = name1.lower() # Lowering case both names
n2 = name2.lower() # Lowering case both names
n3 = n1 + n2 #Concatinating both names

#Counting the occurences of "TRUE" in both names
t = n3.count("t")
# print(t)
r = n3.count("r")
# print(r)
u = n3.count("u")
# print(u)
e = n3.count("e")
# print(e)

#Counting the occurences of "Love" in both names

l = n3.count("l")
# print(l)
o = n3.count("o")
# print(o)
v = n3.count("v")
# print(v)
e = n3.count("e")
# print(e)

#Adding the occurences in both cases to define your destiny
true_count = (t+r+u+e)
love_count = (l+o+v+e)

# print(true_count)
# print(love_count)

#Concatinating the sum of both Love and True ** Converted them to the String:

love_match = str(true_count) + str(love_count)
# print(f"Your score is {love_match}.")

## Finally calculating your detiny:
love_match_int = int(love_match)
if love_match_int < 10 or love_match_int > 90:
  print(f"Your score is {love_match}, you go together like coke and mentos.")
elif love_match_int > 40 and love_match_int < 50:
  print(f"Your score is {love_match}, you are alright together.")
else:
  print(f"Your score is {love_match}.")