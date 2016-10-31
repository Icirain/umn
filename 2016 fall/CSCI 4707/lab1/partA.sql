CREATE TABLE Emp
(
  eid int,
  ename varchar(15),
  age int,
  salary int,
  PRIMARY KEY(eid)
);
CREATE TABLE Dept
(
  did int,
  budget int,
  managerid int,
  PRIMARY KEY(did),
  FOREIGN KEY(managerid) REFERENCES Emp(eid)
);
CREATE TABLE Works
(
  eid int,
  did int,
  FOREIGN KEY(eid) REFERENCES Emp(eid),
  FOREIGN KEY(did) REFERENCES Dept(did)
);
