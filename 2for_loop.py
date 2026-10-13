for x in "programmer":
    #print(x,end='')
    print(x)
    
    
print("\n")
sentence="this is a very long and meaningless sentence"
print(sentence)
count=0
for i in sentence:
    if(i=='e'):
        count+=1
print(f"\n\nthere are {count} letter 'e' in the sentence\n\n")

begin=5
finish=20
step=2
for j in range(begin,finish,step):#这句相当于C语言的 for(i = 5;i < 20,i += 2)
    print(f"{j} ",end='')
    
    
print("\n\n")

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i} = {j*i}\t",end='')
    print()#这里print()自动换行，要是写print("\n")会换两次行