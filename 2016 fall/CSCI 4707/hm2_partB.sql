// B1(2) //
Select O1.sid
from(Select O.sid, COUNT(O.method) AS thecount
	from Onestop O
	GROUP BY O.sid) AS O1
)
WHERE 1.thecount = 2;



 //B3//
 SElECT DISTINCT A.name 
 from (Select M.mid AS tmid
 	   from Directors D, Movies M
 	   where D.name = 'Spielberg' AND D.did = M.did) AS M1, Casts C, Actor A
WHERE C.did = A.aid AND  C.mid = M1.tmid AND A.name NOT IN (SELECT A2.name
                                                            FROM Actor A2,Directors D2, Movies M2, Casts C2
                                                            WHERE D2.name<>'Spielberg' AND D2.did=M2.did AND M2.mid=C2.mid AND A2.aid=C2.aid
                                                           );

      



Select C.cid
FROM Customer C
WHERE NOT EXISTS(SELECT B.pid
                 FROM Buys B
                 WHERE B.cid=C.cid and B.pid NOT IN(SELECT temp.pid
                                                    FROM (SELECT COUNT(DISTINCT B2.cid) AS num,B2.pid
                                                          FROM Buys B2
                                                          GROUP BY B2.pid) AS temp, ( SELECT COUNT(C2.cid) AS num FROM Customer C2) AS NUM
                                                    WHERE temp.num=NUM.num 
                                                    )
                 );