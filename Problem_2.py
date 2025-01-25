-- # Problem Name: Get the Size of a DataFrame
-- ## LeetCode Link: https://leetcode.com/problems/get-the-size-of-a-dataframe/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
----
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
   return(list(players.shape))
