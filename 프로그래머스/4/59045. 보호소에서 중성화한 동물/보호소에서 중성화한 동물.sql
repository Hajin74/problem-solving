-- 코드를 입력하세요
SELECT i.animal_id, i.animal_type, i.name
FROM animal_ins i
JOIN animal_outs o
ON i.animal_id = o.animal_id
WHERE i.sex_upon_intake REGEXP 'Intact'
AND o.sex_upon_outcome REGEXP 'Spayed|Neutered'
ORDER BY i.animal_id ASC;
