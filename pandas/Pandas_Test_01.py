# Project: Pandas_Test_01 - ETH Data Audit
# 1. Time Integrity: Checked for missing hours using .shift() -> Data is 100% clean.
# 2. Volatility: Identified "Flash Crashes" (Price change > 5% in 1 hour).
# 3. Anomaly Detection: Used Rolling Mean & Std (24h window) to find 343 outliers
#    beyond the 3rd standard deviation (3-sigma rule).
# Author: Engineer Ahmad

import pandas as pd

df = pd.read_csv("ETH_1h.csv", parse_dates=["Date"], date_format="%Y-%m-%d %I-%p")

df.sort_values("Date", inplace=True)

df["Time_Delta"] = df["Date"] - df["Date"].shift(1)

df["Time_Delta"].unique()
# done

df["Before_One_Hour"] = df["Close"].shift(1)

df["Flash Crashes"] = (df["Close"] - df["Before_One_Hour"]) / df["Before_One_Hour"]

Flash_Crashes = abs(df["Flash Crashes"]) > 0.05

df.sort_values("Flash Crashes", inplace=True)

Rolling_Mean = df["Close"].rolling(window=24).mean()

df["Rolling Mean"] = Rolling_Mean

new_df = df[["Date", "Close", "Rolling Mean"]]

new_df.set_index("Date", inplace=True)

new_df = new_df.dropna()

Rolling_Std = new_df["Close"].rolling(window=24).std()

new_df["Rolling Std"] = Rolling_Std

new_df = new_df.dropna()

new_df.sort_values("Date", inplace=True)

new_df["Upper_Limit"] = new_df["Rolling Mean"] + (3 * new_df["Rolling Std"])

new_df["Lower_Limit"] = new_df["Rolling Mean"] - (3 * new_df["Rolling Std"])

anomalies = new_df[
    (new_df["Close"] > new_df["Upper_Limit"])
    | (new_df["Close"] < new_df["Lower_Limit"])
]
print(anomalies)
