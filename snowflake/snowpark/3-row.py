# write the same code from 3-row.py using snowpark 
import json
import _utils

session = _utils.get_connection()

def getNewSales(session):
    
    # get average salary in a department 
    def getAvgSal(dept: str) -> float:
        query = ("select floor(avg(salary))"
                 + f"from employees where department = '{dept}'")
        return session.sql(query).collect()[0][0]
    
    # get managers with current and projected salaries 
    def getManagers():
        managers =[]
        query = """
            select department, employee_name, salary
            from employees where  job = 'MANAGER'
            order by department, employee_name
        """
        for row in session.sql(query).collect():
            managers.append({
                "department": str(row[0]),
                "employee_name": str(row[1]),
                "salary": int(row[2])
            })
        return managers


    # get managers with current projected salary
    managers = getManagers()

    for manager in managers:
        manager["new_sal"] = (manager["salary"] + (0.1 * getAvgSal(manager["department"])))
    return json.dumps(managers, indent=2)

sals = getNewSales(session)
print(sals)
session.close()
