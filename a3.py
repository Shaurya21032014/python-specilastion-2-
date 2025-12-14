# program to copy add line of one file to another
# open the file in read mode 
fn = open('codingal.txt', 'r')

# open the another file in write mode 
fn1 = open('codinga2.txt','w')

# read the content of the file line by line 
cont = fn.readlines()
type(cont)
for i in range(1, len(cont)+1):
 if(i % 2 != 0):
        fn1.write([cont[i - 1 ]])
else:
    pass
# close the file 
fn1.close()

# open file in read mode 
fn1 = open('codingal2.txt','r')

# read the content of the file 
cont1 = fn1.read(



)

#  print the content of the file 
print(cont1)

# close all the file 
fn.close()
fn1.close()