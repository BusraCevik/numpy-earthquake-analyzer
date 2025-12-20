import numpy as np


def load_earthquake_data(csv_path):
    # Load dataset
    data = np.genfromtxt(csv_path, delimiter=',', skip_header=1, dtype=None, encoding=None)

    # Read headers
    with open(csv_path, 'r', encoding='utf-8') as f:
        headers = f.readline().strip().split(',')

    # Identify important columns
    date_idx = headers.index('Date')
    lat_idx = headers.index('Latitude')
    lon_idx = headers.index('Longitude')
    mag_idx = headers.index('Magnitude')
    depth_idx = headers.index('Depth')

    # Filter rows with missing values
    valid_rows = [row for row in data if row[mag_idx] != '' and row[lat_idx] != '' and row[lon_idx] != '']

    # Extract columns
    latitudes = np.array([float(row[lat_idx]) for row in valid_rows])
    longitudes = np.array([float(row[lon_idx]) for row in valid_rows])
    magnitudes = np.array([float(row[mag_idx]) for row in valid_rows])
    depths = np.array([float(row[depth_idx]) for row in valid_rows])
    dates = np.array([row[date_idx] for row in valid_rows])

    return headers, latitudes, longitudes, magnitudes, depths, dates