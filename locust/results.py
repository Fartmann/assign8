import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("report_stats.csv")
df = df[df["Name"] != "Aggregated"]

print("\n=== PERFORMANCE METRICS ===")
for _, row in df.iterrows():
    print(f"Endpoint: {row['Name']}")
    print(f"  Avg Time: {row['Average Response Time (ms)']} ms")
    print(f"  Min: {row['Min Response Time (ms)']} ms")
    print(f"  Max: {row['Max Response Time (ms)']} ms")
    print(f"  RPS: {row['Requests/s']:.2f}\n")

plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Average Response Time (ms)'], color='orange')
plt.xticks(rotation=45)
plt.title("Average Response Time")
plt.ylabel("Time (ms)")
plt.tight_layout()
plt.savefig("response_times.png")
plt.show()
