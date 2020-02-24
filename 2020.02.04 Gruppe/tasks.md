# Indexing

## 14.1.1

### q:
Suppose blocks hold either five records, or 20 key-pointer pairs. As a function of n, the number of records, how many blocks do we need to hold a data file and

a. dense index,
b. sparse index?

### a:

Dence index: n / 5 + n / 20
Sparse index: n / 5 + (n/5) / 20, so then one pointer points to a block?

where n / 5 is data pr. block

## 14.2.1

### q:

Suppose that blocks can hold either ten records or 99 keys and 100 pointers. Also assume that the average B-tree node is 70% full; i.e., it will have 69 keys and 70 pointers. We can use B-trees as part of several different structures. For each structure described below, determine 

i. the total number of blocks needed for a 100,000-record file, and
ii. the average number of disk I/O’s to retrieve a record given its search key.

You may assume nothing is in memory initially, and the search key is the primary key for the records.

a. The data file is a sequential file, sorted on the search key, with 20 records per block. The Btree is a dense index.
b. The same as (a), but the data file consists of records in no particular order, packed 20 to a block.
c. The same as (a), but the B-tree is a sparse index.
d. The data file is a sequential file, and the B-tree is a sparse index, but each primary block of the data file has one overflow block. On average, the primary block is full, and the overflow block is half full. However, records are in no particular order within a primary block and its overflow block.

### a:

block: records: 99, pointers: 100
B-tree node: 70% full, 69 keys, 70 pointers
n = 100,000

a.

number of blocks:

    blocks for data + number of leaf nodes + number of nodes
    n / (records pr block)  + n / ( pointer-key pairs) + , witch gives
    100_000 / 20 + 100_000 / (70) + (100_000 / 70) / 70 + 1 ~= 6451

Disk I/O:

    Root + number of layers (not root and leaf) + leaf + store, gives
    1 + 1 + 1 + 1 = 4

b.

Same as in a. since it is pointers, so reading values in ordered is not going to get any benefit.

c.

Since we have a sparse index then the blocks wee need is calculated with

    100_000 / 20 + (100_000 / 20) / 20 + 1 = 5073
    I/O : 3

