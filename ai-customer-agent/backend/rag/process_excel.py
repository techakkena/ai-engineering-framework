import pandas as pd


def process_excel(file_path):

    df = pd.read_excel(file_path)

    text = df.to_string()

    return text
