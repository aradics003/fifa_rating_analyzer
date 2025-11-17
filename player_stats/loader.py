import pandas as pd

class PlayerDataLoader:
    def __init__(self, path):
        self.path = path

    def load(self):
        """loading the dataset"""
        return pd.read_csv(self.path)