--#1
SELECT eid,ename
FROM
(
SELECT eid,ename
FROM Emp
WHERE eid IN(
 (SELECT eid FROM Works WHERE did=1)
)
)
WHERE eid IN ((SELECT eid FROM Works WHERE did=2));


--#2
SELECT did,numberOfemp
FROM
(SELECT did,count(did) AS numberOfemp
FROM WORKS
GROUP BY did)
WHERE numberOfemp>10;

--#3
SELECT E.ename
FROM Emp E
WHERE E.salary>ANY(SELECT D.budget
	                 FROM Dept D
	                  WHERE D.did IN(
                    SELECT D2.did
                    FROM Emp E2,Dept D2,Works W2
                    Where E2.eid=E.eid AND E2.eid=W2.eid AND W2.did=D.did));


--#4
SELECT DISTINCT D.managerid
FROM Dept D
WHERE D.managerid NOT IN  (SELECT D2.managerid
	                            FROM Dept D2
	                            WHERE D2.budget<=50000000
														  );

--#5
SELECT E.ename
FROM Emp E,Dept D
WHERE E.eid=D.managerid AND D.budget=(SELECT MAX(D2.budget)
	                                       FROM Dept D2
                                      );
--#6
SELECT DISTINCT D.managerid
FROM Dept D
WHERE (SELECT SUM(D2.budget) AS sum
       FROM Dept D2
			 WHERE D2.managerid=D.managerid
		  )>50000000;

--#7
SELECT D1.managerid
FROM (SELECT SUM(D.budget) AS sum,managerid
      FROM Dept D
      GROUP BY D.managerid)  D1
WHERE D1.sum=(SELECT MAX(SUM(D2.budget))
	           FROM Dept D2
						 GROUP BY D2.managerid
					 );

--#8
SELECT E3.ename
FROM Emp E3
WHERE E3.eid IN(
(SELECT  DISTINCT E1.eid
FROM Emp E1,Dept D1
WHERE E1.eid=D1.managerid
MINUS
SELECT DISTINCT E.eid
FROM Emp E,Dept D
WHERE E.eid=D.managerid AND D.budget<=30000000)
MINUS
SELECT DISTINCT D2.managerid
FROM Dept D2
WHERE D2.managerid NOT IN  (SELECT D3.managerid
	                            FROM Dept D3
	                            WHERE D3.budget<50000000
														)
);
