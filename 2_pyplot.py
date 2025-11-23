import matplotlib.pyplot as plt
import pandas as pd


date = pd.date_range(start="2025-10-01", freq="D", periods=8)
plt.plot(
    date,
    [23, 17, 17, 16, 15, 14, 17, 20],
    label="day temperature",
    linestyle="--",
    color="#FF5733",
    linewidth=2,
    marker="D",
)
plt.plot(
    date,
    [19, 11, 16, 11, 10, 10, 11, 16],
    label="night temperature",
    linestyle=":",
    color="#061358",
    linewidth=2,
    marker="^",
)
plt.ylim(0, 25)
plt.xlabel("Date", fontsize="small", color="midnightblue")
plt.ylabel("Temperature", fontsize="small", color="midnightblue")
plt.title("Cornella de Llobregat, 08940", fontsize=15)
plt.text(
    date[0],
    2,
    "El otoño está siendo bastante cálido",
    color="darkred",
    fontsize=8,
)
plt.legend()
plt.grid()
plt.show()
