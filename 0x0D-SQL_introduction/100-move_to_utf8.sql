-- Convert a database, table and column to UTF8(utf8mb4, collate utf8mb4_unicode_ci)
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY COLUMN id INT(11);
ALTER TABLE first_table MODIFY COLUMN name TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
