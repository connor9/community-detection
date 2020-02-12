'''
reindex.py

For edgelist files if the node indexes are very high then comboCPP will attempt to allocate memory
as if all the nodes up to that index number were filled in.

I.e.  if your edgelist file is
2500000 250000 4.56
2500000 250001 5.6
it will attempt allocated  multidimensional vectors of up to size 2,500,000*double.
This can quickly exhause allocatable memory.

This script changes a file to rewrite all node indexes to start from 1. It will get all unique node
indexes, de-duplicate and sort them and then map this list to numbers starting from 1.
'''


import csv

filename = 'source.txt'
all_indexes = []
mappings = {}

mappings_counter = 1

with open(filename, 'r') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        all_indexes.append(int(row[0]))
        all_indexes.append(int(row[1]))

all_indexes = sorted(set(all_indexes))
for index in all_indexes:
    mappings[index] = mappings_counter
    mappings_counter = mappings_counter + 1

with open(filename, 'r') as csvfile:
    with open(filename + '.edgelist', 'w', newline='') as csvfile2:
        wr = csv.writer(csvfile2, delimiter=',')
        r = csv.reader(csvfile, delimiter=',')
        for row in r:
            row[0] = mappings[int(row[0])]
            row[1] = mappings[int(row[1])]
            wr.writerow(row)