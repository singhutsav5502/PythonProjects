A=[]
x= " "
while True:
    z = str(input("Element: "))
    if z == "Done":
        break
    A.append(z)
for i in range(len(A)):
    if A[i].startswith("[") and A[i].endswith("]"): #checking if the element is an array using a string method
        print("found a list in the list on element:",i) 
        internalList=A[i]
        internalList=internalList[1:-1]
        internalList=list(map(float,internalList.split(',')))

        for j in internalList: # print individual elements of the array 
            print('elements are:',j) 
        '''x=A[i].replace("["," ") #A test code to strip out values from a nested array
        x=x.replace("]"," ")
        x= x.replace(","," ")
        x = x.strip()
        print(x)'''

    else:
        print("found a normal element")
