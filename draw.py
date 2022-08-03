import matplotlib.pyplot as plt
import numpy as np


class Graph:
    def __init__(self, walk, bike, transit, address):
        self.walk = walk
        self.bike = bike
        self.transit = transit
        self.address = address

    def construct(self):
        labels = ['Walk', 'Bike', 'Transit']

        value = [self.walk, self.bike, self.transit]

        x = np.arange(len(labels))  # the label locations
        width = 0.5  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, value, width, label='Score')
        ax.set_ylabel('Scores')
        ax.set_title(f'Scores of {self.address}')
        ax.set_xticks(x, labels)
        ax.bar_label(rects1, padding=2)

        fig.tight_layout()
        ax.set_ylim(0, 100)
        plt.savefig(f'{self.address}.png')
