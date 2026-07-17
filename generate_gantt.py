import plotly.figure_factory as ff
import pandas as pd
import os

# Create Gantt chart data for Project Timeline
df = pd.DataFrame([
    dict(Task="Phase 1: Data Collection & Cleaning", Start='2024-01-01', Finish='2024-02-15', Resource='Data Engineering'),
    dict(Task="Phase 2: NLP Analysis & Severity Labeling", Start='2024-02-16', Finish='2024-03-10', Resource='NLP Team'),
    dict(Task="Phase 3: Exploratory Data Analysis (EDA)", Start='2024-03-11', Finish='2024-03-30', Resource='Analytics'),
    dict(Task="Phase 4: ML Model Training (Random Forest/XGBoost)", Start='2024-04-01', Finish='2024-05-15', Resource='Data Science'),
    dict(Task="Phase 5: Ward Risk Clustering (K-Means)", Start='2024-05-16', Finish='2024-06-05', Resource='Analytics'),
    dict(Task="Phase 6: Dashboard Development & Testing", Start='2024-06-06', Finish='2024-07-20', Resource='Frontend Dev'),
])

fig = ff.create_gantt(df, index_col='Resource', show_colorbar=True, group_tasks=True, title="FloodSense Mumbai - Project Timeline")

# Save as PNG
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gantt_chart_report.png")
fig.write_image(output_path, width=1000, height=500)
print(f"Gantt chart saved to {output_path}")
