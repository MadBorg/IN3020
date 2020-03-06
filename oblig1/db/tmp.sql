SELECT b
FROM R
WHERE a NOT EXISTS (
    SELECT b
    FROM R
    WHERE b NOT EXISTS (
        SELECT b
        FROM (SELECT b FROM R) AS C
        CROSS JOIN S
        WHERE C.b NOT EXISTS (SELECT b FROM R)
    )
);



group: nameOfTheNewGroup 

R = {
	A, B, C, W
	1, 'z', 1, 4
	2, 'c', 6, 2
	3, 'r', 8, 7
	4, 'n', 9, 4
	2, 'j', 0, 3
	3, 't', 5, 9
	7, 'e', 3, 3
	8, 'f', 5, 8
	1, 'h', 7, 5
}

S = {
	X, Y, Z
	1, 'a', 'a'
	2, 'f' ,'c'
	3, 't', 'b'
	4, 'b', 'b'
	7, 'k', 'a'
	6, 'e', 'a'
	7, 'g', 'c'
	8, 'i', 'b'
	9, 'e', 'c'
	
}