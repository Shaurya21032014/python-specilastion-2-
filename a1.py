# open file and read its contents 
file  = open('codingal.txt', 'r')
print(file.read())
file.close()


#open file and read its beginning 8 charceter 
file = open('codingal.txt', 'r')
print("\n read in parts \n")
print(file.read(8))
file.close()


# append your name and age in the file 
file = open('codingal.txt', 'a')
file.write ("hi i am pengiun and i am 1 year old" \
"")
file.close()