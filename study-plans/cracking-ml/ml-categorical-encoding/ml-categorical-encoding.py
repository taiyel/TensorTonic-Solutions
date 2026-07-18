import numpy as np

def categorical_encode(data, method="label"):
    """
    Returns: encoded result based on method
    """
    sort_data = sorted(list(set(data)))
    mapping = dict(enumerate(sort_data))
    n = len(mapping)
    reverse_mapping = {v: k for k, v in mapping.items()}
    
    if method == 'label':
        code = [reverse_mapping[x] for x in data]
        return {'encoded':code, 'classes':sort_data}
    else:
        code = []
        for x in data:
            arr = [0]*n
            arr[reverse_mapping[x]] = 1
            code.append(arr)
        return code
        
        
        
    