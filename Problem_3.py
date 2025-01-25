-- # Problem Name: Display the First Three Rows
-- ## LeetCode Link: https://leetcode.com/problems/display-the-first-three-rows/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
-- 
----
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
