from sys import argv
# read the WhatYouShouldSee section for how to run this
"""
What You Should See

	WARNING! Pay attention! You have been running python scripts without command line
	arguments. If you type only python3.6 ex13.py you are doing it wrong! Pay close
	attention to how I run it. This applies any time you see argv being used.
"""
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
"""
pass 3 command line arguments
example - python ex13.py 1st_Argument 2nd_Argument 3rd_Argument
"""
