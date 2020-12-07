
def importFile(filename):
    infile = open(filename, 'r')
    contents = []
    for line in infile.readlines():
        contents.append(line)
    return contents



    

if __name__ == "__main__":
    pass
    