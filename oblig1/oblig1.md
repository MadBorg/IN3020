# Oblig 1 - Sanders

## 1.1 Self Join

### a.

``` sql
SELECT personnel.ospID, manager.ospID, manager.smID, manager.function
FROM OnStagePersonnel AS personnel
LEFT JOIN StageManager AS manager
    USING (ospID)

-- GROUP BY manager.function;
;
```

## 1.2

### a .

The division is a operator which gives the values from the dividend that is related to all values from the divisor.

F.eks

Dividend:

| A | B |   
|---|---|   
| a | 1 |   
| d | 2 |   
| c | 1 |
| a | 3 |   
| a | 2 |   
| c | 1 | 

Divisor:

| S |
|---|
| a |
| b |
| c |

Quotient:

| T |
|---|
| 1 |
