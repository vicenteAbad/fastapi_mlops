from os import path
from typing import List

import torch


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class InferenceClassifier(metaclass=SingletonMeta):
    def __init__(self):
        dirname = path.dirname(__file__)
        pytorch_model_path = path.join(dirname, "trained_models/doubleit_model.pt")
        self.ts = torch.jit.load(pytorch_model_path)

    def predict(self, input_data: List[int]):
        input_data_tensor = xs = torch.as_tensor(input_data)
        probas = self.ts(input_data_tensor).tolist()
        return probas
