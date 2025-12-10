
# Write or Read a file

myfile = open("result_scoring.txt", "r")
tmp = myfile.readlines()
print(tmp)
# read()
# readline()
# readlines()
myfile.close()

for line in tmp:
    print(line)
