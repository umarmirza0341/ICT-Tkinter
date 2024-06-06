import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_boxplot(file_path):
    data = pd.read_csv(file_path)

    plt.figure(figsize=(12, 8))
    sns.boxplot(x='Share Name', y='Volume', data=data, color='red')

    plt.xlabel('Category', fontsize=14)
    plt.ylabel('Volume', fontsize=14)
    plt.title('Distribution of Volume Across Categories', fontsize=16)

    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()

    plt.show()


plot_boxplot('Asst-3 data.csv')
