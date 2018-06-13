from collections import Counter
a=dict()
x=open('F:\\python\\a1.txt', 'r')

#def word_count(x):
words = []
for line in x:
    words = line.split()
    for word in words:
        a[word]=a.get(word, 0) + 1

print(a)
print("...............second task.........")
l = list()
for key , values in sorted(a.items(),key=lambda item:(item[1],item[0])):
    l.append((values,key))

#print(l)    
for i in range(1,10):
    print(l[-i])
#Counter = Counter(a)

        #most = Counter.most_common(10)
        #print(most)
    #return a

#print(word_count(x))
