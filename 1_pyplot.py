import matplotlib.pyplot as plt
import pandas as pd

# date = pd.date_range(start="2021-09-01", freq="D", periods=8)
# plt.plot(date, [23, 17, 17, 16, 15, 14, 17, 20])
# plt.show()


date = pd.date_range(start="2025-10-01", freq="D", periods=7)
fig, axs = plt.subplots()
axs.plot(
    date,
    [23, 17, 17, 16, 15, 14, 17],
    color="red",
    linestyle=":",
    label="day temperature",
)
axs.plot(
    date,
    [19, 11, 16, 11, 10, 10, 11],
    color="blue",
    linestyle="--",
    label="night temperature",
)
plt.xlabel("Date", fontsize="small", color="midnightblue")
plt.ylabel("Temperature", fontsize="small", color="midnightblue")
plt.title("Temperature in Cornella de Llobregat", fontsize=15)
plt.text(
    date[0],
    10,
    "El otoño está siendo bastante cálido este año.",
    color="darkred",
    fontsize=8,
)
plt.legend()
plt.show()
