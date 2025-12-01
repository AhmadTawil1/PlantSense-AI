
import ipywidgets as widgets

def create_filters():
    severity = widgets.Dropdown(options=['All Severities', 'High', 'Medium', 'Low'], value='All Severities', layout=widgets.Layout(width='150px'))
    types = widgets.Dropdown(options=['All Types', 'Water', 'Light', 'Temperature'], value='All Types', layout=widgets.Layout(width='150px'))
    mark_read = widgets.Button(description="Mark All Read", layout=widgets.Layout(width='auto'))
    
    # We wrap standard widgets in a card-like container using VBox/HBox styling
    # But to match design exactly, we might need HTML wrapper or just use the widgets directly.
    # Let's use a simple HBox for filters.
    
    return widgets.HBox(
        [widgets.Label("Filters:", layout=widgets.Layout(margin='0 10px 0 0')), severity, types, mark_read],
        layout=widgets.Layout(
            background_color='white',
            padding='15px',
            border='1px solid #eee',
            border_radius='12px',
            margin='0 0 20px 0',
            justify_content='flex-start',
            align_items='center'
        )
    )

def create_alert_card(data):
    title = data['title']
    msg = data['msg']
    time = data['time']
    severity = data['severity']
    action_label = data.get('action')

    # Severity: warning, info, success
    colors = {
        "warning": {"bg": "#fef9e7", "border": "#f1c40f", "icon": "⚠️"},
        "info": {"bg": "#e8f8f5", "border": "#3498db", "icon": "ℹ️"},
        "success": {"bg": "#eafaf1", "border": "#27ae60", "icon": "✓"}
    }
    
    style = colors.get(severity, colors["info"])
    
    action_btn = ""
    if action_label:
        action_btn = f"<button style='background: white; border: 1px solid #ddd; padding: 6px 12px; border-radius: 6px; cursor: pointer; color: #2c3e50; font-size: 12px; margin-top: 10px;'>{action_label}</button>"
        
    return widgets.HTML(f"""
    <div style='background: {style['bg']}; border: 1px solid {style['bg']}; border-left: 4px solid {style['border']}; border-radius: 12px; padding: 20px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between;'>
        <div>
            <div style='display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;'>
                <div style='font-weight: 600; color: #2c3e50; display: flex; gap: 10px; align-items: center;'>
                    <span style='font-size: 18px;'>{style['icon']}</span> {title}
                </div>
                <div style='font-size: 12px; color: #7f8c8d;'>{time}</div>
            </div>
            <div style='font-size: 13px; color: #7f8c8d; margin-left: 30px;'>{msg}</div>
        </div>
        <div style='margin-left: 30px;'>
            {action_btn}
        </div>
    </div>
    """)
