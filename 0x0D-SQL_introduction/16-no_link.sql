-- List all records of second_table
-- Records are ordered by descending
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
