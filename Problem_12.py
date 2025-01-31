-- # Problem Name: Reshape Data: Concatenate
-- ## LeetCode Link: https://leetcode.com/problems/reshape-data-concatenate/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
--
----
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df3 = pd.concat([df1, df2])
    return df3
