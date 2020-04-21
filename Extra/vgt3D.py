import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

BOUNDS = ((-5, 5), (-5, 5), (-5, 5))
ROTATION = (20, 300)


def __annotations__(x, y, z, i, j, k, fig, ax) -> None:
    '''
    Parameters
    ----------
    x : int/float
        starting x-coordinate of a vector
    
    y : int/float
        starting y-coordinate of a vector
    
    z : int/float
        starting z-coordinate of a vector
    
    i : int/float
        i-component of a vector
    
    j : int/float
        j-component of a vector
    
    k : int/float
        k-component of a vector
    
    fig : matplotlib ~figure.Figure
        a Figure object to add an axes to
    
    ax : matplotlib ~mplot3d.Axes3D
        an Axes3D object to plot onto
    
    Returns
    -------
    None
    '''

    # Start Point
    ax.scatter(x, y, z, color="k")
    ax.text(x, y, z, "({:.1f}, {:.1f}, {:.1f})".format(x, y, z))

    # End Point
    ax.scatter(x + i, y + j, z + k, color="k")
    ax.text(x + i, y + j, z + k, "({:.1f}, {:.1f}, {:.1f})".format(x + i, y + j, z + k))

    # Component Lines
    ax.plot( [x, x+i], [y, y], [z, z], linestyle="--", color="C0")
    ax.plot( [x+i, x+i], [y, y+j], [z, z], linestyle="--", color="C1")
    ax.plot( [x+i, x+i], [y+j, y+j], [z, z+k], linestyle="--", color="C2")


def plot_vector3D(x, y, z, i, j, k, fig, ax=None, bounds=BOUNDS, subplot=111, rotation=ROTATION, color='r', annotations=True) -> Axes3D:
    '''
    Parameters
    ----------
    x : int/float/iterable[int/float]
        starting x-coordinate of the vector(s)

    y : int/float/iterable[int/float]
        starting y-coordinate of the vector(s)
    
    z : int/float/iterable[int/float]
        starting z-coordinate of the vector(s)
    
    i : int/float/iterable[int/float]
        i-component of the vector(s)

    j : int/float/iterable[int/float]
        j-component of the vector(s)

    k : int/float/iterable[int/float]
        k-component of the vector(s)
    
    fig : matplotlib ~figure.Figure
        a Figure object to add an axes to
    
    ax : matplotlib ~mplot3d.Axes3D (optional), default=None
        an Axes3D object to plot onto

    bounds : tuple (optional), default=((-5, 5), (-5, 5), (-5, 5))
        (x, y, z) limits of the graph
    
    subplot : int/str (optional), default=111
        matplotlib ~Figure.add_subplot() subplot parameter
    
    rotation : tuple (optional), default=(20, 300)
        matplotlib ~Axes3D.view_init() parameters
    
    color : str/iterable[str] (optional), default='r'
        matplotlib ~Axes.plot() color parameter
    
    annotations : bool (optional), default=True
        enables/disables labeling of start/end coordinates
    
    Returns
    -------
    ax : matplotlib ~mplot3d.Axes3D
        the Axes3D object that was created/edited for plotting
    '''

    # Bounds
    xlim, ylim, zlim = bounds

    # Settings
    if not ax:
        ax = fig.add_subplot(subplot, projection="3d")
    ax.view_init(*rotation)
    
    # Vector(s)
    ax.quiver(x, y, z, i, j, k, color=color)

    try:
        iter(x), iter(y), iter(z), iter(i), iter(j), iter(k)
        if not len(x) == len(y) == len(z) == len(i) == len(j) == len(k):
            raise TypeError("Parameters x, y, z, i, j and k must all be of equal iterable length")
        
        # Annotations
        if annotations:
            for a in range(len(x)):
                __annotations__(x[a], y[a], z[a], i[a], j[a], k[a], fig, ax)
    
    except TypeError:
        if not all(isinstance(comp, (int, float)) for comp in [x, y, z, i, j, k]):
            raise TypeError("Parameters x, y, z, i, j and k are not all iterables, ints or floats")
        
        if annotations:
            __annotations__(x, y, z, i, j, k, fig, ax)

    # Bounds
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_zlim(*zlim)
    
    # Axis Lines
    ax.plot(xlim, [0, 0], [0, 0], alpha=0.5, color="C0")
    ax.plot([0, 0], ylim, [0, 0], alpha=0.5, color="C1")
    ax.plot([0, 0], [0, 0], zlim, alpha=0.5, color="C2")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    
    return ax


class Vector3D(object):
    
    def __init__(self, i, j, k):
        '''
        i : int/float
            i-component of vector
        
        j : int/float
            j-component of vector
        
        k : int/float
            k-component of vector
        '''

        self.i = i
        self.j = j
        self.k = k
        
    def __add__(self, other):
        '''
        Adds two Vector3D instances vectorially
        ''' 
        return Vector3D(self.i + other.i, self.j + other.j, self.k + other.k)
    
    def __iadd__(self, other): 
        '''
        In-place adds two Vector3D instances vectorially
        '''
        self.i += other.i
        self.j += other.j
        self.k += other.k
        return self
    
    def __sub__(self, other):  
        '''
        Subtracts two Vector3D instances vectorially
        '''
        return Vector3D(self.i - other.i, self.j - other.j, self.k - other.k)
    
    def __isub__(self, other):
        '''
        In-place subtracts two Vector3D instances vectorially
        '''
        self.i -= other.i
        self.j -= other.j
        self.k -= other.k
        return self
    
    def __mul__(self, a): 
        '''
        Multiplies vector by scalar
        '''
        return Vector3D(self.i * a, self.j * a, self.k * a)
    
    def __imul__(self, a):
        '''
        In-place multiplies vector by scalar
        '''
        self.i *= a
        self.j *= a
        self.k *= a
        return self
    
    def __truediv__(self, a):
        '''
        Divides vector by scalar
        '''
        return Vector3D(self.i / a, self.j / a, self.k / a)
    
    def __idiv__(self, a):
        '''
        In-place divides vector by scalar
        '''
        self.i /= a
        self.j /= a
        self.k /= a
        return self

    def cross(self, other):
        '''
        The cross product between two Vector3D instances
        '''
        return Vector3D(self.j*other.k - self.k*other.j, self.k*other.i - self.i*other.k, self.i*other.j - self.j*other.i )
    
    def dot(self, other):
        '''
        The dot product between two Vector3D instances
        '''
        return (self.i * other.i) + (self.j * other.j) + (self.k * other.k)
    
    def angle(self, other):
        '''
        The angle between two Vector3D instances
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
        return math.sqrt( self.i**2 + self.j**2 + self.k**2 )

    def plot(self, x, y, z, fig, ax=None, bounds=BOUNDS, subplot=111, rotation=ROTATION, color='r', annotations=True):
        '''
        Plots vector (see plot_vector3D())
        '''
        ret_ax = plot_vector3D(x, y, z, self.i, self.j, self.k, fig, 
                               ax=ax, 
                               bounds=bounds, 
                               subplot=subplot, 
                               rotation=rotation, 
                               color=color, 
                               annotations=annotations)
        return ret_ax

    def __str__(self):
        return "<{:.1f}, {:.1f}, {:.1f}>".format(self.i, self.j, self.k)
    
    def __repr__(self):
        return self.__str__()


class VectorField3D(object):

    def __init__(self, i_func, j_func, k_func):
        '''
        i_func : Callable
            i-component function; must have three inputs and one output
        
        j_func : Callable
            j-component function; must have three inputs and one output

        k_func : Callable
            k-component function; must have three inputs and one output
        '''
        self.i_func = i_func
        self.j_func = j_func
        self.k_func = k_func 


    def plot(self, fig, ax=None, scale_factor=10, density=10, bounds=BOUNDS, subplot=111, rotation=ROTATION, colormap="Blues", colorbar=True) -> Axes3D:
        '''
        Parameters
        ----------
        fig : matplotlib ~figure.Figure
            a Figure object to add an axes to
        
        ax : matplotlib ~axes.Axes3D (optional), default=None
            an Axes3D object to plot onto
        
        scale_factor : int/float (optional), default=10
            factor to downscale vector magnitudes
        
        density : int (optional), default=10
            a scalar that goes into calculating how many vectors are produced for the field

        bounds : tuple (optional), default=((-5, 5), (-5, 5), (-5, 5))
            (x, y, z) limits of the graph
        
        subplot : int/str (optional), default=111
            matplotlib ~Figure.add_subplot() subplot parameter

        rotation : tuple (optional), default=(20, 300)
            matplotlib ~Axes3D.view_init() parameters
        
        colormap : str (optional), default='Blues'
            matplotlib built-in colormap type
        
        colorbar : bool (optional), default=True
            enables/disables colorbar
        
        Returns
        -------
        ax : matplotlib ~mplot3d.Axes3D
            the Axes3D object that was created/edited for plotting
        '''

        xlim, ylim, zlim = bounds

        coordinates = [ [], [], [] ]
        components = [ [], [], [] ]

        max_mag = 0

        for x in np.linspace(xlim[0], xlim[1], density):
            for y in np.linspace(ylim[0], ylim[1], density):
                for z in np.linspace(zlim[0], zlim[1], density):
                    
                    # Coordinates in space
                    coordinates[0].append(x)
                    coordinates[1].append(y)
                    coordinates[2].append(z)

                    # Corresponding vector
                    v = Vector3D(self.i_func(x, y, z), self.j_func(x, y, z), self.k_func(x, y, z)) / scale_factor
                    mag = v.magnitude()

                    # Vector components
                    components[0].append(v.i)
                    components[1].append(v.j)
                    components[2].append(v.k)

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
            k_comp = components[2][i]

            mag = math.sqrt(i_comp**2 + j_comp**2 + k_comp**2)

            color = cm_sub[round((mag / max_mag) * 1000) - 1]

            colors.append(cmap(color))

        # Plotting
        ax = plot_vector3D(coordinates[0], coordinates[1], coordinates[2], components[0], components[1], components[2],
            fig=fig,
            ax=ax,
            bounds=bounds,
            subplot=subplot,
            rotation=rotation,
            color=colors,
            annotations=False,
        )

        # Colorbar
        if colorbar:
            cbar = plt.colorbar(mpl.cm.ScalarMappable(cmap=cmap), label="Magnitude (Factored Down by {})".format(scale_factor), ticks=[0, 1])
            cbar.ax.set_yticklabels(["Low", "High"])

        return ax
