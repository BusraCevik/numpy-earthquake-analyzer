import matplotlib.pyplot as plt

def plot_depth_vs_magnitude_hist(depths, magnitudes, output_path=None):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10,6))
    plt.hist2d(depths, magnitudes, bins=[70, 50], range=[[0,70],[magnitudes.min(), magnitudes.max()]],
               cmap='magma_r', vmin=1, vmax=200)
    cbar = plt.colorbar()
    cbar.set_label('Number of Earthquakes', rotation=270, labelpad=15)
    plt.xlabel('Depth (km)')
    plt.ylabel('Magnitude')
    plt.title('2D Histogram: Magnitude vs Depth (0-100 km)')
    if output_path:
        plt.savefig(output_path, bbox_inches='tight')  # output klasörüne kaydet
    plt.show()


def plot_depth_vs_magnitude_scatter(depths, magnitudes, output_path=None):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.scatter(depths, magnitudes, alpha=0.5, s=10, c='#C71585')
    plt.xlabel('Depth (km)')
    plt.ylabel('Magnitude')
    plt.title('Magnitude vs Depth Scatter Plot')
    if output_path:
        plt.savefig(output_path, bbox_inches='tight')
    plt.show()

