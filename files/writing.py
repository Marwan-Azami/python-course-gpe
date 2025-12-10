
def read_from_file(file):
    tab = []
    file_ = open(file, "r+")
    while True:
        line = file_.readline()
        if line == '':
            break
        tab.append(int(line.strip()))
    file_.close()
    return tab


def write_tab(file, tab):
    _file = open(file, "a+")
    for v in tab:
        _file.write(str(v)+"\n")
    _file.close()


# tab = []
# db = open("database3.txt", "a+")
# #
# # db.write("Hello \n")
# # db.write("World \n")
# for line in db:
#     print(line)
#     tab.append(line)
# db.close()
# print(tab)

tab2 = [1, 2, 3]
#write_tab("scores.txt", tab2)
saved_tab = read_from_file("scores.txt")
print(saved_tab[0])