# samples the donations for Obama and McCain. It will print 1 out of every 1000 donations to either Obama or McCain (or roughly 3900 total donations):
import sys

with file(sys.argv[1], 'r') as f: 
    i = 0
    print f.readline() # first line contains the CSV headers
    
    for line in f:
        if "Obama" in line or "McCain" in line:
            if i % 1000 == 0:
                # 'in' is case-sensitive and won't pick up
                # donations by MCCAIN or OBAMA
                print line[:-1]
            i += 1
