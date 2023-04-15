drop table orders;

create table Analysis
    (an_id INT
    ,an_name VARCHAR2(255)
    ,an_cost NUMBER
    ,an_price NUMBER
    ,an_group INT
    );

create table Groups
    (gr_id INT
    ,gr_name VARCHAR2(255)
    ,gr_temp VARCHAR2(255)
    );

create table Orders
    (ord_id INT
    ,ord_datetime TIMESTAMP
    ,ord_an int
    );

delete from Groups;
delete from Analysis;
delete from Orders;

insert all
into Groups values (1, 'Groups1','+1..+5')
into Groups values (2, 'Groups2','+10..+15')
into Groups values (3, 'Groups3','-10..-5')
into Analysis values (1, 'Analysis11',100, 500, 1)
into Analysis values (2, 'Analysis12',1000, 1500, 1)
into Analysis values (3, 'Analysis21',20, 700, 2)
into Analysis values (4, 'Analysis22',115, 225, 2)
into Analysis values (5, 'Analysis31',210, 670, 3)
SELECT * FROM dual;


insert into Orders
select level as ord_id
       ,TO_TIMESTAMP(to_char(round(dbms_random.value(2020,2022))) --yyyy
                ||'.'
                ||to_char(round(dbms_random.value(1,3))) --mon
                ||'.'
                ||to_char(round(dbms_random.value(1,28))) --dd
                ||' '
                ||to_char(round(dbms_random.value(0,23))) --hh24
                ||':'
                ||to_char(round(dbms_random.value(0,59))) --mi
                ||':'
                ||to_char(round(dbms_random.value(0,59))) --ss
                , 'YYYY/MM/DD HH24:MI:SS') as ord_datetime
       ,round(dbms_random.value(1,5)) as ord_an
   from dual
connect by level <= 12000;



select * from orders;

--task 1 
--Формулировка: вывести название и цену для всех анализов, которые продавались 5 февраля 2020 и всю следующую неделю.

select a.an_name, a.an_price
from orders o
join analysis a
on o.ord_an = a.an_id
where o.ord_datetime between to_date('05/02/2020', 'dd/mm/yyyy') and to_date('05/02/2020', 'dd/mm/yyyy') + INTERVAL '7' DAY


--task 2
--Формулировка: нарастающим итогом рассчитать, как увеличивалось количество проданных тестов каждый месяц каждого года с разбивкой по группе.



with preptable as
    (select gr_name, extract(month from ord_datetime ) as ord_month, extract(year from ord_datetime ) as ord_year, count(o.ord_an) as count_an
    from orders o
    join analysis a on an_id = ord_an
    join groups g on an_group = gr_id
    group by gr_name, extract(year from ord_datetime ), extract(month from ord_datetime )
    ) 
select ord_year, ord_month, gr_name, coalesce(sum(count_an) over (partition by gr_name order by ord_year, ord_month rows between unbounded preceding and current row), 0) as total_an
from preptable
order by gr_name, ord_year, ord_month

