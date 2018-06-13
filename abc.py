#Trying To Push
xyz=open("C:\\Users\lenovo\Desktop\mypython\\mail.txt", "r")

for line in xyz:
    
    if(line.startswith('Subject:')):
        abc=line.split(':')
        print(abc[1])
        #for i in abc:
        #print(i)
    
    #for word in words:
        #if(word=='Subject:'):
       #print(line)
    
