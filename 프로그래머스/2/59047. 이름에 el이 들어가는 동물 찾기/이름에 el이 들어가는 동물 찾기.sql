-- 코드를 입력하세요
SELECT animal_id, name
FROM animal_ins
WHERE animal_type = 'DOG' 
AND name LIKE '%el%' or '%EL%' or '%eL%' or '%El%'
ORDER BY name;