import streamlit as st
import requests
from time import sleep
import pandas as pd

placeholder0 = st.empty()
placeholder = st.empty()
placeholder2 = st.empty()
placeholder0.title("Callviz - Remote Monitor Callback Visualizer")

def to_df(data):
    """
        Convert the dictionary into a pandas dataframe that streamlit can plot
    :param data: Dict
    :return: Pandas Dataframe
    """

    dict = {}
    for item in data:
        dict[item["epoch"]] = [value for value in item.values()][1:]
    df = pd.DataFrame.from_dict(dict, orient="index", columns=["loss", "accuracy", "val_loss", "val_accuracy", "lr"])
    return df

def main():
    while True:
        response = requests.get('http://localhost:5000/get_info')
        data = response.json()
        df = to_df(data)
        df.index.name = "Epoch"
        placeholder.line_chart(df)
        placeholder2.write(df.iloc[:-1,:])
        sleep(1)

if __name__ == '__main__':
    main()

