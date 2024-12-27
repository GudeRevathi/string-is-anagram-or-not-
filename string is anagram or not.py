s1=input("enter a string:").lower()
s2=input("enter a string:").lower()
str1=s1.replace(" ","")
str2=s2.replace(" ","")
t1=sorted(str1)
t2=sorted(str2)
print(t1,t2)
if t1==t2:
    print("yes")
else:
    print("no")
