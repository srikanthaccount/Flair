import os
#import pdb;pdb.set_trace()

path= "sample.yaml"
with open(path,'r') as f:
    data=f.read()
    #print(data)
    words = data.split()
    print("Words count",len(words))
    print(words)

vowels='aeiou'
count=0
with open(path,'r') as f:
    data=f.read()
    for each in data:
        if each.lower() in vowels:
            count = count+1

print(count)
path1="copy_sample"
with open(path1,'w') as f:
    f.write(str(words))
    print("Wirite Done")

    
    

    

vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
with open(path,'r') as f:
    #import pdb;pdb.set_trace()
    data=f.read()
    for each in data:
        if each.lower() in vowels:
            vowels[each.lower()]+=1

print(vowels)


with open(path,'r+') as f:
    data=f.read()
    str1=''
    for each in data:
        if each.lower() in vowels:
            str1+=each.upper()
        else:
            str1+=each
    print(len(data))
    f.seek(len(data)+1)
    f.write("\n"+str1)

#print(str1)


