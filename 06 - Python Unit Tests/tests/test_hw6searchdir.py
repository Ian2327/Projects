#Ian Setia
#isetia@nd.edu

import unittest
import sys, os, subprocess, re
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
from hw6searchdir import *

class TestHW6SearchDir(unittest.TestCase): 
    def run_hw6searchdir(self, *args):
        results = subprocess.run(
            ['python3', '../hw6searchdir.py'] + list(args),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = results.stdout.decode('utf-8')
        stderr = results.stderr.decode('utf-8')
        return stdout, stderr
    def test_non_recursive(self):
        stdout, stderr = self.run_hw6searchdir("./data/ex-tests/nrd-1/")
        self.assertRegex(stdout, r'./data/ex-tests/nrd-1/, ParamDictionary.cc, 379 LOC, 3 I, 1 LI, 26 MF, 10 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-1/, PktQueue.cc, 42 LOC, 1 I, 1 LI, 4 MF, 4 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-1/, RIPPS_PktPair.cc, 607 LOC, 5 I, 3 LI, 50 MF, 23 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-1/, Thread_IO.cc, 149 LOC, 7 I, 5 LI, 0 MF, 0 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-1/, fmnc_manager.cc, 2310 LOC, 18 I, 11 LI, 77 MF, 36 OLF')
        stdout, stderr = self.run_hw6searchdir("./data/ex-tests/nrd-2/")
        self.assertRegex(stdout, r'./data/ex-tests/nrd-2/, Adapter.cc, 724 LOC, 12 I, 11 LI, 42 MF, 16 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-2/, ParamDictionary.cc, 379 LOC, 3 I, 1 LI, 26 MF, 10 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-2/, PktQueue.cc, 42 LOC, 1 I, 1 LI, 4 MF, 4 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-2/, RIPPS_PktPair.cc, 607 LOC, 5 I, 3 LI, 50 MF, 23 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-2/, TWiCE_Gateway.cc, 991 LOC, 7 I, 6 LI, 22 MF, 5 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-2/, Thread_IO.cc, 149 LOC, 7 I, 5 LI, 0 MF, 0 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-2/, fmnc_manager.cc, 2310 LOC, 18 I, 11 LI, 77 MF, 36 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-2/, fmnc_test_sequence.cc, 2662 LOC, 9 I, 5 LI, 84 MF, 44 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-2/, ip-utils.cc, 1239 LOC, 5 I, 1 LI, 0 MF, 5 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-2/, whirlwind_gateway.cc, 1186 LOC, 12 I, 10 LI, 27 MF, 4 OLF')
        stdout, stderr = self.run_hw6searchdir("./data/ex-tests/nrd-3/")
        self.assertRegex(stdout, r'./data/ex-tests/nrd-3/, Adapter.cc, 724 LOC, 12 I, 11 LI, 42 MF, 16 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-3/, AdapterFile.cc, 812 LOC, 9 I, 8 LI, 32 MF, 16 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/nrd-3/, AdapterPCap.cc, 211 LOC, 7 I, 6 LI, 14 MF, 8 OLF')

        
    def test_recursive(self):
        stdout, stderr = self.run_hw6searchdir('-r', './data/ex-tests/rd-1')
        self.assertRegex(stdout, r'./data/ex-tests/rd-1/, ParamDictionary.cc, 379 LOC, 3 I, 1 LI, 26 MF, 10 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-1/, PktQueue.cc, 42 LOC, 1 I, 1 LI, 4 MF, 4 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-1/, RIPPS_PktPair.cc, 607 LOC, 5 I, 3 LI, 50 MF, 23 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-1/, Thread_IO.cc, 149 LOC, 7 I, 5 LI, 0 MF, 0 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-1/, fmnc_manager.cc, 2310 LOC, 18 I, 11 LI, 77 MF, 36 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-1/sd/, TWiCE_Gateway.cc, 991 LOC, 7 I, 6 LI, 22 MF, 5 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-1/sd/, whirlwind_gateway.cc, 1186 LOC, 12 I, 10 LI, 27 MF, 4 OLF')
        stdout, stderr = self.run_hw6searchdir('-r', './data/ex-tests/rd-2')
        self.assertRegex(stdout, r'./data/ex-tests/rd-2/, fmnc_client.cc, 10 LOC, 0 I, 0 LI, 0 MF, 0 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-2/, fmnc_connection.cc, 685 LOC, 3 I, 2 LI, 66 MF, 47 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-2/, fmnc_connection_tcp_slice.cc, 609 LOC, 4 I, 3 LI, 43 MF, 24 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-2/, fmnc_manager.cc, 2310 LOC, 18 I, 11 LI, 77 MF, 36 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-2/, fmnc_measurement_packet.cc, 847 LOC, 4 I, 2 LI, 75 MF, 31 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-2/sd3/, MemPoolCustom.cc, 52 LOC, 2 I, 2 LI, 0 MF, 0 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-2/sd3/, MemPoolObject.cc, 189 LOC, 13 I, 13 LI, 13 MF, 9 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-2/sd2/, fmnc_session.cc, 10 LOC, 0 I, 0 LI, 0 MF, 0 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-2/sd2/, fmnc_support.cc, 26 LOC, 2 I, 2 LI, 0 MF, 0 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-2/sd2/, fmnc_test_analysis.cc, 567 LOC, 7 I, 5 LI, 29 MF, 14 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-2/sd2/, fmnc_test_sequence.cc, 2662 LOC, 9 I, 5 LI, 84 MF, 44 OLF')
        stdout, stderr = self.run_hw6searchdir('-r', './data/ex-tests/rd-3')
        self.assertRegex(stdout, r'./data/ex-tests/rd-3/, Adapter.cc, 724 LOC, 12 I, 11 LI, 42 MF, 16 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-3/, AdapterFile.cc, 812 LOC, 9 I, 8 LI, 32 MF, 16 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-3/, AdapterPCap.cc, 211 LOC, 7 I, 6 LI, 14 MF, 8 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-3/mon/, Monitor.cc, 224 LOC, 8 I, 7 LI, 14 MF, 5 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-3/mon/, Thread_Archive.cc, 209 LOC, 5 I, 5 LI, 16 MF, 6 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-3/mon/, Thread_Timer.cc, 588 LOC, 8 I, 6 LI, 36 MF, 17 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-3/packetcache/, PacketCacheEntry.cc, 17 LOC, 2 I, 1 LI, 2 MF, 0 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-3/packetcache/, PacketCacheModule.cc, 137 LOC, 8 I, 5 LI, 7 MF, 3 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-3/packetcache/, PacketCacheSupport.cc, 15 LOC, 2 I, 2 LI, 0 MF, 0 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-3/packetcache/, PacketCacheTable.cc, 610 LOC, 7 I, 5 LI, 7 MF, 4 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-3/packetcache/address/, NetAddress.cc, 291 LOC, 4 I, 3 LI, 30 MF, 16 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-3/packetcache/address/, NetAddressEthernet.cc, 156 LOC, 6 I, 4 LI, 8 MF, 2 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-3/packetcache/address/, NetAddressIPv4.cc, 196 LOC, 6 I, 4 LI, 10 MF, 2 OLF')
        self.assertRegex(stdout, r'./data/ex-tests/rd-3/packetcache/address/, NetAddressIPv4Subnet.cc, 161 LOC, 6 I, 4 LI, 9 MF, 2 OLF')
        stdout, stderr = self.run_hw6searchdir('-r', './data/ex-tests/rd-4')
        self.assertRegex(stdout, r'./data/ex-tests/rd-4/, AdapterPCap.cc, 211 LOC, 7 I, 6 LI, 14 MF, 8 OLF')

    def test_deeper_recursive_dir(self):
        stdout, stderr = self.run_hw6searchdir('-r', "./data/ex-tests/rd-deep")
        self.assertRegex(stdout, r'data/ex-tests/rd-deep/sub_dir/, fmnc_client.cc, 10 LOC, 0 I, 0 LI, 0 MF, 0 OLF')
        self.assertRegex(stdout, r'data/ex-tests/rd-deep/sub_dir/rd-1/, ParamDictionary.cc, 379 LOC, 3 I, 1 LI, 26 MF, 10 OLF')
        self.assertRegex(stdout, r'data/ex-tests/rd-deep/sub_dir/rd-1/, PktQueue.cc, 42 LOC, 1 I, 1 LI, 4 MF, 4 OLF')
        self.assertRegex(stdout, r'data/ex-tests/rd-deep/sub_dir/rd-1/, RIPPS_PktPair.cc, 607 LOC, 5 I, 3 LI, 50 MF, 23 OLF')
        self.assertRegex(stdout, r'data/ex-tests/rd-deep/sub_dir/rd-1/, Thread_IO.cc, 149 LOC, 7 I, 5 LI, 0 MF, 0 OLF')
        self.assertRegex(stdout, r'data/ex-tests/rd-deep/sub_dir/rd-1/, fmnc_manager.cc, 2310 LOC, 18 I, 11 LI, 77 MF, 36 OLF')
        self.assertRegex(stdout, r'data/ex-tests/rd-deep/sub_dir/rd-1/sd/, TWiCE_Gateway.cc, 991 LOC, 7 I, 6 LI, 22 MF, 5 OLF')
        self.assertRegex(stdout, r'data/ex-tests/rd-deep/sub_dir/rd-1/sd/, whirlwind_gateway.cc, 1186 LOC, 12 I, 10 LI, 27 MF, 4 OLF')

    def test_empty_recursive_dir(self):
        stdout, stderr = self.run_hw6searchdir('-r', "./data/ex-tests/rd-empty")
        self.assertRegex(stdout, r'Warning: there are no source files in the given directory')
        self.assertEqual(stderr.strip(), '')

    def test_invalid_directory(self):
        stdout, stderr = self.run_hw6searchdir('-r', "./data/ex-tests/nonexistent_dir")
        self.assertEqual("", stderr)
        self.assertRegex(stdout, r'The directory .* does not exist.')

    def test_invalid_arguments(self):
        stdout, stderr = self.run_hw6searchdir('-z', "./data/ex-tests/rd-1")
        self.assertIn("usage: hw6searchdir.py [-h] [-r] [--csv CSV] [--stats] [--quiet] directory\nhw6searchdir.py: error: unrecognized arguments: -z", stderr)


if __name__ == '__main__':
    unittest.main()
