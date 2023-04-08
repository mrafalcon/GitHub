--создание схем org и firm
/*
--conn.SYSTEM/oracle;

create user ORG identified by org;

GRANT create session TO ORG;
GRANT create table TO ORG;
GRANT create view TO ORG;
GRANT create any trigger TO ORG;
GRANT create any procedure TO ORG;
GRANT create sequence TO ORG;
GRANT create synonym TO ORG;
alter user ORG quota unlimited on users;


create user FIRM identified by firm;

GRANT create session TO FIRM;
GRANT create table TO FIRM;
GRANT create view TO FIRM;
GRANT create any trigger TO FIRM;
GRANT create any procedure TO FIRM;
GRANT create sequence TO FIRM;
GRANT create synonym TO FIRM;
alter user FIRM quota unlimited on users;

*/

--создание таблиц SYS_LOAD_DOCUMENTS для org и firm
/*
--connect ORG/org;

create schema AUTHORIZATION org
  create table --if not exists 
  SYS_LOAD_DOCUMENTS (
   FILE_ID int
    , FILENAME varchar2(255)
    , FILE_EXT varchar2(255)
    , FILE_SIZE int
    , CREATOR varchar2(255)
    , DATE_MODIFY date
    , OBJECT_ID int
    , "COMMENT" varchar2(255)
    , PK_TABLE_ID  int
, PRIMARY KEY (FILE_ID)
  );

--connect FIRM/firm;
create schema AUTHORIZATION firm
  create table --if not exists 
  SYS_LOAD_DOCUMENTS (
   FILE_ID int
    , FILENAME varchar2(255)
    , FILE_EXT varchar2(255)
    , FILE_SIZE int
    , CREATOR varchar2(255)
    , DATE_MODIFY date
    , OBJECT_ID int
    , "COMMENT" varchar2(255)
    , PK_TABLE_ID  int
, PRIMARY KEY (FILE_ID)
  );



*/

-- выдача привелегий на таблицах для пользователя HR
/*

--connect SYSTEM/oracle;

grant ALL on FIRM.SYS_LOAD_DOCUMENTS to HR;
grant ALL on ORG.SYS_LOAD_DOCUMENTS to HR;
*/

--connect HR/oracle;

delete from ORG.SYS_LOAD_DOCUMENTS;
delete from FIRM.SYS_LOAD_DOCUMENTS;

insert all
into ORG.SYS_LOAD_DOCUMENTS values (1, 'name11','1',1,'1',to_date('01/01/2023','dd/mm/yyyy'),1,'comm11',1)
into ORG.SYS_LOAD_DOCUMENTS values (2, 'name12','1',1,'1',to_date('02/01/2023','dd/mm/yyyy'),1,'comm12',1)
into ORG.SYS_LOAD_DOCUMENTS values (7, 'name17','1',1,'1',to_date('07/01/2023','dd/mm/yyyy'),1,'comm17',1)
into ORG.SYS_LOAD_DOCUMENTS values (8, 'name18','1',1,'1',to_date('08/01/2023','dd/mm/yyyy'),1,'comm18',1)
into ORG.SYS_LOAD_DOCUMENTS values (11, 'name111','1',1,'1',to_date('11/01/2023','dd/mm/yyyy'),1,'comm111',1)
into ORG.SYS_LOAD_DOCUMENTS values (12, 'name112','1',1,'1',to_date('12/01/2023','dd/mm/yyyy'),1,'comm112',1)
SELECT * FROM dual;

insert all
into FIRM.SYS_LOAD_DOCUMENTS values (5, 'name52','1',1,'1',to_date('05/02/2023','dd/mm/yyyy'),1,'comm25',1)
into FIRM.SYS_LOAD_DOCUMENTS values (2, 'name22','1',1,'1',to_date('02/02/2023','dd/mm/yyyy'),1,'comm22',1)
into FIRM.SYS_LOAD_DOCUMENTS values (3, 'name23','1',1,'1',to_date('03/02/2023','dd/mm/yyyy'),1,'comm23',1)
into FIRM.SYS_LOAD_DOCUMENTS values (4, 'name24','1',1,'1',to_date('04/02/2023','dd/mm/yyyy'),1,'comm24',1)
into FIRM.SYS_LOAD_DOCUMENTS values (8, 'name38','1',1,'1',to_date('08/03/2023','dd/mm/yyyy'),1,'comm38',1)
into FIRM.SYS_LOAD_DOCUMENTS values (9, 'name39','1',1,'1',to_date('09/03/2023','dd/mm/yyyy'),1,'comm39',1)
SELECT * FROM dual;


-- решение 1 - шаг 1 - удаление из таблицы ORG.SYS_LOAD_DOCUMENTS
/*

-- delete
delete from ORG.SYS_LOAD_DOCUMENTS
where (file_id) in (
select (o.file_id)
from ORG.SYS_LOAD_DOCUMENTS o
left  join  FIRM.SYS_LOAD_DOCUMENTS f
on (f.FILE_ID) = (o.FILE_ID)
where (f.FILE_ID) is NULL
) ;

*/

-- решение 1 - шаг 2 - добавление и обновление строк - вариант 1 
/*
insert into  ORG.SYS_LOAD_DOCUMENTS 
select f.* 
from FIRM.SYS_LOAD_DOCUMENTS f
left  join ORG.SYS_LOAD_DOCUMENTS o
on (f.FILE_ID) = (o.FILE_ID)
where (o.FILE_ID) is NULL; -- add

update ORG.SYS_LOAD_DOCUMENTS o1
set (file_id, filename, file_ext, file_size, creator, date_modify, object_id, "COMMENT", pk_table_id) = (select f.* 
from FIRM.SYS_LOAD_DOCUMENTS f
where (f.FILE_ID) = (o1.FILE_ID)
)
where exists (
select 1 
from FIRM.SYS_LOAD_DOCUMENTS f
where (f.FILE_ID) = (o1.FILE_ID)
); --update
*/

-- решение 1 - шаг 2 - добавление и обновление строк - вариант 2 
/*
MERGE INTO ORG.SYS_LOAD_DOCUMENTS o
    using (select * from FIRM.SYS_LOAD_DOCUMENTS) f
    on ((f.FILE_ID) = (o.FILE_ID))
    when matched THEN 
        update set o.filename = f.filename, o.file_ext = f.file_ext, 
            o.file_size = f.file_size, o.creator = f.creator, 
            o.date_modify = f.date_modify, o.object_id = f.object_id, 
            o."COMMENT" = f."COMMENT", o.pk_table_id = f.pk_table_id

    when not matched then insert (o.file_id, o.filename, o.file_ext, o.file_size, o.creator, o.date_modify, o.object_id, o."COMMENT", o.pk_table_id)
    values (f.file_id, f.filename, f.file_ext, f.file_size, f.creator, f.date_modify, f.object_id, f."COMMENT", f.pk_table_id);

*/

-- решение 2 - шаг 1 - анализ необходимости выполнения действий - вариант 1
/*
select file_id, filename, file_ext, file_size, creator, date_modify, object_id, "COMMENT", pk_table_id, 
  case 
        when file_id in (
        select o.file_id from ORG.SYS_LOAD_DOCUMENTS o
        join FIRM.SYS_LOAD_DOCUMENTS f
        on o.file_id = f.FILE_ID
      ) and file_level = 'org' then '0'                       -- row for update in "org"
        
        when file_id in (
        select o.file_id from ORG.SYS_LOAD_DOCUMENTS o
        join FIRM.SYS_LOAD_DOCUMENTS f
        on o.file_id = f.FILE_ID
      ) and file_level = 'firm' then '1'                      -- updated row in "firm" 
        
        when file_id in (
        select f.file_id from FIRM.SYS_LOAD_DOCUMENTS f
        left join ORG.SYS_LOAD_DOCUMENTS o
        on (f.FILE_ID) = (o.FILE_ID)
        where (o.FILE_ID) is NULL
      ) and file_level = 'firm' then '2'                      -- add row to "org"
      
      else '-1'                                               -- delete row from "org"
  end as action_type
from (select file_id, filename, file_ext, file_size, creator, date_modify, object_id, "COMMENT", pk_table_id, 'org' as file_level from ORG.SYS_LOAD_DOCUMENTS
union all
select file_id, filename, file_ext, file_size, creator, date_modify, object_id, "COMMENT", pk_table_id, 'firm' as file_level from FIRM.SYS_LOAD_DOCUMENTS)
*/
--

-- решение 2 - шаг 1 - анализ необходимости выполнения действий - вариант 2

create or replace view current_union as 
select file_id, filename, file_ext, file_size, creator, date_modify, object_id, "COMMENT", pk_table_id,         
    case
      when file_id in (
        select firm from (select f.file_id as firm
from FIRM.SYS_LOAD_DOCUMENTS f
join ORG.SYS_LOAD_DOCUMENTS o
on f.FILE_ID = o.FILE_ID)
      ) then 'need_to_update'                        --need to update from 'firm'
    else 'delete'                           --need to delete from 'org'
    end as action_type
from ORG.SYS_LOAD_DOCUMENTS

union all

select file_id, filename, file_ext, file_size, creator, date_modify, object_id, "COMMENT", pk_table_id, 
case 
        when file_id in (
        select firm from (select f.file_id as firm
from FIRM.SYS_LOAD_DOCUMENTS f
join ORG.SYS_LOAD_DOCUMENTS o
on f.FILE_ID = o.FILE_ID)
      ) then 'new_update'                      -- updated row
      else 'add'                        -- to add row
  end as action_type  
from FIRM.SYS_LOAD_DOCUMENTS;


-- решение 2 - шаг 2 - выполнение указанных действий

select * from current_union

drop table hr.tbl_b;
drop table hr.tbl_c;
create table hr.tbl_c
(id int, name varchar2(255), d TIMESTAMP default sysdate);
insert into hr.tbl_c (id, name) values (1, 'A');


select * from hr.tbl_c;

DECLARE
c_id FIRM.SYS_LOAD_DOCUMENTS.file_id%type;
CURSOR c1
IS 
select file_id
from FIRM.SYS_LOAD_DOCUMENTS;
begin 
  open c1;
  loop
  fetch c1 into c_id;
    exit when c1%notfound;
    insert into hr.tbl_c (id, name) values (c_id, c_id);
    DBMS_OUTPUT.PUT_LINE ('Current ID: '||c_id);
--    commit;
  end loop;
  close c1;
  commit;
end;

select * from hr.tbl_c;


select * from (select creator, MAX(DATE_MODIFY) from firm.SYS_LOAD_DOCUMENTS group by creator) where rownum = 1