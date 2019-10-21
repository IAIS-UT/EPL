import glob

# this section will return a list of all the files in the directory
list_of_files = glob.glob('*.properties')


# this section will read each file one by one and puts it together in a "contents"
# string and replace "=" with "," and put the file name in front of it
contents = ""
for i in range(len(list_of_files)):
    a = list_of_files[i]
    with open(a, "r" ,encoding="utf8") as my_new_file:
        for line in my_new_file:
            if line[0] == "#":
                continue
            if line == '\n':
                continue
            l = list(line.strip())
            if l.count("=") == 0:
                l.append("=")
            l.append(";")
            l.append(a)
            l.append('\n')
            for j in range(len(l)):
                if l[j] == "=":
                    l[j] = ";"
            tmp = "".join(l)
            contents = contents + tmp


# this section writes the "contents" string into a new file named "big_file"
big_file = open("big_file.txt", "w" ,encoding="utf8")
big_file.write(contents)
big_file.close()

big_file = open("big_file.txt", "r" , encoding="utf8")
print(big_file.read())


