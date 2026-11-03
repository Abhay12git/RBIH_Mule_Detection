import numpy as np

def recall_at_k(
    y_true,
    y_scores,
    k
):

    idx = np.argsort(
        y_scores
    )[::-1][:k]

    selected = y_true.iloc[idx]

    recalled = selected.sum()

    total_frauds = y_true.sum()

    return recalled / total_frauds