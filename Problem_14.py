-- # Problem Name: Reshape Data: Melt
-- ## LeetCode Link: https://leetcode.com/problems/reshape-data-melt/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
----
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    df_long = report.melt(id_vars=["product"], 
                  var_name="quarter", 
                  value_name="sales")
    return df_long
