# query compilation

* Query managment
* Model for cost calc
* cost of basic operations
* Implemention alg

## Quary managment

* each compilation gives expreience (metadata, ...)

## Physical operators

* cost is size
* number of disc I/Os, is a cost
* Need to be able to estimate cost of each operator

## Cost parameters

* facotrs of cost:
    * Number of blocs available in mem, M
    * Wether there are indexes
    * disc
    * ...
* for eeach relation
  * Number of blocks required to store all the tuple, B_R
  * Number of tuples, T_R
  * Number of destinct values for an attribute A, V_R(A)
  * Average number of tuoples

   We will generally assume tightly packed relations!

## factors that increase cost

* Use of indexes that are not in mem
  * Contributes to increase cost
* ...

## Cost of basic operations

* Reading a disc block is 1 disc IO
* Writing 1 disc IO
* Unsorted reading a relation R
  * Clustered relation: B_R disc IO
  * Scattered relation - worst case T_R disc IOs, can be worse
* sorting - 
* hash partitioning, not sufficicient mem, ...

* Remember that Postgres differ between - sequential read and random read
  * Mostly sequntial

## ingestion and indices

* In postgres, indices are dence
* Indexes is not ued if we have to mant duplicates
  * Postgress stil want to use them but they will be different

## Bitmap heap scan

* Random reads can read the same block several times, creasing cost
* Bitmap heap scan fixes this
* Idea: Read index, find block number for all the tuples we should have. Read the correct blocks in their order. 

## Sorting

* if the relation fits in mem we sort it
* if the relation does not fit in mem, we use a algroithm that is efficient on muliple data sets
* Frequently used: Two-Phase Multiway Merge Sort (TPMMS)

## Two-Phase Multiway Merge Sort (TPMMS)

* Cost 2B_R, for phase 1, all blocks are both read and written
* cosr B_R, for phase 2
* M >= sqrt(B_R)

## Hash partitioning

* cost: 2B_R

## Executing the Query

* Three main classes of algorithms:
  * Sort based, hash based, index-based
* cost and complexity is divided into different elvels
  * One pass, data fits in mem
  * Two pass, data to large
  * n pass, recursive genrealizations of two pas alg.

## roups of operators

* Tuple-at-a-time, unary operations:
  * selection (!)
  * projection (")
* Full-relation, unary operations:
  * grouping (#)
  * duplicate elimination ($)
* Binary operations:
  * set and bag union (∪)
  * set and bag sections (∩)
  * set and bag difference (−)
  * join (⋈)
  * product (×)

