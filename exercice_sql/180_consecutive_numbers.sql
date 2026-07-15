-- 180. Consecutive Numbers

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | num         | varchar |
-- +-------------+---------+
-- In SQL, id is the primary key for this table.
-- id is an autoincrement column starting from 1.
 
-- Find all numbers that appear at least three times consecutively.
-- Return the result table in any order.
-- The result format is in the following example.

-- Example 1:

-- Input: 
-- Logs table:
-- +----+-----+
-- | id | num |
-- +----+-----+
-- | 1  | 1   |
-- | 2  | 1   |
-- | 3  | 1   |
-- | 4  | 2   |
-- | 5  | 1   |
-- | 6  | 2   |
-- | 7  | 2   |
-- +----+-----+

-- Output: 
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+
-- Explanation: 1 is the only number that appears consecutively for at least three times.

SELECT  DISTINCT log_a.num AS ConsecutiveNums
FROM Logs AS log_a, Logs AS log_b, Logs AS log_c
WHERE log_a.id + 1 = log_b.id
AND log_b.id + 1 = log_c.id
AND log_a.num = log_b.num
AND log_b.num = log_c.num

-- Finite Incantatem