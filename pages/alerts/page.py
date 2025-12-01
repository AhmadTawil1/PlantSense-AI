
import ipywidgets as widgets
from .data import ALERTS_LIST
from .components import create_filters, create_alert_card

def render():
    # Filters (Using HTML for better styling control to match the card look)
    # We use the component we created, but maybe wrap it or use the HTML version if we prefer
    # Let's use a pure HTML version for the filters to match the design exactly as shown in the image
    filters = widgets.HTML("""
    <div class='card' style='display: flex; justify-content: space-between; align-items: center; padding: 15px 20px; margin-bottom: 20px;'>
        <div style='display: flex; align-items: center; gap: 15px;'>
            <span style='font-weight: 600;'>Filters:</span>
            <select style='padding: 6px 12px; border: 1px solid #ddd; border-radius: 6px; background: #f8f9fa; outline: none;'><option>All Severities</option></select>
            <select style='padding: 6px 12px; border: 1px solid #ddd; border-radius: 6px; background: #f8f9fa; outline: none;'><option>All Types</option></select>
        </div>
        <button style='background: white; border: 1px solid #ddd; padding: 6px 12px; border-radius: 6px; cursor: pointer;'>Mark All Read</button>
    </div>
    """)
    
    # Alerts Grid
    alert_cards = [create_alert_card(a) for a in ALERTS_LIST]
    
    grid = widgets.GridBox(alert_cards, layout=widgets.Layout(grid_template_columns='1fr 1fr', grid_gap='20px'))
    
    return widgets.VBox([filters, grid])
