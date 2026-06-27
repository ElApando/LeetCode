-- 175. Combine Two Tables
-- +-------------+---------+
-- | Column Name | Type |
-- +-------------+---------+
-- | personId | int |
-- | lastName | varchar |
-- | firstName | varchar |
-- +-------------+---------+
-- personId is the primary key (column WITH unique values) for this table.
-- This TABLE contains information about the ID of some persons AND their first AND last names. 
-- Table: Address 
-- +-------------+---------+
-- | Column Name | Type |
-- +-------------+---------+
-- | addressId | int |
-- | personId | int |
-- | city | varchar |
-- | state | varchar |
-- +-------------+---------+
-- addressId is the primary key (column WITH unique values) for this table.
-- Each row of this TABLE contains information about the city AND state of one person WITH ID = PersonId. 
-- Write a solution to report the first name, last name, city, AND state of each person IN the Person table. If the address of a personId is not present IN the Address table, report null instead. 
-- Return the result TABLE IN any order. 
-- The result format is IN the following example. 
-- Example 1: 
-- Input:
-- Person table:
-- +----------+----------+-----------+
-- | personId | lastName | firstName |
-- +----------+----------+-----------+
-- | 1 | Wang | Allen |
-- | 2 | Alice | Bob |
-- +----------+----------+-----------+
-- Address table:
-- +-----------+----------+---------------+------------+
-- | addressId | personId | city | state |
-- +-----------+----------+---------------+------------+
-- | 1 | 2 | New York City | New York |
-- | 2 | 3 | Leetcode | California |
-- +-----------+----------+---------------+------------+
-- Output:
-- +-----------+----------+---------------+----------+
-- | firstName | lastName | city | state |
-- +-----------+----------+---------------+----------+
-- | Allen | Wang | Null | Null |
-- | Bob | Alice | New York City | New York |
-- +-----------+----------+---------------+----------+
-- Explanation:
-- There is no address IN the address TABLE for the personId = 1 so we return null IN their city AND state.
-- addressId = 1 contains information about the address of personId = 2.
-- 

SELECT  p.firstName
       ,p.LastName
       ,a.city
       ,a.state
FROM Person AS p
LEFT JOIN Address AS a
ON p.personID = a.personID;

-- Finite Incantatem
