from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import plotly
import json 


infile = open ('US_fires_9_14.json')
outfile = open("readable_US_fires_9_1.json","w")

eqdata = json.load(infile)

json.dump(eqdata,outfile,indent=4)

bright,lats,lons =[],[],[]

list_of_eqs = eqdata

for eq in list_of_eqs:
    if eq["brightness"] > 450:
        brit = eq["brightness"]
        lat = eq["latitude"]
        lon = eq["longitude"]
        lats.append(lat)
        lons.append(lon)
        bright.append(brit)

print(bright)

data = [{
    'type': 'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{
        'size':[(.025*b)for b in bright],
        'color':bright,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title':'Magnitude'}
    }



}]


my_layout = Layout(title="US Fires - 9/1/2020 through 9/13/2020")

fig = {'data': data,'layout':my_layout}

offline.plot(fig,filename='USFires.html')