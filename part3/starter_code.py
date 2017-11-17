import pandas as pd
import bqplot
import us

names = ["date", "city", "state", "country", "shape", "duration_seconds",
         "duration_reported", "description", "report_date", "latitude",
         "longitude"]

fn = "/srv/nbgrader/data/ufo-scrubbed-geocoded-time-standardized.csv"
ufo = pd.read_csv(fn, names = names, parse_dates = ["date", "report_date"])

abbr_to_fits = us.states.mapping('abbr', 'fips')
ufo["fips"] = ufo["state"].apply(lambda a: int(abbr_to_fits.get(str(a).upper(), -1)))
fips_count = ufo.groupby("fips")["duration_seconds"].count()

map_styles = {'scales': {'projection': bqplot.AlbersUSA(),
                         'color': bqplot.ColorScale(colors=["red", "blue"])},
              'color': fips_count.to_dict()}
states_map = bqplot.Map(map_data=bqplot.topo_load('map_data/USStatesMap.json'),
        **map_styles)
map_fig = bqplot.Figure(marks=[states_map], title='USA')
