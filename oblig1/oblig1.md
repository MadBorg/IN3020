# Oblig 1 - Sanders

## 1.1 Self Join

### a.

``` sql
SELECT personell.name, personell.lastname, manager.name, manager.lastname, manager.function
FROM OnStagePersonnell personell
LEFT JOIN StageManager manager
    WHERE personell.ospID == manager.ospID

GROUP BY manager.function

```