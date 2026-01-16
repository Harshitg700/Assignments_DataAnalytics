#Ques1
--create MATERIALIZED view main_dataset.amount_spend_country_wise as 

Select cst.Country,sum(od.amount) as total_amount_spend
from fact_order od 
inner join dim_customer cst on od.Customer_ID = cst.Customer_ID
inner join dim_shipping shp on od.Customer_ID = shp.Customer_ID
where shp.status = "Pending"
group by 1
order by 2 desc ;

#Ques2 
Select 
od.Customer_ID,
od.item,
count(od.order_id) as total_transactions,
count(*) as total_quantity_sold,
sum(od.amount) as total_amount_spent
from fact_order od 
inner join dim_customer cst on od.Customer_ID = cst.Customer_ID
group by 1 ,2



#Ques3 -- the maximum product purchased for each country 
#onabsoulte--count
Select 
country, item
from(
Select 
country, item, 
RANK() OVER (PARTITION BY country ORDER BY number_of_orders DESC) as rank
from (
Select 
cst.country,od.item,count(od.order_id) as number_of_orders
from fact_order od 
inner join dim_customer cst on od.Customer_ID = cst.Customer_ID
group by 1,2 )cnt
)ranked
where ranked.rank =1 ;

#ontotal--amount 
Select 
country, item
from(
Select 
country, item, 
RANK() OVER (PARTITION BY country ORDER BY order_amt DESC) as rank
from (
Select 
cst.country,od.item,sum(od.amount) as order_amt
from fact_order od 
inner join dim_customer cst on od.Customer_ID = cst.Customer_ID
group by 1,2 )cnt
)ranked
where ranked.rank =1 ;


#Ques4
#most purchased below age30 & most purchased above age30

Select xyz.item,'Item most purchased by cust below 30 yrs age' AS category
from(
Select od.item,count(*)
from fact_order od 
inner join dim_customer cst on od.Customer_ID = cst.Customer_ID
where (cst.age <30)
group by 1 
order by 2 desc 
limit 1)xyz

union all

Select xyz.item,'Item most purchased by cust above 30 yrs age' AS category
from(
Select
od.item,count(*)
from fact_order od 
inner join dim_customer cst on od.Customer_ID = cst.Customer_ID
where (cst.age >30)
group by 1 
order by 2 desc 
limit 1) xyz;

#Ques5
SELECT 
    cst.country,
    COUNT(od.order_id) AS transaction_count,
    SUM(od.amount) AS sales_amount
FROM fact_order od
INNER JOIN dim_customer cst
    ON od.Customer_ID = cst.Customer_ID
GROUP BY cst.country
ORDER BY 
    COUNT(od.order_id) ASC,
    SUM(od.sales_amount) ASC
LIMIT 1;
