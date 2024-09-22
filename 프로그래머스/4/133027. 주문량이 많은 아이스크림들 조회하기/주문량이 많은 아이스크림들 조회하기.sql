-- 코드를 입력하세요
SELECT f.flavor
FROM  first_half f
JOIN july j
ON f.flavor = j.flavor
GROUP  BY j.flavor
ORDER  BY (f.total_order + SUM(j.total_order) ) DESC
LIMIT  3