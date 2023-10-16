v=['a','A','e','E','i','I','o','O','u','U']
word=input("Enter the word: ")
s=[i for i in word if i in v]
print(s)