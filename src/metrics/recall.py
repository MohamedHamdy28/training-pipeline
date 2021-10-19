import numpy as np

from metrics import AbstractMetric


class Recall(AbstractMetric):
    def __init__(self):
        super().__init__()

    def get_value(self, confusion_matrix: np.ndarray):
        return np.mean(np.nan_to_num(np.diag(confusion_matrix) / confusion_matrix.sum(axis=1)))