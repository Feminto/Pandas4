import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unq_sal = sorted(employee['salary'].drop_duplicates(), reverse= True)

    #invalid cases
    if len(unq_sal) < N or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})

    nth_sal = unq_sal[N-1] # Nth highest will be calculated as N-1 since the Indexing starts at 0. Eg. 2nd hishest will be at Index 1
    return pd.DataFrame({f'getNthHighestSalary({N})':[nth_sal]})