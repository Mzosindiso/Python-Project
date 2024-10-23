import os
import matplotlib.pyplot as plt

def plot_histograms(df):
    df.hist(figsize=(15, 12), bins=20)
    plt.tight_layout()
    os.makedirs('../results/figures', exist_ok=True)
    plt.savefig('../results/figures/histograms.png')
    plt.close()

def plot_scatter(df, x_column, y_column):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_column], df[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Scatter Plot: {x_column} vs {y_column}')
    os.makedirs('../results/figures', exist_ok=True)
    plt.savefig(f'../results/figures/scatter_{x_column}_{y_column}.png')
    plt.close()