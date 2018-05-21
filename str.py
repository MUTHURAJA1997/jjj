b=input("enter the sentence: ")
vowels=('a','e','i','o','u')
for x in b.lower():
    if x in vowels:
        b=b.replace(x,"")
print(b[::-1])
