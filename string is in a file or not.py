f=open("khushi.txt","r")
str=input("ENTER THE WORD:-")
str1=f.read()
if str in str1:
    print("YES")
else:
    print("NO")
f.close()
