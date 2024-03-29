-- Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

-- You need to convert all of the following to UTF8:

	-- Database hbtn_0c_0
	-- Table first_table
	-- Field name in first_table

-- Convert the database to UTF8
ALTER DATABASE hbtn_0c_0 COLLATE utf8mb4_unicode_ci;

-- Convert the first_table table to UTF8
ALTER TABLE hbtn_0c_0.first_table COLLATE utf8mb4_unicode_ci;

-- Convert the name field in the first_table table to UTF8
ALTER TABLE hbtn_0c_0.first_table CHANGE name name VARCHAR(255) COLLATE utf8mb4_unicode_ci;
