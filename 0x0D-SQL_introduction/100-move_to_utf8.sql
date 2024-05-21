-- alter a table

USE hbtn_0c_0;  -- Set the database to use

-- Convert the database schema to UTF-8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Convert the data in the 'first_table' to UTF-8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Convert the 'name' column to UTF-8 (optional)
ALTER TABLE first_table MODIFY name CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
