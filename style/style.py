import pkg_resources
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap

COLOURS = {
    'A': '#8cddcf',
    'B': '#4ab7ee',
    'C': '#1a78ee',
    'D': '#eea9c5',
    'F': '#ee7438',
    'A-': '#abe0dd',
    'B-': '#abe0f4',
    'C-': '#8dc0f7',
    'D-': '#efd0e0',
    'F-': '#f7b7a1',
    'A+': '#61d6bf',
    'B+': '#17a5dd',
    'C+': '#0966cc',
    'D+': '#e492b8',
    'F+': '#e56538',
    'dark_gray': '#3d4e5f',
    'medium_gray': '#77838f',
    'light_gray': '#b1b8bf',
    'RAG_G': '#4ab270',
    'RAG_A': '#ffec62',
    'RAG_R': '#e74258'
}

SCORES = [COLOURS['A'], COLOURS['B'], COLOURS['C'], COLOURS['D'], COLOURS['F']]

MAP = LinearSegmentedColormap.from_list('base', SCORES, 256)
MAP_DISCRETE = LinearSegmentedColormap.from_list('base', SCORES, 5)


def use_style():
    """
    Overwrite the global matplotlib style with the basic style, reading
    from the associated stylefile. Should function for any valid matplotlib
    style file.
    """
    style_dict = {}
    path = pkg_resources.resource_filename(__name__, 'base.mplstyle')
    with open(path) as f:
        for line in f:
            components = line.split(':')
            if len(components) == 2:
                # Account for comments
                value = components[1].split('#')[0].strip()
                style_dict[components[0].strip()] = value
    mpl.rcParams.update(style_dict)
