
import ipywidgets as widgets
from .data import PLANTS_DATA
from .components import create_plant_card, create_health_card, create_sensor_card, create_alerts_card, create_actions_card

def render():
    # State
    current_plant_id = "1"
    
    # Output area for dynamic content
    content = widgets.Output()
    
    def update_view(change=None):
        nonlocal current_plant_id
        if change:
            current_plant_id = change['new']
            
        plant = PLANTS_DATA[current_plant_id]
        
        # Grid 1: Top 3 cards
        c1 = create_plant_card(plant)
        c2 = create_health_card(plant)
        c3 = create_sensor_card(plant)
        
        grid1 = widgets.GridBox([c1, c2, c3], layout=widgets.Layout(grid_template_columns='1fr 1fr 1fr', grid_gap='20px', margin='0 0 20px 0'))
        
        # Grid 2: Bottom 2 cards
        c4 = create_alerts_card(plant)
        c5 = create_actions_card()
        
        grid2 = widgets.GridBox([c4, c5], layout=widgets.Layout(grid_template_columns='1fr 1fr', grid_gap='20px'))
        
        content.clear_output()
        with content:
            display(grid1)
            display(grid2)

    # Selector
    selector_options = [(p['name'], k) for k, p in PLANTS_DATA.items()]
    selector = widgets.Dropdown(options=selector_options, value="1", layout=widgets.Layout(width='300px'))
    selector.observe(update_view, names='value')
    
    # Top Bar with Selector
    top_bar = widgets.HBox(
        [widgets.HTML("<span style='font-weight:600; color:#2c3e50; margin-right:10px;'>Select Plant:</span>"), selector], 
        layout=widgets.Layout(margin='0 0 20px 0')
    )
    
    # Initial render
    update_view()
    
    return widgets.VBox([top_bar, content])
