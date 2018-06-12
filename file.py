list1=[]
frequency=dict()

xyz=open('C:\\Users\lenovo\Desktop\\a1.txt', 'r')
print(xyz)

def word_count(xyz):

    for word in xyz:
        words=word.split()
        for i in words:
            if(i not in list1):
                list1.append(i)
                frequency[i]=1
            
            else:
                frequency[i]=frequency[i]+1

    return frequency       

print(word_count(xyz))
print(max(word_count(xyz)))

             
            
            
    
