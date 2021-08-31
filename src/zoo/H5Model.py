import pandas as pd


class H5Model:
    def __init__(self, h5_filename) -> None:
        self.h5_filename = h5_filename
        self.df = pd.read_hdf(h5_filename, key="data", mode="r")
