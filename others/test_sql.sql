--EXPLAIN PLAN FOR
select distinct JOB_ID, sum(SALARY) from EMP_DETAILS_VIEW
where JOB_ID like 'ST_%'
group by JOB_ID
having sum(salary) >= 5000
--select job_id, salary, trunc(salary, -3), round(salary, -3) from EMP_DETAILS_VIEW
--where JOB_ID like 'ST_%'