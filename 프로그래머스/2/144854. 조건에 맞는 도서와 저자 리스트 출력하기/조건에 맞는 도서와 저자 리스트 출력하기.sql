-- 코드를 입력하세요
SELECT b.book_id, a.author_name, DATE_FORMAT(b.published_date, '%Y-%m-%d')
FROM BOOK as b
INNER JOIN AUTHOR as a ON a.author_id = b.author_id
WHERE b.category = '경제'
ORDER BY published_date ASC;