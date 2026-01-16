
-- Duplicate order IDs
SELECT
   order_id,
   count(*) AS duplicate_count
 FROM order_tbl
 GROUP BY order_id
 HAVING COUNT(*) > 1;

-- Duplicate Customer_ID
Select 
Customer_ID,
count(*) as duplicate_count
from customer_tbl
group by Customer_ID
having count(*) > 1

--Null Names in customer tbl
Select 
count(*)
sum(case when First is null or Last is null  then 1 else 0 end)as null_first_or_last
from customer_tbl