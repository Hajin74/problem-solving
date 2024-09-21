-- 코드를 입력하세요
SELECT SUBSTRING(product_code, 1, 2) as category, count(*) as products
FROM product
GROUP BY category
ORDER By category