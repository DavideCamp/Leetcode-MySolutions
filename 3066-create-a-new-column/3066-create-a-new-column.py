import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    new_df = employees
    df = new_df.insert(2, "bonus", [s*2 for s in employees['salary']])
    return new_df