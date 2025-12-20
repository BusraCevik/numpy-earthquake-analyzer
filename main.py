from src.data_loader import load_earthquake_data
from src.time_analysis import yearly_stats
from src.depth_mag import (
    plot_depth_vs_magnitude_hist,
    plot_depth_vs_magnitude_scatter
)
from src.plotly_map import prepare_plotly_df, create_animated_map
import os

# ==================================================
# Output Directories
# ==================================================
DATA_OUTPUT_DIR = 'data/outputs'
DOCS_DIR = 'docs'

os.makedirs(DATA_OUTPUT_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)

# ==================================================
# Load Dataset
# ==================================================
csv_path = 'data/dataset/database.csv'
headers, lat, lon, mag, depth, dates = load_earthquake_data(csv_path)

# ==================================================
# Time Analysis
# ==================================================
unique_years, yearly_counts, yearly_avg_magnitude, years = yearly_stats(dates, mag)

# ==================================================
# Depth vs Magnitude Plots
# ==================================================
plot_depth_vs_magnitude_hist(
    depth,
    mag,
    output_path=os.path.join(DATA_OUTPUT_DIR, 'hist_depth_mag.png')
)

plot_depth_vs_magnitude_scatter(
    depth,
    mag,
    output_path=os.path.join(DATA_OUTPUT_DIR, 'scatter_depth_mag.png')
)

# ==================================================
# Filter Extreme Values
# ==================================================
mask = (depth >= 0) & (depth <= 700) & (mag >= 0)
lat, lon, mag, depth, dates, years = (
    lat[mask],
    lon[mask],
    mag[mask],
    depth[mask],
    dates[mask],
    years[mask]
)

# ==================================================
# Plotly Interactive Map
# ==================================================
df_plotly = prepare_plotly_df(lat, lon, mag, years)

create_animated_map(
    df_plotly,
    output_path=os.path.join(DOCS_DIR, 'index.html')
)
