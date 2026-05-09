import pandas as pd
import plotly.express as px
import numpy as np

def prepare_plotly_df(latitudes, longitudes, magnitudes, years):
    unique_years = np.unique(years)
    yearly_data = {}
    for year in unique_years:
        mask = years == year
        yearly_data[year] = {
            'lat': latitudes[mask],
            'lon': longitudes[mask],
            'mag': magnitudes[mask]
        }

    all_data = []
    for year, data_dict in yearly_data.items():
        df_year = pd.DataFrame({
            'Latitude': data_dict['lat'],
            'Longitude': data_dict['lon'],
            'Magnitude': data_dict['mag'],
            'Year': year
        })
        all_data.append(df_year)

    df_plotly = pd.concat(all_data, ignore_index=True)
    return df_plotly

def create_animated_map(df_plotly, output_path=None):
    mag_min = df_plotly['Magnitude'].min()
    mag_max = df_plotly['Magnitude'].max()

    fig = px.scatter_geo(
        df_plotly,
        lat='Latitude',
        lon='Longitude',
        color='Magnitude',
        size='Magnitude',
        size_max=8,
        animation_frame='Year',
        projection='natural earth',
        color_continuous_scale='Magenta',
        range_color=[mag_min, mag_max],
        title='Global Earthquakes Animation by Year'
    )
    fig.update_layout(legend_title_text='Magnitude')

    if output_path:
        fig.write_html(output_path)

    fig.show()
