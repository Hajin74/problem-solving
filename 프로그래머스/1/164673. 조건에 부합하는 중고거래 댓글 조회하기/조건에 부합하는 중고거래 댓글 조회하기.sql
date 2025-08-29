-- 코드를 입력하세요
# SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, date_format(r.created_date, '%Y-%m-%d') as CREATED_DATE
# from used_goods_board b
# inner join used_goods_reply r on b.board_id = r.board_id
# -- where r.created_date >= '2022-10-01' and r.created_date < '2022-11-01'
# where year(r.created_date) = 2022 and month(r.created_date) = 10
# order by created_date asc, TITLE asc

SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') CREATED_DATE
from USED_GOODS_BOARD B 
inner join USED_GOODS_REPLY R on B.BOARD_ID = R.BOARD_ID
where B.CREATED_DATE LIKE '2022-10%'
order by CREATED_DATE asc, TITLE asc;