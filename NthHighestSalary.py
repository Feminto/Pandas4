import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unq_sal = sorted(employee['salary'].drop_duplicates(), reverse= True)

    #invalid cases
    if len(unq_sal) < N or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})

    nth_sal = unq_sal[N-1] # Nth highest will be calculated as N-1 since the Indexing starts at 0. Eg. 2nd hishest will be at Index 1
    return pd.DataFrame({f'getNthHighestSalary({N})':[nth_sal]})


# Method 2
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    r_set = set()
    for i in range(len(employee)):
        sal = employee['salary'][i]
        r_set.add(sal)

    # print(r_set)
    result = []
    for i in r_set:
        result.append(i)

    unq_sal = sorted(result, reverse = True)

    #invalid cases
    if len(unq_sal) < N or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})

    nth_sal = unq_sal[N-1] # Nth highest will be calculated as N-1 since the Indexing starts at 0. Eg. 2nd hishest will be at Index 1
    return pd.DataFrame({f'getNthHighestSalary({N})':[nth_sal]})