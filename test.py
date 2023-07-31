import numpy as np
import matplotlib.pyplot as plt


def test():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

    