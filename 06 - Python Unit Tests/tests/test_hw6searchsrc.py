#Ian Setia
#isetia@nd.edu
import unittest
import sys, os, subprocess, re
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from hw6searchsrc import *

class TestHW6SearchSrc(unittest.TestCase):
    def test_countLines(self):
        self.assertEqual(countLines("./data/fmnc_manager.cc"), 2310)
        self.assertEqual(countLines("./data/ParamDictionary.cc"), 379)
        self.assertEqual(countLines("./data/PktQueue.cc"), 42)
        self.assertEqual(countLines("./data/RIPPS_PktPair.cc"), 607)
        self.assertEqual(countLines("./data/Thread_IO.cc"), 149)
    def test_countInclude(self):
        self.assertEqual(countInclude("./data/fmnc_manager.cc"), 18)
        self.assertEqual(countInclude("./data/ParamDictionary.cc"), 3)
        self.assertEqual(countInclude("./data/PktQueue.cc"), 1)
        self.assertEqual(countInclude("./data/RIPPS_PktPair.cc"), 5)
        self.assertEqual(countInclude("./data/Thread_IO.cc"), 7)
    def test_countIncludeLocal(self):
        self.assertEqual(countIncludeLocal("./data/fmnc_manager.cc"), 11)
        self.assertEqual(countIncludeLocal("./data/ParamDictionary.cc"), 1)
        self.assertEqual(countIncludeLocal("./data/PktQueue.cc"), 1)
        self.assertEqual(countIncludeLocal("./data/RIPPS_PktPair.cc"), 3)
        self.assertEqual(countIncludeLocal("./data/Thread_IO.cc"), 5)
    def test_countMemberFuncs(self):
        self.assertEqual(countMemberFuncs("./data/fmnc_manager.cc"), 77)
        self.assertEqual(countMemberFuncs("./data/ParamDictionary.cc"), 26)
        self.assertEqual(countMemberFuncs("./data/PktQueue.cc"), 4)
        self.assertEqual(countMemberFuncs("./data/RIPPS_PktPair.cc"), 50)
        self.assertEqual(countMemberFuncs("./data/Thread_IO.cc"), 0)
    def test_countOneLineFuncs(self):
        self.assertEqual(countOneLineFuncs("./data/fmnc_manager.cc"), 36)
        self.assertEqual(countOneLineFuncs("./data/ParamDictionary.cc"), 10)
        self.assertEqual(countOneLineFuncs("./data/PktQueue.cc"), 4)
        self.assertEqual(countOneLineFuncs("./data/RIPPS_PktPair.cc"), 23)
        self.assertEqual(countOneLineFuncs("./data/Thread_IO.cc"), 0)
    def test_extract_filename_filepath(self):
        self.assertEqual(extract_filename_filepath("./data/fmnc_manager.cc"), ("./data/", "fmnc_manager.cc"))
        self.assertEqual(extract_filename_filepath("./data/ParamDictionary.cc"), ("./data/", "ParamDictionary.cc"))
        self.assertEqual(extract_filename_filepath("./data/PktQueue.cc"), ("./data/", "PktQueue.cc"))
        self.assertEqual(extract_filename_filepath("./data/RIPPS_PktPair.cc"), ("./data/", "RIPPS_PktPair.cc"))
        self.assertEqual(extract_filename_filepath("./data/Thread_IO.cc"), ("./data/", "Thread_IO.cc"))
        #Random other files to test the function 
        self.assertEqual(extract_filename_filepath("./../../../somedir/subdir/note.jpeg"), ("./../../../somedir/subdir/", "note.jpeg"))
        self.assertEqual(extract_filename_filepath("/home/user/documents/project/file.txt"), ("/home/user/documents/project/", "file.txt"))

    def run_hw6searchsrc(self, *args):
        results = subprocess.run(
            ['python3', '../hw6searchsrc.py'] + list(args), 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = results.stdout.decode('utf-8')
        stderr = results.stderr.decode('utf-8')
        return stdout, stderr

    def test_min_args(self):
        stdout, stderr = self.run_hw6searchsrc("./data/fmnc_manager.cc")
        self.assertRegex(stdout, r'path: .*\nfile: fmnc_manager.cc\nlines: \d+')


    def test_all_flags(self):
        stdout, stderr = self.run_hw6searchsrc(
            "./data/fmnc_manager.cc", '--include', 
            '--includelocal', '--member', '--memberfuncs', 
            '--ptr', '--onelinefuncs', '--simplefunc', 
            '--simplefuncec')
        self.assertRegex(stdout, r'path: .*\nfile: fmnc_manager.cc\nlines: \d+')
        self.assertRegex(stdout, r'include: \d+')
        self.assertRegex(stdout, r'includelocal: \d+')
        self.assertRegex(stdout, r'member: \d+')
        self.assertRegex(stdout, r'memberfuncs: \d+')
        self.assertRegex(stdout, r'ptr: \d+')
        self.assertRegex(stdout, r'onelinefuncs: \d+')
        self.assertRegex(stdout, r'simplefunc: \d+')
        self.assertRegex(stdout, r'simplefuncec: \d+')

    def test_subset_of_flags(self): 
        stdout, stderr = self.run_hw6searchsrc(
            "./data/fmnc_manager.cc", '--includelocal',
            '--memberfuncs', '--onelinefuncs')
        self.assertRegex(stdout, r'path: .*\nfile: fmnc_manager.cc\nlines: \d+')
        self.assertRegex(stdout, r'includelocal: \d+')
        self.assertRegex(stdout, r'memberfuncs: \d+')
        self.assertRegex(stdout, r'onelinefuncs: \d+')

    def test_argument_order(self):
        stdout, stderr = self.run_hw6searchsrc(
            "./data/fmnc_manager.cc", '--simplefuncec', 
            '--includelocal', '--onelinefuncs', '--ptr', 
            '--memberfuncs', '--include', '--simplefunc', 
            '--member')
        self.assertRegex(stdout, r'path: .*\nfile: fmnc_manager.cc\nlines: \d+')
        self.assertRegex(stdout, r'include: \d+')
        self.assertRegex(stdout, r'includelocal: \d+')
        self.assertRegex(stdout, r'member: \d+')
        self.assertRegex(stdout, r'memberfuncs: \d+')
        self.assertRegex(stdout, r'ptr: \d+')
        self.assertRegex(stdout, r'onelinefuncs: \d+')
        self.assertRegex(stdout, r'simplefunc: \d+')

    def test_absolute_path(self):
        stdout, stderr = self.run_hw6searchsrc(
            "/escnfs/home/isetia/repos/student-cse20289-fa24-isetia/hw/hw06/tests/data/fmnc_manager.cc")
        self.assertRegex(stdout, r'path: /escnfs/home/isetia/repos/student-cse20289-fa24-isetia/hw/hw06/tests/data/\nfile: fmnc_manager.cc\nlines: \d+')

    def test_no_specified_file(self):
        stdout, stderr = self.run_hw6searchsrc()
        self.assertIn("error", stderr.lower())
    
    def test_nonexistent_file(self):
        stdout, stderr = self.run_hw6searchsrc("nonexistentFile.cc")
        self.assertIn("error", stderr.lower())
        
    def test_not_cc_file(self): #if file exists, code will run normally regardless of type, if file does not exist, it will error regardless of type
        stdout, stderr = self.run_hw6searchsrc("file.txt")
        self.assertIn("error", stderr.lower())
        stdout, stderr = self.run_hw6searchsrc("./data/file.txt")
        self.assertRegex(stdout, r'path: ./data/\nfile: file.txt\nlines: \d+')

    
    def test_file_is_directory(self):
        stdout, stderr = self.run_hw6searchsrc("./data/")
        self.assertIn("error", stderr.lower())

    def test_invalid_argument(self):
        stdout, stderr = self.run_hw6searchsrc("./data/fmnc_manager.cc", '--invalidflag')
        self.assertIn("error", stderr.lower())

if __name__ == "__main__":
    unittest.main()
