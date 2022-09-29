import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv"
)

new_df = df[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "Country Name",
        "GDP (current US$)",
    ]
]


import matplotlib.pyplot as plt

plt.scatter(
    new_df["Mortality rate, infant (per 1,000 live births)"],
    new_df["GDP (current US$)"],
    alpha=0.5,
)
