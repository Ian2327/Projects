#Ian Setia
#isetia@nd.edu

import os, subprocess, argparse, csv, statistics

def run_searchsrc_subprocess(file_path, file_name):
    full_path = os.path.join(file_path, file_name)  #combines file path and name
    #command to be run by subprocess
    command = ['python3', '/escnfs/home/isetia/repos/student-cse20289-fa24-isetia/hw/hw06/hw6searchsrc.py', full_path, '--include', '--includelocal', '--memberfuncs', '--onelinefuncs']
    result = subprocess.run(command, stdout=subprocess.PIPE)
    
    #converts to string
    output = result.stdout.decode('utf-8')

    output_dict = {}
    for line in output.split('\n'):
        if ': ' in line:
            key, value = line.split(': ', 1)
            output_dict[key] = value

    return output_dict

#prints the the dictionary given, given that it contains all necessary information
def print_dict(d):
    print("{}, {}, {} LOC, {} I, {} LI, {} MF, {} OLF".format(d.get('path'), d.get('file'), d.get('lines'), d.get('include'), d.get('includelocal'), d.get('memberfuncs'), d.get('onelinefuncs')))

#reads the .cc files in a given directory and returns a dictionary of dictionsaries
def dir_reader(dir_path, isQuiet, isRecursive):
    if not os.path.isdir(dir_path):
        raise FileNotFoundError("The directory {} does not exist.".format(dir_path))

    dir_files = []
    for dirpath, dirnames, filename in os.walk(dir_path):
        for files in filename:
            if(files.endswith(".cc")):
                result = run_searchsrc_subprocess(dirpath, files);
                if not isQuiet:
                    print_dict(result)

                dir_files.append(result)
        if not isRecursive:
            break
    if not dir_files:
        print("Warning: there are no source files in the given directory")

    return dir_files

#returns a csv file with the name csv_name with all data from list of files inputted
def output_csv(file_list, csv_name):
    if os.path.exists(csv_name):
        user_input = input("The file {} already exists in this directory. Overwrite? (yes/no): ").strip().lower()
        if(user_input == 'no'):
            print("Output to CSV has been cancelled")
            return
    
    with open(csv_name, 'w', newline='') as csvfile:
        fieldnames = ['path', 'file', 'lines', 'include', 'includelocal', 'memberfuncs', 'onelinefuncs']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        writer.writerows(file_list)

#computes statistics of list of files
def stats(file_list):
    fields = ['lines', 'include', 'includelocal', 'memberfuncs', 'onelinefuncs']
    #creates a dictionary where each field is initially assigned an empty list
    stats = {field: [] for field in fields}
    for files in file_list:
        for field in fields:
            if field in files:
                files[field] = int(files[field])
                #appends the data to the corresponding list, based on field
                stats[field].append(files[field])
    print("Field, Min, MinFile, Max, MaxFile, Mean, Median, StdDev")
    for field in fields:
        if len(stats[field]) > 1:
            min_val = min(stats[field])
            max_val = max(stats[field])
            mean_val = statistics.mean(stats[field])
            median_val = statistics.median(stats[field])
            stdev_val = statistics.stdev(stats[field])
            min_file = file_list[stats[field].index(min_val)]['file']
            max_file = file_list[stats[field].index(max_val)]['file']
            print("{}, {}, {}, {}, {}, {}, {}, {}".format(field, min_val, min_file, max_val, max_file, mean_val, median_val, stdev_val))
        elif len(stats[field]) == 1:
            min_val = max_val = mean_val = median_val = stats[field][0];
            min_file = max_file = file_list[stats[field].index(min_val)]['file']
            stdev_val = 0;
            print("{}, {}, {}, {}, {}, {}, {}, {}".format(field, min_val, min_file, max_val, max_file, mean_val, median_val, stdev_val))

def main():
    parser = argparse.ArgumentParser()

    #adds argument tags to identify from command line
    parser.add_argument('directory', type=str, help='directory to analyze')
    parser.add_argument('-r', action='store_true', help='denotes if directories should be processed recursively (default=false)')
    parser.add_argument('--csv', type=str, default=None, help='denotes to output csv file (default=false)')
    parser.add_argument('--stats', action='store_true', help='denotes if statistics should be computed across each of the numeric fields and reported (default=false)')
    parser.add_argument('--quiet', action='store_true', help='requests output to stay quiet (default=false)')

    args = parser.parse_args()

    if not args.directory:
        print("Error: No directory given")
        return 
    
    try: 
        file_list = dir_reader(args.directory, isQuiet=args.quiet, isRecursive=args.r);
    except FileNotFoundError as e:
        print(e)
        return

    if args.csv:
        output_csv(file_list, args.csv)
    if args.stats:
        stats(file_list)
    


if __name__ == "__main__":
    main()
