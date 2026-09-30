# Write your MySQL query statement below
SELECT w2.id FROM Weather w2
JOIN Weather w1
ON w2.recordDate=DATE_ADD(w1.recordDate,INTERVAL 1 DAY)
WHERE w1.temperature<w2.temperature;
