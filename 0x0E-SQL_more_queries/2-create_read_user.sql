-- Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* IF EXISTS TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
