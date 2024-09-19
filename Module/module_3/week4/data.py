import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def  draw():
    """
    
    
    """
    np.random.seed(42)
    X = np.random.rand(100, 2) * 10  # 100 điểm dữ liệu với 2 features trong khoảng [0, 10]
    y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.randn(100) * 2  

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    sc = ax.scatter(X[:, 0], X[:, 1], y, c=y, cmap='viridis', marker='o')

    ax.set_title('3D Visualization of Random Regression Data with Adjustable View')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_zlabel('Output (y)')

    axcolor = 'lightgoldenrodyellow'
    ax_elev = plt.axes([0.25, 0.02, 0.65, 0.03], facecolor=axcolor)  # Slider cho elev
    ax_azim = plt.axes([0.25, 0.06, 0.65, 0.03], facecolor=axcolor)  # Slider cho azim

    slider_elev = Slider(ax_elev, 'Elev', 0, 90, valinit=30)
    slider_azim = Slider(ax_azim, 'Azim', 0, 360, valinit=60)

    def update(val):
        ax.view_init(elev=slider_elev.val, azim=slider_azim.val)
        fig.canvas.draw_idle()  

    slider_elev.on_changed(update)
    slider_azim.on_changed(update)

    plt.show()

if __name__ == "__main__" :
    draw()
    