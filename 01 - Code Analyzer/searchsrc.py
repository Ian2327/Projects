#Ian Setia
#isetia@nd.edu

import argparse

#Reads a given file and returns a list with the lines in the file
def readFile(fileName):
    f = open(fileName, 'r')
    lines = []
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        lines.append(line)
    return lines

#Scans each line in the list of lines for the #include
def countInclude(lines):
    i = 0
    for line in lines:
        if line.startswith('#include'):
            i+=1
    return i

#Counts number of :: substrings present in every line, returns sum
def countMember(lines):
    m = 0
    for line in lines:
        m+=line.count('::')
    return m

#Similar to countMember (searches for -> instead of ::) returns pointer count
def countPtr(lines):
    p = 0
    for line in lines:
        p+=line.count('->')
    return p
    
#Counts the number of 0 or 1 lined functions whose curly braces appear on their own lines
def countSimplefunc(lines):
    i = 0
    sf = 0
    insideFunc = False
    for line in lines:
        if line.startswith('{'):
            insideFunc = True
            i = 0
        elif insideFunc:
            i+=1
            if i <= 2 and line.startswith('}'):
                sf+=1
            elif i > 2:
                insideFunc = False
    
    return sf
    
#same as previous function, but also counts functions whose beginning curly brace is not necessarily on its own line
def countSimplefuncec(lines):
    i = 0
    sfec = 0
    insideFunc = False
    for line in lines:
        stripped = line.strip()
        #checks for beginning curly brace which may not be on own line
        if stripped.endswith('{') and (line[0:1].isalpha() or line.startswith('{')):  
            insideFunc = True
            i = 0
        elif insideFunc:
            i+=1
            #ensures that functions are no more than 1 line
            if i <= 2 and line.startswith('}'):
                sfec+=1
            elif i > 2:
                insideFunc = False
    return sfec
    

def main():
    parser = argparse.ArgumentParser()

    #adds argument tags to identify from command line
    parser.add_argument('fileName', type=str, help='name of file to scan')
    parser.add_argument('--include', action='store_true', help='counts number of include statements in code')
    parser.add_argument('--member', action='store_true', help='')
    parser.add_argument('--ptr', action='store_true', help='')
    parser.add_argument('--simplefunc', action='store_true', help='')
    parser.add_argument('--simplefuncec', action='store_true', help='')

    args = parser.parse_args()

    #turns the file into a list of lines
    lines = readFile(args.fileName)
    
    print("file: {}\nlines: {}".format(args.fileName, len(lines)))

    #checks for argument tags before printing wanted information
    if args.include:
        print("include: {}".format(countInclude(lines)))
    if args.member:
        print("member: {}".format(countMember(lines)))
    if args.ptr:
        print("ptr: {}".format(countPtr(lines)))
    if args.simplefunc:
        print("simplefunc: {}".format(countSimplefunc(lines)))
    if args.simplefuncec:
        print("simplefuncec: {}".format(countSimplefuncec(lines)))

    print("")

    
if __name__ == "__main__":
    main()
