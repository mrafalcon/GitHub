--select * from countries

/*
CREATE OR REPLACE PACKAGE aa_pkg AUTHID DEFINER IS
  TYPE aa_type IS TABLE OF INTEGER INDEX BY VARCHAR2(15);
END;
/
CREATE OR REPLACE PROCEDURE print_aa (
  aa aa_pkg.aa_type
) AUTHID DEFINER IS
  i  VARCHAR2(15);
BEGIN
  i := aa.FIRST;
 
  WHILE i IS NOT NULL LOOP
    DBMS_OUTPUT.PUT_LINE (aa(i) || '  ' || i);
    i := aa.NEXT(i);
  END LOOP;
END;
/
DECLARE
  aa_var  aa_pkg.aa_type;
BEGIN
  aa_var('zero') := 0;
  aa_var('one') := 1;
  aa_var('two') := 2;
  print_aa(aa_var);
END;
/
*/

--SELECT lpad(' ', 3*level)||d.EMPLOYEE_ID as Tree


/*

*/

--drop package MY_FIRST_PACKAGE;

create or replace package my_package AS --спецификация --константы, переменные, курсоры
--  function my_test_func (val_in IN int) return int;
  procedure my_test_proc (val_out number); --лучше использовать numeric
  procedure ierarh_proc (lvl number);
end my_package;


create or replace package body my_package AS --тело
  function my_test_func (val_in IN number) return number is
    val1 number;
    error_type exception;
      begin
      val1 := 0;
      if (val_in < 0 or val_in <> round(val_in, 0)) then 
        raise error_type;
      end if;
      for i IN 1 .. val_in
        loop 
        val1 := (val1 + i) * 2;
        end loop;
      return val1;
    exception
      when error_type then
        DBMS_OUTPUT.PUT_LINE ('Function: Type error');
      when others then
        DBMS_OUTPUT.PUT_LINE ('Function: Unexpected error');
  end my_test_func;

  procedure my_test_proc (val_out number) is
    error_type exception;
    begin
      if (val_out < 0 or val_out <> round(val_out, 0) ) then 
        raise error_type;
      end if;
      dbms_output.put_line('Running the test "my_package" with value = '|| val_out || ' and result = '||my_test_func (val_out)); -- вначале взять в какую-то переменную, а потом в output
    exception
      when error_type then
        DBMS_OUTPUT.PUT_LINE ('Procedure my_test_proc: Type error');
      when others then
        DBMS_OUTPUT.PUT_LINE ('Unexpected error');
  end my_test_proc;

  procedure ierarh_proc (lvl number) is
    error_type exception;
    c_lvl varchar2(255);
    cursor c1 IS
      SELECT SYS_CONNECT_BY_PATH(d.EMPLOYEE_ID, '/') as Path
        from EMPLOYEES d
        where level = lvl
        start with d.MANAGER_ID is null
        connect by prior d.EMPLOYEE_ID = d.MANAGER_ID;
    begin
      if (lvl < 0 or lvl <> round(lvl, 0)) then 
        raise error_type;
      end if;
      open c1;
      loop
      fetch c1 into c_lvl;
        exit when c1%notfound;
        DBMS_OUTPUT.PUT_LINE ('Current level-path: '||c_lvl); --на данном этапе разработки не требуется что-то дополнительное
      end loop;
      close c1;
    
    exception
      when error_type then
        DBMS_OUTPUT.PUT_LINE ('Procedure ierarh_proc: Type error');
      when others then
        DBMS_OUTPUT.PUT_LINE ('Unexpected error');
    end ierarh_proc;
end my_package;




--select my_package.my_test_func (2) from dual;
begin
my_package.my_test_proc (-2);
my_package.ierarh_proc (4.1);
end;

