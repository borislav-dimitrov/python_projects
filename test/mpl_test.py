import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter as tk


def upd(ax, canvas, fig, contour, cbar):
    import pdb;
    pdb.set_trace()
    # contour.set_clim(-.5, 1)
    # new_ticks = np.linspace(-.5, 1, len(cbar.values) + 1).astype(int)
    # print(new_ticks)
    # cbar.set_ticklabels(new_ticks)
    canvas.draw()


def main():
    root = tk.Tk()
    fig = Figure(figsize=(6, 5))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    ax = fig.gca()
    # Generate some random data
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-X ** 2 - Y ** 2)

    # Create a contour plot
    contour = ax.contourf(X, Y, Z, cmap='coolwarm')
    cbar = fig.colorbar(contour)

    tk.Button(root, text='A', command=lambda: upd(ax, canvas, fig, contour, cbar)).pack()

    root.mainloop()


if __name__ == '__main__':
    main()
