
import ipywidgets as widgets
from .data import ANALYSIS_RESULTS
from .components import create_image_upload_card, create_results_card

def render():
    c1 = create_image_upload_card()
    c2 = create_results_card(ANALYSIS_RESULTS)
    
    grid = widgets.GridBox([c1, c2], layout=widgets.Layout(grid_template_columns='1fr 1fr', grid_gap='20px'))
    
    return grid
