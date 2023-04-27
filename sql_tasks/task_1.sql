/* Есть строка с перечисленными ид через зпт. Например, 5223, 5473, 5474, 5475, 5227, 5477, 5285, 5478, 5398, 5509

Второй строкой имеем 5477, 5474

Надо, из первой строки удалить то, что есть во второй строке и вернуть результат в виде строки.
*/


with string1 as

(SELECT REGEXP_SUBSTR(str, '(\d+)', 1, LEVEL) as val1
  FROM (SELECT '5223, 5473, 5474, 5475, 5227, 5477, 5285, 5478, 5398, 5509' str FROM DUAL)
  CONNECT BY REGEXP_SUBSTR(str, '(\d+)', 1, LEVEL) IS NOT NULL
),

string2 as

(SELECT REGEXP_SUBSTR(str, '(\d+)', 1, LEVEL) as val2
  FROM (SELECT '5474, 5477' str FROM DUAL)
  CONNECT BY REGEXP_SUBSTR(str, '(\d+)', 1, LEVEL) IS NOT NULL
),

result_table as 

(select val1 as val
from string1 s1
left join string2 s2
on s1.val1 = s2.val2
where s2.val2 is null)

	
SELECT LISTAGG(val, ', ') WITHIN GROUP (ORDER BY val) "Unique_value"
FROM result_table;