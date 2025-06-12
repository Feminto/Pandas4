import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unq_sal = sorted(employee['salary'].drop_duplicates(), reverse = True)
    
    #invalid cases
    if len(unq_sal) < 2:
        return pd.DataFrame({'SecondHighestSalary':[None]})

    second_sal = unq_sal[1] # 2nd highest is at Index 1
    return pd.DataFrame({'SecondHighestSalary':[second_sal]})