import _utils

session = _utils.get_connection()

# get managers with projected 10% raise of average department 
query = """
with q1 as (select department , floor(avg(salary)) as avg_sal 
from employees
group by department
order by department)

select e.department, e.employee_name,e.salary , q1.avg_sal,
e.salary + (0.1 * q1.avg_sal) as new_sal
from employees  e
join q1 on q1.department = e.department
where job ='MANAGER'
order by e.department, employee_name;
"""


df= session.sql(query).toPandas()
print(df)

#df = session.table("employees").filter("job_id = 'SA_MAN'").join(session.table("departments"), on="department_id").select("employees.first_name", "employees.last_name", "employees.salary", "departments.department_name").toPandas()
#print(df)
session.close()
