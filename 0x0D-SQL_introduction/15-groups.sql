-- Number of of records with the same score
SELECT score, count(*) as number FROM second_table GROUP BY score;
