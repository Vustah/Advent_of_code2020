import urllib.request as url

def importFile(filename):
    infile = open(filename, 'r')
    contents = []
    for line in infile.readlines():
        contents.append(line)
    return contents


def readLink(url_link):
    f = url.urlopen(url_link)
    myfile = f.read()
    return myfile

    
if __name__ == "__main__":
    print(readLink("https://adventofcode.com/2020/day/4/input"))
    
    