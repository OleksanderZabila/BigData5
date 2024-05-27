from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.tile_providers import get_provider
import pandas as pd

# Создание набора данных
data = {
    'longitude': [-73.968285, -73.977291, -73.985676, -73.9669, -73.975, -73.965, -73.977, -73.98, -73.982, -73.985],
    'latitude': [40.785091, 40.762428, 40.748817, 40.780, 40.770, 40.760, 40.770, 40.775, 40.780, 40.785],
    'city': ['New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York', 'New York',
             'New York'],
    'crimes': [100, 50, 75, 60, 80, 70, 90, 85, 95, 65],
    'crime_type': ['Robbery', 'Assault', 'Burglary', 'Robbery', 'Assault', 'Burglary', 'Robbery', 'Assault', 'Burglary',
                   'Robbery']  # Добавлено новое поле с типом преступления
}

# Приведение координат к соответствующему формату
min_lon, max_lon = min(data['longitude']), max(data['longitude'])
min_lat, max_lat = min(data['latitude']), max(data['latitude'])

data['x_coord'] = [(lon - min_lon) / (max_lon - min_lon) * 2000 for lon in data['longitude']]
data['y_coord'] = [(lat - min_lat) / (max_lat - min_lat) * 2000 for lat in data['latitude']]

# Создание источника данных
source = ColumnDataSource(data=data)

# Создание карты
p = figure(x_range=(0, 2000), y_range=(0, 2000), title="Crime Data Visualization")
p.add_tile(get_provider('CARTODBPOSITRON'))

# Добавление маркеров
p.circle(x='x_coord', y='y_coord', size='crimes', fill_color='red', fill_alpha=0.6, source=source)

# Добавление интерактивных названий городов и количества преступлений
hover = HoverTool()
hover.tooltips = [("City", "@city"), ("Crimes", "@crimes"),
                  ("Crime Type", "@crime_type")]  # Добавлено отображение типа преступления
p.add_tools(hover)

# Вывод визуализации
output_file("crime_map.html")
show(p)
