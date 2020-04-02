from typing import List, Tuple

def load_data(path: str) -> List[List[float]]:
    data = []
    r = []
    
    with open(path, 'r') as file:
       for l in file:
        row = l.split()
        if row:
            data.append(
                (row)
            )

    return  data