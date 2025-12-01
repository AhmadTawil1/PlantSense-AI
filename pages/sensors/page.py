
import ipywidgets as widgets
from .data import SENSORS_DATA, HISTORY_DATA, SUMMARY_DATA
from .components import create_gauge, create_history_chart, create_summary_card

def render():
    # Gauges
    gauges = [create_gauge(d) for d in SENSORS_DATA]
    
    top_row = widgets.GridBox(gauges, layout=widgets.Layout(grid_template_columns='1fr 1fr 1fr', grid_gap='20px', margin='0 0 20px 0'))
    
    # Bottom Row
    chart = create_history_chart(HISTORY_DATA)
    summary = create_summary_card(SUMMARY_DATA)
    
    bottom_row = widgets.GridBox([chart, summary], layout=widgets.Layout(grid_template_columns='3fr 1fr', grid_gap='20px'))
    
    return widgets.VBox([top_row, bottom_row])
