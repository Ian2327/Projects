#!/bin/sh

timestamp=$(date "+%Y-%m-%d_%H-%M")
log="${timestamp}_UnitTest.log"

echo "Running the unit tests for Homework 2 ..."
echo "  Saving the results in timestamped files: ${log}"

cd tests/
python3 -m unittest discover &> "../$log"
cd - > /dev/null

if grep -q "FAILED" "${log}"; then
	echo "  Some test(s) failed. Displaying log:"
	cat "${log}"
else
	echo "  All tests passed successfully!"
fi

echo "  Log is stored at: $(find -iname ${log})"

