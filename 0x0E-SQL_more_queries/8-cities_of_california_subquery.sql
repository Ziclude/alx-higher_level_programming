-- List all CA cities in database
-- Ordered by ascending id
SELECT id, name
FROM cities
WHERE state_id IN
(SELECT id
FROM states
WHERE name = "California")
ORDER BY id;
