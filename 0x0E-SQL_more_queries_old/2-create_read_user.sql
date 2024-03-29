-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2.

	-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
	-- The user_0d_2 password should be set to user_0d_2_pwd
	-- If the database hbtn_0d_2 already exists, your script should not fail
	-- If the user user_0d_2 already exists, your script should not failWrite a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* IF EXISTS TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
