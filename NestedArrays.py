A=["1","[2,2.5]","3","4"]
x= " "
for i in range(len(A)):
    if A[i].startswith("[") and A[i].endswith("]"):
        print("found a list in the list on element:",i)
        internalList=A[i]
        for j in internalList:
            print('elements are:',j)
        '''x=A[i].replace("["," ")
        x=x.replace("]"," ")
        x= x.replace(","," ")
        x = x.strip()
        print(x)'''

    else:
        print("found a normal element")
