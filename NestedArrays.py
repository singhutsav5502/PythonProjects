A=["1","[2,2.5]","3","4"]
x= " "
for i in range(len(A)):
    if A[i].startswith("[") and A[i].endswith("]"): #checking if the element is an array using a string method
        print("found a list in the list on element:",i) 
        internalList=A[i]
        for j in internalList: #trying to print individual elements of the array but DOESN'T work due to string type
            print('elements are:',j) 
        '''x=A[i].replace("["," ") #A test code to strip out values from a nested array
        x=x.replace("]"," ")
        x= x.replace(","," ")
        x = x.strip()
        print(x)'''

    else:
        print("found a normal element")
