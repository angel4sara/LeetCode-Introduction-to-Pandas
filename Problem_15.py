-- # Problem Name: Method Chaining
-- ## LeetCode Link: https://leetcode.com/problems/method-chaining/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
----
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    result = animals[animals["weight"] > 100].sort_values(by="weight", ascending=False)[["name"]]
    return result
