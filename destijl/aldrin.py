import pkg_resources
import matplotlib as mpl
import matplotlib.font_manager as font_manager

COLOURS = {
    'B': '#0b3d91',
    'R': '#c62d1f',
    'ALT': '#00a6d2',
    'AU': '#ff9d1e',
    'G': '#2e8540',
    'C': '#205493',
    'B-': '#105bd8',
    'R-': '#dd361c',
    'ALT-': '#02bfe7',
    'AU-': '#f9aa43',
    'G-': '#4aa564',
    'C-': '#4773aa',
    'B+': '#061f4a',
    'R+': '#99231b',
    'ALT+': '#046b99',
    'B--': '#dce4ef',
    'R--': '#e59892',
    'ALT--': '#9bdaf1',
    'AU--': '#ffc375',
    'G--': '#94bfa2',
    'C--': '#8ba6ca',
    'dark_gray': '#3d4e5f',
    'medium_gray': '#77838f',
    'light_gray': '#b1b8bf',
    'warm_gray': '#494440',
    'GR+': '#323a45',
    'GR': '#5b616b',
    'GR-': '#aeb0b',
    'GR--': '#d6d7d9',
}


def aldrin() -> None:
    load_fonts()
    use_style('aldrin.mplstyle')

def load_fonts() -> None:
    for font in font_manager.findSystemFonts('fonts'):
        font_manager.fontManager.addfont(font)


def use_style(file: str) -> None:
    """
    Overwrite the global matplotlib style with the basic style, reading
    from the associated stylefile. Should function for any valid matplotlib
    style file.
    """
    style_dict = {}
    path = pkg_resources.resource_filename(__name__, file)
    with open(path) as f:
        for line in f:
            components = line.split(':')
            if len(components) == 2:
                # Account for comments
                value = components[1].split('#')[0].strip()
                style_dict[components[0].strip()] = value
    mpl.rcParams.update(style_dict)
