
import ipywidgets as widgets
from .data import USER_LEVEL, MISSIONS, ACHIEVEMENTS, STREAK_DATA
from .components import create_level_card, create_missions_card, create_achievements_card, create_streak_card

def render():
    c1 = create_level_card(USER_LEVEL)
    c2 = create_missions_card(MISSIONS)
    c3 = create_achievements_card(ACHIEVEMENTS)
    
    top_row = widgets.GridBox([c1, c2, c3], layout=widgets.Layout(grid_template_columns='1fr 1fr 1fr', grid_gap='20px', margin='0 0 20px 0'))
    
    streak = create_streak_card(STREAK_DATA)
    
    return widgets.VBox([top_row, streak])
