from datetime import datetime
import pandas as pd

df = pd.read_csv("report_stats.csv")
df = df[df['Name'] != 'Aggregated']

with open("performance_report.txt", "w") as f:
    f.write("Performance Testing Report - Reqres.in\n")
    f.write("="*40 + "\n")
    f.write(f"Date: {datetime.now()}\n\n")

    f.write("Tested Endpoints:\n")
    for name in df['Name']:
        f.write(f"  - {name}\n")
    f.write("\n")

    f.write("Performance Metrics:\n")
    for _, row in df.iterrows():
        f.write(f"\nEndpoint: {row['Name']}\n")
        f.write(f"  Avg Time: {row['Average Response Time (ms)']} ms\n")
        f.write(f"  Max Time: {row['Max Response Time (ms)']} ms\n")
        f.write(f"  RPS: {row['Requests/s']:.2f}\n")

    f.write("\nOptimization Suggestions:\n")
    f.write("- Провести профилирование на стороне сервера (если доступно)\n")
    f.write("- Внедрить кэширование результатов на GET\n")
    f.write("- Убедиться, что база данных оптимизирована под POST\n")
