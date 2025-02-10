string = "Hello, World!"
ans=0
for i in range(len(string)):
    if string[i] in ['a','e','i','o','u']:
        ans+=1
print(ans)