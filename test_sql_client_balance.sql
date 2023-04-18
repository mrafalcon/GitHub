/*  drop table ClientBalance;
  create table --if not exists 
  ClientBalance (
   client_id int
    , client_name varchar2(255)
    , client_balance_date date
    , client_balance_value int
  );
*/
--delete from ClientBalance;
--delete from FIRM.SYS_LOAD_DOCUMENTS;

insert all
into ClientBalance values (1, 'name11',to_date('01/01/2023','dd/mm/yyyy'),1)
into ClientBalance values (1, 'name11',to_date('01/01/2023','dd/mm/yyyy'),1)
into ClientBalance values (2, 'name12',to_date('02/01/2023','dd/mm/yyyy'),2)
into ClientBalance values (1, 'name11',to_date('01/01/2023','dd/mm/yyyy'),1)
into ClientBalance values (1, 'name11',to_date('01/01/2023','dd/mm/yyyy'),1)
into ClientBalance values (3, 'name13',to_date('03/01/2023','dd/mm/yyyy'),3)
into ClientBalance values (1, 'name11',to_date('01/01/2023','dd/mm/yyyy'),1)
into ClientBalance values (1, 'name11',to_date('01/01/2023','dd/mm/yyyy'),1)
SELECT * FROM dual;



select * from ClientBalance;


delete from ClientBalance
    where rowid not in (
        select rowid from (
            select rowid, row_number() over (partition by client_id, client_name, client_balance_date, client_balance_value order by client_id) as numrow
            from ClientBalance
        )
        where numrow = 1
    );

select * from ClientBalance;


select * from JSON_TABLE()


{"ClientData":["{\"client_id\":\"1\",\"client_name\":\"A\",\"client_balance\":\"02/04/2023\",\"client_balance_value\":\"1\"}","{\"client_id\":\"1\",\"client_name\":\"A\",\"client_balance\":\"02/04/2023\",\"client_balance_value\":\"12\"}","{\"client_id\":\"1\",\"client_name\":\"A\",\"client_balance\":\"02/04/2023\",\"client_balance_value\":\"121\"}","{\"client_id\":\"1\",\"client_name\":\"A\",\"client_balance\":\"13/04/2023\",\"client_balance_value\":\"100\"}","{\"client_id\":\"1\",\"client_name\":\"A\",\"client_balance\":\"17/04/2023\",\"client_balance_value\":\"0\"}","{\"client_id\":\"2\",\"client_name\":\"B\",\"client_balance\":\"17/04/2023\",\"client_balance_value\":\"1000\"}","{\"client_id\":\"2\",\"client_name\":\"B\",\"client_balance\":\"18/04/2023\",\"client_balance_value\":\"0\"}","{\"client_id\":\"2\",\"client_name\":\"B\",\"client_balance\":\"16/04/2023\",\"client_balance_value\":\"0\"}","{\"client_id\":\"2\",\"client_name\":\"B\",\"client_balance\":\"11/04/2023\",\"client_balance_value\":\"1000\"}","{\"client_id\":\"2\",\"client_name\":\"B\",\"client_balance\":\"11/04/2023\",\"client_balance_value\":\"1000\"}","{\"client_id\":\"2\",\"client_name\":\"B\",\"client_balance\":\"11/04/2023\",\"client_balance_value\":\"1000\"}","{\"client_id\":\"2\",\"client_name\":\"B\",\"client_balance\":\"11/04/2023\",\"client_balance_value\":\"1000\"}"]}
