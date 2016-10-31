SELECT inter.sid1,inter.sid2, inter.cid
FROM (SELECT E1.sid AS sid1,E2.sid AS sid2,E1.cid
      FROM Enroll E1,Enroll E2
      WHERE E1.sid!=E2.sid AND E1.cid=E2.cid AND E1.sid<E2.sid)AS inter
WHERE NOT EXISTS(SELECT *
                 FROM (SELECT inter.sid1 AS sid1, inter.sid2 AS sid2, Enroll.cid
                       FROM inter,Enroll
                       WHERE Enroll.sid=inter.sid1 OR Enroll.sid=inter.sid2) AS full_set
                 WHERE full_set.sid1=inter.sid1 AND full_set.sid2=inter.sid2 AND full_set.cid!=inter.cid
                 )

--B.1.A
SELECT inter_sect.sid1, inter_sect.sid2
FROM 
(
    SELECT E1.sid AS sid1, E2.sid AS sid2, COUNT(E1.cid) AS NUM
    FROM Enroll E1, Enroll E2
    WHERE E1.sid1<E2.sid2 AND E1.cid=E2.cid
    GROUP BY E1.sid,E2.sid
) inter_sect,
(
    SELECT E3.sid AS sid, COUNT(E3.cid) AS NUM
    FROM Enroll E3
    GROUP BY E3.sid
) temp1,
(
    SELECT E4.sid AS sid, COUNT(E4.cid) AS NUM
    FROM Enroll E4
    GROUP BY E4.sid
) temp2
WHERE
(
   inter_sect.sid1=temp1.sid
   AND inter_sect.sid2=temp2.sid
   AND inter_sect.NUM=temp1.NUM
   AND inter_sect.NUM=temp2.NUM
)
;




--B.2.B
SELECT temp2.sid
FROM
(
  SELECT O3.sid AS sid
  FROM onestop O3, onestop O4
  WHERE O3.sid=O3.sid AND O3.method<>O4.method 
)AS temp2
WHERE temp2.sid NOT IN  
(
    SELECT temp.sid
    FROM  onestop,(SELECT O1.sid, O1.method AS method1, O2.method AS method2
                   FROM onestop O1, onestop O2
                   WHERE O1.sid=O2.sid AND O1.method<>O2.method) AS temp
    WHERE onestop.sid=temp.sid AND onestop.method<>temp.method1 AND onestop.method<>temp.method2
); 


