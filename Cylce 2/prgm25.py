str=input("Enter a sentence: ")
str=str.casefold()
str1=[i for i in str]
dict={}.fromkeys(str1,0)
for i in str:
    if i in dict:
        dict[i]=dict[i]+1
print(dict)
