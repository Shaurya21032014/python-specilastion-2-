file1 = open('codingal.txt', 'r')
file2 = open('codingal2.txt', 'w')

# reading each line from oringal
# text file 
for line in file1.readlines():

    # reading all lines that do not 
    # 2begin with coding 
    if not (line.startswith('coding')):

        # printing those lines 
        print(line)

        # storing only those lines that
        # do not begin with "Coding"
        file2.write(line)


# close and save the file s
file2.close()
file1.close()


