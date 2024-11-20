import _utils

conn = _utils.get_connection()

# get managers with projected 10% riase of average per department 
#cur = conn.cursor()
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
cur = conn.cursor()
cur.execute(query)
df = cur.fetch_pandas_all()
print(df)
cur.close()
conn.close()
