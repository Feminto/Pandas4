#Method 1
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unq_sal = sorted(employee['salary'].drop_duplicates(), reverse= True)

    #invalid cases
    if len(unq_sal) < N or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    else:
        nth_sal = unq_sal[N-1] # Nth highest will be calculated as N-1 since the Indexing starts at 0. Eg. 2nd hishest will be at Index 1
    
    # if invalid case is evaluated later, it causes Runtime Error:
    # nth_sal will try to access an index that might not exist in unq_sal. 
    # If N is invalid (e.g., N > len(unq_sal) or N <= 0), then: unq_sal[N-1] throws an IndexError.
    
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