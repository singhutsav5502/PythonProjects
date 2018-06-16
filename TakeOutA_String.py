data = "From someone@ukz.sdsf.sgs to me afsf yay LOL! i am going bonkers xD"
atPOS = data.find("@")
spPOS = data.find(" ",atPOS)
finalSTR= data[atPOS+1:spPOS]
print(finalSTR)

#replace , find , lower , upper , lstrip , rstrip , strip , startswith , capitalize
#x = 'From marquard@uct.ac.za'
#print(x[8])
#x = 'From marquard@uct.ac.za'
#print(x[14:17])
