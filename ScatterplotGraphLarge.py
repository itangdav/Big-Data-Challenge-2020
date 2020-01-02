import plotly
import plotly.graph_objs as go
from scipy import stats
import numpy as np

X_COORDS = []
Y_COORDS = []

DATA = []

def initialize_coords():
    f= open("CityData.txt","r")
    f1 = f.readlines()
    for i in f1:
        population = float(i[:i.index("|")])
        change = float(i[i.index("|")+1:i.rindex("|")])
        distance = float(i[i.rindex("|")+1:])
        if(population>=1000):
            X_COORDS.append(distance)
            Y_COORDS.append(change)

    counter = 0
    while counter < len(X_COORDS):
        if X_COORDS[counter] is None or Y_COORDS[counter] is None:
            X_COORDS.pop(counter)
            Y_COORDS.pop(counter)
        else:
            counter += 1

def linear_regress():
    slope, intercept, r_value, p_value, std_err = stats.linregress(X_COORDS, Y_COORDS)
    DATA.append(go.Scatter(
        x=[0.0, max(X_COORDS)],
        y=[intercept, slope * max(X_COORDS) + intercept],
        mode='lines',
        name=("Regression Line Linear, R=" + str(r_value))
    ))

def format_layout():
    layout = go.Layout(
        hovermode='closest',
        xaxis=dict(
            title=X_AXIS,
            ticklen=5,
            zeroline=False,
            gridwidth=2,
        ),
        yaxis=dict(
            title=Y_AXIS,
            ticklen=5,
            gridwidth=2,
        )
    )
    return layout

#Main


global X_AXIS, Y_AXIS;
X_AXIS = "Distance to Ocean";
Y_AXIS = "Change in Growth from 2017 to 2018";

initialize_coords()
layout = format_layout()
DATA.append(go.Scatter(
    x=X_COORDS,
    y=Y_COORDS,
    mode='markers',
    name="Test"
))
linear_regress()

filename = "plots/LargeCities.html"
plotly.offline.plot({
    "data": DATA,
    "layout": layout,
}, auto_open=True, filename=filename)