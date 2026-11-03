import matplotlib.pyplot as plt
import numpy as np

year = np.array([2022, 2023, 2024, 2025, 2026])
book_sales = np.array([1000, 2500, 1500, 1800, 800])
electronic_sales = np.array([500, 1200, 800, 1500, 1800])
grosery_sales = np.array([1500, 1800, 800, 2000, 1200])
food_sales = np.array([1800, 2500, 2000, 2200, 900])

line_style = dict(marker=".",
                  markerfacecolor="red",
                  markersize="20",
                  markeredgecolor="red",
                  linewidth="2",
                  linestyle="solid")

plt.plot(year, book_sales, color="gray", **line_style)
plt.plot(year, electronic_sales, color="blue", **line_style)
plt.plot(year, grosery_sales, color="green", **line_style)
plt.plot(year, food_sales, color="orange", **line_style)

plt.tick_params(axis="both",
                color="#1dcaf5")
plt.title("Year Sales Data", fontsize="20",
          family="Arial",
          color="#0e298c")
plt.xlabel("Year", fontsize="20",
           family="Arial",
           color="#1544ed")
plt.ylabel("Sales Report", fontsize="20",
           family="Arial",
           color="#1544ed")

plt.xticks(year)
plt.subplots_adjust(left=0.14, bottom=0.175)


plt.show()
