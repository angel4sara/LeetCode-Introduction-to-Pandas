-- # Problem Name: Rename Columns
-- ## LeetCode Link:https://leetcode.com/problems/rename-columns/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
----
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    new = students.rename(columns = {
        'id' : 'student_id',
        'first' : 'first_name',
        'last' : 'last_name',
        'age'  :  'age_in_years'
    })
    return new
