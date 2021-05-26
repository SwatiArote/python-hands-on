file = open("/Users/san6685/PycharmProjects/python-courea-sessions/demo-file.txt","r") #path and mode of file r/w
print(file.name)
print(file.mode)
file.close()

with open("/Users/san6685/PycharmProjects/python-courea-sessions/demo-file.txt","r") as file1:
    content = file1.read(10)
    print(f"file1.read() :{content}")
    # will not result as file aledry read
    content1 = file1.readline()
    print(f"file1.readline() :{content1}")

    content2 = file1.readlines() #to save the text file to a list
    print(f"file1.readlines(0) :{content2[0]}")

print(file1.close())
print(content)

# notes:
# We can also pass an argument to  readline()  to specify the number of charecters we want to read.
# However, unlike  read(),  readline() can only read one line at most.
# We can use the method readlines() to save the text file to a list
# with with automaticaly close the file after operation

# r+ : Reading and writing. Cannot truncate the file.
# w+ : Writing and reading. Truncates the file.
# a+ : Appending and Reading. Creates a new file, if none exists.
# You dont have to dwell on the specifics of each mode for this lab.
# .tell() - returns the current position in bytes
# .seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'.
# From can take the value of 0,1,2 corresponding to beginning, relative to current position and end

#file writing
with open("/Users/san6685/PycharmProjects/python-courea-sessions/demo-file2.txt","w") as file2:
    file2.write("this is demo file for writing \n please wrote here")

#copy file conetent to other content
with open("/Users/san6685/PycharmProjects/python-courea-sessions/demo-file.txt","r") as file1:
    with open("/Users/san6685/PycharmProjects/python-courea-sessions/demo-file3.txt", "w") as file3:
        for line in file1:
            file3.write(line)

with open('/Users/san6685/PycharmProjects/python-courea-sessions/demo-file3.txt"', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))

    data = testwritefile.read()
    if (not data):  # empty strings return false in python
        print('Read nothing')
    else:
        print(testwritefile.read())

    testwritefile.seek(0, 0)  # move 0 bytes from beginning.

    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data):
        print('Read nothing')
    else:
        print(data)

    print("Location after read: {}".format(testwritefile.tell()))

#We can write to files without losing any of the existing data as follows by setting the mode argument to append a.

# with open("/Users/san6685/PycharmProjects/python-courea-sessions/demo-file3.txt","a") as modifedfile:
#      modifedfile.write("this is text added in append mpde")

