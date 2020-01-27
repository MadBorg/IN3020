# INDEXING

<!--
 ``` sql

``` 
-->

## Infromation

chap. 6th,  7th ( SQL )

Not planing to have recursive in the exam, but might have a task on in in the oblig, or in a weekly task. 

* Today: chap. 16th, 17th
* next time: (5th relationel algebra, nex time?)
* ... : 20th, 21st, 22nd - transactions?
* ... : 18th, 19th -  query
* ... : 30th - Security

There might se solutions for the exercises online.

## Types

* Conventional indexes
* B-rees and hashing
* Multidimensional indexes
* Tree structures
* Hash-like insexing
* Bitmap indexe


## what is an index

Helping in finding the data we are looking for.
The simplest is probably the hash-index.

## Index

* Usually sorted.
    * Organized, such that it fits the search we are going to use.
    * Organizing in some benifital way.
* One or many
    * sparsed or dence.
    * With more search is usualy faster but needs space
* Hirarki
* Might just make everything more complex

Dence or sparse. One for all or one for many. 

Primary index: one to one, sorted physically on the search key.

Cluster index: one to many, sill sorted physically, but allows groups.

## Delation in the case of sparse index

When you delete you might need to re organize the indexses. espessialy if you use sparse indexing. Sometimes we dont have to re organize the indexing. Some blocks might have empty spaces. Sometimes you enter a new block. We like to leave free spaces for postentional new values. You can compress and the db will take less space but you can also uncompress for faster insertion.



## --

Blocks do not always stay together. They might be saved at other places. Dont have to be saved continusly. This is solved with pointers.

## Cluster indexes

* Earlier the key had to be the same, here it can be multiple 10ns. Key does not have to be uniqe.
* All the similar keys is sotred next to eachother.
* Fast, espessialy if you are looking for a group.

## unsorted files Secondary indexes

If the file is not sorted, or sorted on another val. You might need a Secondary index. So the secondary is sorted on the value you want.

First level is always dence. Higer levels is sparce.

## inverted index

* SELECT * FROM R where a like '%cat%'
* Search for documents
* Its inverted becouse it is first looking at the data, for then to find the ID.
* Index with kety words?

## How to store an index

* In sorted lists

__B+ Trees (Balances Binary Tree)__

* The nodes are blocks
* Leafs is sstored with pointers to the nex value.

Efficiency

* negative - Must always start from root.
* positive - The number of levels is usually vety low (typically 3)
* positive - Intervall search is fast
* positive - For large n, it is rearly necessary to split / merge 
* positive - Disk I/O can be reduced by keeping some of the index blocks in mem

## Hash Tables

* It points to buckets of informations
* We often mix block and bucket, but its not the same
* Array size is usualy prime numbers
* Its fast since its only a function to get to the place

Efficiency

* Idealy, the array size is large enough so that all elements of one hash value fit into one bucket block.
* Good for something, but not all.

## Dynamic hash tables

* the Index array is dynamic
* Linear, extensive hasing

## Multidimentioal indices

Searching for two(multiple) values in at the same time. To help with the situation

``` sql
SELECT * FROM table WHERE x < 10 and a = 10;
```

## Map View

* In two dimentions we can visualize it in a map.
* Points: a_1 and b1
* Lines:
* ...

## Tree Structures

* K-d trees
* Quad-trees
* R - Trees

