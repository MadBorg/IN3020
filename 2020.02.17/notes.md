# Query Compilation

* Commutative
  * Natural join, product, Theta-join, Union, Intersection
* Associative
  *  Natural join, product, Union, Intersection

## Order of produkt and join

* Order does matter on efficiency
* If we can estimate the sizes we can iptimize

## Algebaic laws.

* Some laws may be different for sets and bags
* R ∩S (S ∪S T) = (R ∩S S) ∪S (R ∩S T)
* R ∩B (S ∪B T) ≠ (R ∩B S) ∪B (R ∩B T)

## Alg - Projection

* Projection can be pushed through join and cross product, as long as we do not remove attributes used further up the tree.
* 