import math

def distance_metric(x, y, metric, p=2):
    """
    Compute the distance between vectors x and y using the specified metric.
    Returns: float rounded to 4 decimal places
    """
    if metric == "euclidean":
        result = math.sqrt(sum((xi - yi) ** 2 for xi, yi in zip(x, y)))

    elif metric == "manhattan":
        result = sum(abs(xi - yi) for xi, yi in zip(x, y))

    elif metric == "cosine":
        dot = sum(xi * yi for xi, yi in zip(x, y))
        norm_x = math.sqrt(sum(xi ** 2 for xi in x))
        norm_y = math.sqrt(sum(yi ** 2 for yi in y))
        if norm_x == 0 or norm_y == 0:
            return 0.0
        result = 1 - dot / (norm_x * norm_y)

    elif metric == "chebyshev":
        result = max(abs(xi - yi) for xi, yi in zip(x, y))

    elif metric == "minkowski":
        result = sum(abs(xi - yi) ** p for xi, yi in zip(x, y)) ** (1 / p)

    else:
        raise ValueError(f"Unknown metric: {metric}")

    return round(result, 4)


    