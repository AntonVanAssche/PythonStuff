#!/usr/bin/env python3

# Import libraries
import pandas as pd
import plotly.express as px

# The API used to get the data.
url = 'http://api.open-notify.org/iss-now.json'

# Get the data from the json file the API provided.
# df stands for data frame.
df = pd.read_json(url)

# In order to plot the data in a correct way, we need to change the layout a little bit.
df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True)

# The output of 'print(df)' is now:
#        index  message  iss_position           timestamp  latitude  longitude
# 0   latitude  success       35.2540 2022-05-04 16:22:23    35.254  -130.1239
# 1  longitude  success     -130.1239 2022-05-04 16:22:23    35.254  -130.1239

# Drop the columns we don't need anymore.
# (This isn't necessary, but it will make the output a bit cleaner.)
df = df.drop(['index', 'message'], axis = 1)

# The output of 'print(df)' is now:
#    iss_position           timestamp  latitude  longitude
# 0       37.2204 2022-05-04 16:21:35   37.2204  -132.8641
# 1     -132.8641 2022-05-04 16:21:35   37.2204  -132.8641

# Create the image with the location of the ISS.
fig = px.scatter_geo(df, lat='latitude', lon='longitude')

print(df)

# Open the image in a browser.
fig.show()
