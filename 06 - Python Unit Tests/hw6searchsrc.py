#Ian Setia
#isetia@nd.edu

import argparse, re

#Reads a given file and returns a list with the lines in the file
def readFile(fileName):
    with open(fileName, 'r') as f:
        lines = []
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            lines.append(line)
        return lines

#Returns number of lines
def countLines(fileName):
    lines = readFile(fileName)
    return len(lines)

#Scans each line in the list of lines for the #include
def countInclude(fileName):
    lines = readFile(fileName)
    i = 0
    for line in lines:
        if line.startswith('#include'):
            i+=1
    return i

#Scans each line in the list of lines for #include "
def countIncludeLocal(fileName):
    lines = readFile(fileName)
    i = 0
    for line in lines:
        if line.startswith('#include "'):
            i+=1
    return i

#Counts number of :: substrings present in every line, returns sum
def countMember(fileName):
    lines = readFile(fileName)
    m = 0
    for line in lines:
        m+=line.count('::')
    return m

#Count number of lines that start with alphanumeric and contains ::
def countMemberFuncs(fileName):
    lines = readFile(fileName)
    m = 0;
    for line in lines:
        #search for alphanumeric start with :: being present somewhere in the line
        if(re.search(r'^[a-zA-Z0-9].*::', line)):
            m+=1
    return m

#Similar to countMember (searches for -> instead of ::) returns pointer count
def countPtr(fileName):
    lines = readFile(fileName)
    p = 0
    for line in lines:
        p+=line.count('->')
    return p

#counts number of one line functions using regex
def countOneLineFuncs(fileName):
    lines = readFile(fileName)
    f = 0
    check = 0
    for line in lines:
        #search for alphanumeric beginning and { at end if there is one
        if(re.search(r'^[a-zA-Z0-9].*[{]?$', line)):
            check = 1
        elif(check == 2 and re.search(r'^}$', line)):
            check = 0
            f += 1
        elif(check == 1):
            #search for { at start of line in case it wasn't on previous function line
            if re.search(r'^{$', line):
                check = 1
            else:
                check = 2
        else:
            check = 0
    return f
    
#Counts the number of 0 or 1 lined functions whose curly braces appear on their own lines
def countSimplefunc(fileName):
    lines = readFile(fileName)
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
def countSimplefuncec(fileName):
    lines = readFile(fileName)
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
    
def extract_filename_filepath(filename):
    match = re.search(r'^(.*[\\/])([^\\/]+)$', filename)
    path, file_name = match.groups()
    return path, file_name


def main():
    parser = argparse.ArgumentParser()

    #adds argument tags to identify from command line
    parser.add_argument('fileName', type=str, help='name of file to scan')
    parser.add_argument('--include', action='store_true', help='counts number of include statements in code')
    parser.add_argument('--includelocal', action='store_true', help='counts number of local include statements in code')
    parser.add_argument('--member', action='store_true', help='')
    parser.add_argument('--memberfuncs', action='store_true', help='counts number of member functions')
    parser.add_argument('--ptr', action='store_true', help='count number of -> pointers')
    parser.add_argument('--onelinefuncs', action='store_true', help='counts number of one line functions')
    parser.add_argument('--simplefunc', action='store_true', help='counts number of simple functions')
    parser.add_argument('--simplefuncec', action='store_true', help='counts number of simple functions whose \'{\' can be on same line as function')

    args = parser.parse_args()

    fileName = args.fileName
    #searches for the final / or \ in the line, then separates the file name into group 2, getting anything after the final / or \
    #match = re.search(r'^(.*[\\/])([^\\/]+)$', fileName)
    path, file_name = extract_filename_filepath(fileName)
    print("path: {}".format(path)) 
    print("file: {}\nlines: {}".format(file_name, countLines(fileName)))

    #checks for argument tags before printing wanted information
    if args.include:
        print("include: {}".format(countInclude(fileName)))
    if args.includelocal:
        print("includelocal: {}".format(countIncludeLocal(fileName)))
    if args.memberfuncs:
        print("memberfuncs: {}".format(countMemberFuncs(fileName)))
    if args.member:
        print("member: {}".format(countMember(fileName)))
    if args.ptr:
        print("ptr: {}".format(countPtr(fileName)))
    if args.onelinefuncs:
        print("onelinefuncs: {}".format(countOneLineFuncs(fileName)))
    if args.simplefunc:
        print("simplefunc: {}".format(countSimplefunc(fileName)))
    if args.simplefuncec:
        print("simplefuncec: {}".format(countSimplefuncec(fileName)))

    print("")

    
if __name__ == "__main__":
    main()
