import urllib.request as url

def importFile(filename):
    infile = open(filename, 'r')
    contents = []
    for line in infile.readlines():
        contents.append(line)
    return contents


def readLink(url_link):
    req = url.Request(url_link)
    f = url.urlopen(req)
    myfile = f.read()
    return myfile

    
if __name__ == "__main__":
    print(readLink("https://adventofcode.com/2020/day/5/input"))
    
    