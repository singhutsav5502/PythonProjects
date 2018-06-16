count=0
a=[]
while True:
    x = input("Enter Array Element:")
    if x == "done":
        break
    a.append(x)
   
for i in a:
    count += 1
print(count)
