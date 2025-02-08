-- # Problem Name: Modify Columns
-- ## LeetCode Link: https://leetcode.com/problems/modify-columns/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
----
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] =employees['salary'] *2 
    return employees
