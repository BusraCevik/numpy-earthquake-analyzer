import numpy as np


def extract_year(date_str):
    date_str = date_str.strip()
    if 'T' in date_str:
        return int(date_str.split('T')[0].split('-')[0])
    elif '/' in date_str:
        return int(date_str.split('/')[-1])
    else:
        return int(date_str[:4])


def yearly_stats(dates, magnitudes):
    years = np.array([extract_year(d) for d in dates])
    unique_years = np.unique(years)

    yearly_counts = np.zeros(len(unique_years))
    yearly_avg_magnitude = np.zeros(len(unique_years))

    for i, year in enumerate(unique_years):
        mask = years == year
        yearly_counts[i] = np.sum(mask)
        yearly_avg_magnitude[i] = np.mean(magnitudes[mask])

    return unique_years, yearly_counts, yearly_avg_magnitude, years
