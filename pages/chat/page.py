
import ipywidgets as widgets
from .data import CHAT_HISTORY, CONTEXT_DATA, SUGGESTED_QUESTIONS
from .components import create_chat_area, create_context_card, create_suggestions_card

def render():
    chat_area = create_chat_area(CHAT_HISTORY)
    
    # Sidebar
    context = create_context_card(CONTEXT_DATA)
    suggestions = create_suggestions_card(SUGGESTED_QUESTIONS)
    sidebar = widgets.VBox([context, suggestions], layout=widgets.Layout(grid_gap='20px'))
    
    grid = widgets.GridBox([chat_area, sidebar], layout=widgets.Layout(grid_template_columns='3fr 1fr', grid_gap='20px'))
    
    return grid
