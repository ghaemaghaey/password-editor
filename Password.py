import re

input1 = input('enter what are you want to change in your text file')
input2 = input ('enter what are you want to change in your text file')
#open input and output file
a = open("input.txt","r")
v = open ('output.txt','w')
for word in a:
    reader = a.readline()
    writer1 = v.write(re.sub(input1,input2,word))
    writer = v.write(re.sub(input1,input2,reader))#write input text in output with changes
a.close()
v.close()
a = open('input.txt','w')
v = open('output.txt','r')
for cp in v:
    readercp = v.readline()
    writercp = a.write(cp)
    writecp2 = a.write(readercp)
a.close()
v.close()
a = open('output.txt','w')
v = open('input.txt','r')
for delete in v:
    reader= v.readline()
    writer1 = a.write(re.sub('.*','',delete))
    writer2 = a.write(re.sub('.*','',reader))
