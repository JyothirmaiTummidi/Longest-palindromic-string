a=input("Enter any string : ")
longest=""
max=0
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        sub=""
        for k in range(i,j):
            sub +=a[k]
        rev=""
        for k in range(j-1,i-1,-1):
            rev+=a[k]
            
        if sub==rev and len(sub)>max:
            longest=sub
            max=len(sub)
print(f"Longest palindromic string in the given string '{a}' is {longest}")