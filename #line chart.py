#line chart
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'study_sessions.csv'  
df = pd.read_csv(file_path)

df["Duration"] = pd.to_timedelta(df["Duration"])
df["StartDate"] = pd.to_datetime(df["StartDate"])
daily_totals = df.groupby("StartDate")["Duration"].sum()

x_values = range(len(daily_totals.index.date))  
dates = daily_totals.index.date  
y_values = daily_totals.dt.total_seconds() / 3600  

plt.figure(figsize=(12, 6))

plt.plot(
    x_values,  
    y_values,  
    color='blue', marker='o', label='Study Duration' 
)

for x, y in zip(x_values, y_values):
    plt.vlines(
        x=x, 
        ymin=0,  
        ymax=y,  
        colors='gray', linestyles='dotted', linewidth=1
    )

plt.title("Total Study Duration per Day", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total Duration (hours)", fontsize=12)
plt.xticks(ticks=x_values, labels=dates, rotation=45, fontsize=10)
plt.yticks(fontsize=10)

plt.legend(loc='lower right', fontsize=10, title="Legend")

plt.tight_layout()
plt.show()
