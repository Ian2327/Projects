Ian Setia
isetia@nd.edu

Task 3d: if file is not a .cc file, the code will just run as normal (however, will probably will print 0 for all values other than lines)

Task 4: although my hw6searchsrc code will run on non .cc files, the hw6searchdir will filter on the .cc files, so that no other types of files will be scanned

Task 5: must do 'chmod +x doTests.sh' to enable executable form

Task 6:
- Bugs (hw6searchsrc):
	- line 21: added + 1 to line count
	- line 28: added " to search pattern to search for local includes rather than just includes
	- line 37: removed " from search pattern to search for all includes
- Failed Test Cases (hw6searchsrc):
	test_deeper_recursive_dir,
	test_non_recursive,
	test_recursive,
	test_countInclude,
	test_countIncludeLocal,
	test_countLines 

- Bugs (hw6searchdir):
	- line 26: added extra comma to output formatting 
- Failed Test Cases (hw6searchdir):
	test_deeper_recursive_dir,
	test_non_recursive,
	test_recursive
