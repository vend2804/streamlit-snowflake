import _utils

from snowflake.snowpark.functions import call_function, col


session = _utils.get_connection()

# independent query

avgSales = (session
            .table("employees")
            .select("department", "salary")
            .group_by("department")
            .agg({"salary": "avg"})
            .select("Department", call_function("floor", col("AVG(SALARY)")).alias("avg_sal"))
            .sort("Department")
            )

#avgSales.show()

managers = (session.table("Employees")
            .select("Department", "Employee_Name", "Salary")
            .filter(col("Job") == "MANAGER")
            .sort("Department", "Employee_Name")
        )
#managers.show()
#print(managers.collect())

(managers.join(avgSales,managers.department == avgSales.department)
        .select(managers.department.alias("Department"),
                managers.employee_name,
                managers.salary,
                (managers.salary + (0.1 * avgSales.avg_sal)).alias("new_sal")
                )
                .show()
        )
            
        