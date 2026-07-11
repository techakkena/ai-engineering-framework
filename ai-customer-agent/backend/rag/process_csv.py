import pandas as pd


def process_csv(file_path):

    df = pd.read_csv(file_path)

    return df.to_string()
