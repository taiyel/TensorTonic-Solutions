import numpy as np

def feature_scale(X, method="minmax"):
    """
    Returns: 2D list of scaled values
    """
    X=np.asarray(X,dtype=float)
    
    if method == "minmax":
        for col in range(len(X[0])):
            min_x = np.min(X[:,col])
            max_x = np.max(X[:,col])
            if max_x == min_x:
                X[:, col] = 0.0
            else:
                X[:,col] = (X[:,col] - min_x)/(max_x-min_x)
    else:
        for col in range(len(X[0])):
            mean_x = np.mean(X[:,col])
            std_x = np.std(X[:,col])
            if std_x == 0:
                X[:,col] = 0.0
            else:
                X[:,col] = (X[:,col] - mean_x)/std_x
    return X