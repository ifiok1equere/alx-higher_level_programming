-- Write a script that lists all cities contained in the database hbtn_0d_usa.

SELECT c.id, c.name, s.name  FROM cities as c JOIN states as s on c.state_id=s.id;
