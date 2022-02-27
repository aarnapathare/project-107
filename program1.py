import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
studentdf = df.loc[df["student_id"] == "TRL_987"]
grouped = studentdf.groupby("level")["attempt"].mean()
print(grouped)

fig = go.Figure(go.Bar(
    x = grouped, y = ["Level 1", "Level 2", "Level 3", "Level 4"],
    orientation = "h"
))

fig.show()