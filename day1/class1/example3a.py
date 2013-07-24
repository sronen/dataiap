# Filter the donations dataset for Obama and McCain donations only.
import sys

with file(sys.argv[1], 'r') as f: 
    print f.readline() # first line contains the CSV headers

    for line in f:
        if "Obama" in line or "McCain" in line:
            # 'in' is case-sensitive and won't pick up
            # donations by MCCAIN or OBAMA
                print line[:-1]