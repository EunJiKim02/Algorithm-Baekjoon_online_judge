-- 코드를 입력하세요
WITH AVAIL_CAR AS (SELECT CAR_ID, '대여중' AS AVAILABILITY
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE TO_DATE('2022-10-16', 'YYYY-MM-DD') BETWEEN START_DATE AND END_DATE)
    
SELECT C.CAR_ID, CASE 
    WHEN A.AVAILABILITY IS NULL THEN '대여 가능'
    ELSE A.AVAILABILITY
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY C
    LEFT OUTER JOIN AVAIL_CAR A ON C.CAR_ID = A.CAR_ID
GROUP BY C.CAR_ID, A.AVAILABILITY
ORDER BY CAR_ID DESC;