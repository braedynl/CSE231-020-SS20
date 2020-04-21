import math 
import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

BOUNDS = ((-5, 5), (-5, 5))


def __annotations__(x, y, i, j, fig, ax) -> None:
    '''
    Parameters
    ----------
    x : int/float
        starting x-coordinate of a vector
    
    y : int/float
        starting y-coordinate of a vector
    
    i : int/float
        i-component of a vector
    
    j : int/float
        j-component of a vector
    
    fig : matplotlib ~figure.Figure
        a Figure object to add an axes to
    
    ax : matplotlib ~axes.Axes
        an Axes object to plot onto
    
    Returns
    -------
    None
    '''

    # Start Point
    ax.scatter(x, y, color='k')
    ax.text(x, y, "({:.1f}, {:.1f})".format(x, y))

    # End Point
    ax.scatter(x + i, y + j, color='k')
    ax.text(x + i, y + j, "({:.1f}, {:.1f})".format(x + i, y + j))

    # Component Lines
    ax.plot( [x, x+i], [y, y], linestyle="--", color="C0")
    ax.plot( [x+i, x+i], [y, y+j], linestyle="--", color="C1")


def plot_vector2D(x, y, i, j, fig, ax=None, bounds=BOUNDS, subplot=111, color='r', annotations=True) -> Axes:
    '''
    Parameters
    ----------
    x : int/float/iterable[int/float]
        starting x-coordinate of the vector(s)

    y : int/float/iterable[int/float]
        starting y-coordinate of the vector(s)
    
    i : int/float/iterable[int/float]
        i-component of the vector(s)

    j : int/float/iterable[int/float]
        j-component of the vector(s)
    
    fig : matplotlib ~figure.Figure
        a Figure object to add an axes to
    
    ax : matplotlib ~axes.Axes (optional), default=None
        an Axes object to plot onto

    bounds : tuple (optional), default=((-5, 5), (-5, 5))
        (x, y) limits of the graph
    
    subplot : int/str (optional), default=111
        matplotlib ~Figure.add_subplot() subplot parameter
    
    color : str/iterable[str] (optional), default='r'
        matplotlib ~Axes.plot() color parameter
    
    annotations : bool (optional), default=True
        enables/disables labeling of start/end coordinates
    
    Returns
    -------
    ax : matplotlib ~axes.Axes
        the Axes object that was created/edited for plotting
    '''
    
    # Bounds
    xlim, ylim = bounds

    # Settings
    if not ax:
        ax = fig.add_subplot(subplot)
    ax.set_aspect("equal")
    ax.grid(b=True)
    
    # Vector(s)
    ax.quiver(x, y, i, j, scale=1, units='xy', color=color)

    try:
        iter(x), iter(y), iter(i), iter(j)
        if not len(x) == len(y) == len(i) == len(j):
            raise TypeError("Parameters x, y, i and j must all be of equal iterable length")
            
        # Annotations
        if annotations:
            for a in range(len(x)):
                __annotations__(x[a], y[a], i[a], j[a], fig, ax)
    
    except TypeError:
        if not all(isinstance(comp, (int, float)) for comp in [x, y, i, j]):
            raise TypeError("Parameters x, y, i and j are not all iterables, ints or floats")
        
        if annotations:
            __annotations__(x, y, i, j, fig, ax)

    # Bounds
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    
    # Axis Lines
    ax.plot(xlim, [0, 0], alpha=0.5, color="C0")
    ax.plot([0, 0], ylim, alpha=0.5, color="C1")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    
    return ax


class Vector2D(object):
    
    def __init__(self, i, j):
        '''
        i : int/float
            i-component of vector
        
        j : int/float
            j-component of vector
        '''

        self.i = i
        self.j = j    
        
    def __add__(self, other):
        '''
        Adds two Vector2D instances vectorially
        ''' 
        return Vector2D(self.i + other.i, self.j + other.j)
    
    def __iadd__(self, other):
        '''
        In-place adds two Vector2D instances vectorially
        '''
        self.i += other.i
        self.j += other.j
        return self
    
    def __sub__(self, other):
        '''
        Subtracts two Vector2D instances vectorially
        '''
        return Vector2D(self.i - other.i, self.j - other.j)
    
    def __isub__(self, other):  
        '''
        In-place subtracts two Vector2D instances vectorially
        '''  
        self.i -= other.i
        self.j -= other.j
        return self
    
    def __mul__(self, a): 
        '''
        Multiplies vector by scalar
        ''' 
        return Vector2D(self.i * a, self.j * a)
    
    def __imul__(self, a): 
        '''
        In-place multiplies vector by scalar
        ''' 
        self.i *= a
        self.j *= a
        return self
    
    def __truediv__(self, a):
        '''
        Divides vector by scalar
        '''
        return Vector2D(self.i / a, self.j / a)
    
    def __idiv__(self, a):
        '''
        In-place divides vector by scalar
        '''
        self.i /= a
        self.j /= a
        return self

    def dot(self, other):
        '''
        The dot product between two Vector2D instances
        '''
        return (self.i * other.i) + (self.j * other.j)
    
    def angle(self, other):
        '''
        The angle between two Vector2D instances
        '''
        return math.acos( self.dot(other) / ( self.magnitude() * other.magnitude() ) )
        
    def unit(self):
        '''
        Converts vector to unit vector
        '''
        self.__idiv__(self.magnitude())
        
    def magnitude(self):
        '''
        Magnitude of the vector
        '''
        return math.sqrt( self.i**2 + self.j**2)

    def plot(self, x, y, fig, ax=None, bounds=BOUNDS, subplot=111, color='r', annotations=True):
        '''
        Plots vector (see plot_vector2D())
        '''
        ret_ax = plot_vector2D(x, y, self.i, self.j, fig, 
                               ax=ax, 
                               bounds=bounds, 
                               subplot=subplot, 
                               color=color, 
                               annotations=annotations)
        return ret_ax
    
    def __str__(self):
        return "<{:.1f}, {:.1f}>".format(self.i, self.j)
    
    def __repr__(self):
        return self.__str__()


class VectorField2D(object):

    def __init__(self, i_func, j_func):
        '''
        i_func : Callable
            i-component function; must have two inputs and one output
        
        j_func : Callable
            j-component function; must have two inputs and one output
        '''

        self.i_func = i_func
        self.j_func = j_func


    def plot(self, fig, ax=None, scale_factor=10, density=10, bounds=BOUNDS, subplot=111, colormap='Blues', colorbar=True) -> Axes:
        '''
        Parameters
        ----------
        fig : matplotlib ~figure.Figure
            a Figure object to add an axes to
        
        ax : matplotlib ~axes.Axes (optional), default=None
            an Axes object to plot onto
        
        scale_factor : int/float (optional), default=10
            factor to downscale vector magnitudes
        
        density : int (optional), default=10
            a scalar that goes into calculating how many vectors are produced for the field

        bounds : tuple (optional), default=((-5, 5), (-5, 5))
            (x, y) limits of the graph
        
        subplot : int/str (optional), default=111
            matplotlib ~Figure.add_subplot() subplot parameter
        
        colormap : str (optional), default='Blues'
            matplotlib built-in colormap type
        
        colorbar : bool (optional), default=True
            enables/disables colorbar
        
        Returns
        -------
        ax : matplotlib ~axes.Axes
            the Axes object that was created/edited for plotting
        '''

        xlim, ylim = bounds

        coordinates = [ [], [] ]
        components = [ [], [] ]

        max_mag = 0

        for x in np.linspace(xlim[0], xlim[1], density):
            for y in np.linspace(ylim[0], ylim[1], density):
                
                # Coordinates in space
                coordinates[0].append(x)
                coordinates[1].append(y)

                # Corresponding vector
                v = Vector2D(self.i_func(x, y), self.j_func(x, y)) / scale_factor
                mag = v.magnitude()

                # Vector components
                components[0].append(v.i)
                components[1].append(v.j)

                # Finding vector with largest magnitude
                if mag > max_mag:
                    max_mag = mag

        # Colormap
        cmap = plt.get_cmap(colormap)
        colors = []
        cm_sub = np.linspace(0, 1, 1000)

        # Assigns each vector that was calculated a color on the map,
        # dependent on the vector's magnitude compared to the largest vector(s)
        for i in range(len(components[0])):
            i_comp = components[0][i]
            j_comp = components[1][i]

            mag = math.sqrt(i_comp**2 + j_comp**2)

            color = cm_sub[round((mag / max_mag) * 1000) - 1]

            colors.append(cmap(color))

        # Plotting
        ax = plot_vector2D(coordinates[0], coordinates[1], components[0], components[1],
            fig=fig,
            ax=ax,
            bounds=bounds,
            subplot=subplot,
            color=colors,
            annotations=False,
        )

        # Colorbar
        if colorbar:
            cbar = plt.colorbar(mpl.cm.ScalarMappable(cmap=cmap), label="Magnitude (Factored Down by {})".format(scale_factor), ticks=[0, 1])
            cbar.ax.set_yticklabels(["Low", "High"])

        return ax