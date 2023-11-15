-- Convert a database, table and column to UTF8(utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci;
ALTER TABLE second_table CONVERT TO CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci;
ALTER TABLE second_table MODIFY COLUMN name TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
