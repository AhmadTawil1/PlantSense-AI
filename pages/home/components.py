
import ipywidgets as widgets

def create_plant_card(plant):
    return widgets.HTML(f"""
    <div class='card'>
        <div class='card-title'>Current Plant</div>
        <div class='plant-image-box' style='background: #d5f5e3; border-radius: 12px; height: 180px; display: flex; align-items: center; justify-content: center; font-size: 80px; margin-bottom: 16px;'>
            {plant['emoji']}
        </div>
        <div class='plant-name' style='font-size: 18px; font-weight: 700; color: #2c3e50;'>{plant['name']}</div>
        <div class='plant-type' style='font-size: 13px; color: #7f8c8d;'>{plant['type']}</div>
    </div>
    """)

def create_health_card(plant):
    score = plant['health']
    color = "#2ecc71" if score > 80 else "#f1c40f" if score > 50 else "#e74c3c"
    dash_array = f"{score}, 100"
    
    svg = f"""
    <svg viewBox="0 0 36 36" style="display: block; margin: 0 auto; max-width: 80%; max-height: 250px;">
      <path style="fill: none; stroke: #eee; stroke-width: 3.8;"
        d="M18 2.0845
          a 15.9155 15.9155 0 0 1 0 31.831
          a 15.9155 15.9155 0 0 1 0 -31.831"
      />
      <path style="fill: none; stroke-width: 2.8; stroke-linecap: round; animation: progress 1s ease-out forwards;"
        stroke="{color}"
        stroke-dasharray="{dash_array}"
        d="M18 2.0845
          a 15.9155 15.9155 0 0 1 0 31.831
          a 15.9155 15.9155 0 0 1 0 -31.831"
      />
      <text x="18" y="20.35" style="fill: #2ecc71; font-family: 'Inter', sans-serif; font-weight: bold; font-size: 0.5em; text-anchor: middle;">{score}</text>
      <text x="18" y="25" style="fill: #7f8c8d; font-family: 'Inter', sans-serif; font-size: 0.15em; text-anchor: middle;">{plant['health_label']}</text>
    </svg>
    """
    
    return widgets.HTML(f"""
    <div class='card'>
        <div class='card-title'>Plant Health</div>
        <div style='display: flex; align-items: center; justify-content: center; height: 240px;'>
            {svg}
        </div>
    </div>
    """)

def create_sensor_card(plant):
    rows = ""
    for s in plant['sensors']:
        rows += f"""
        <div style='background: #e8f8f5; padding: 12px 16px; border-radius: 10px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;'>
            <div style='display: flex; align-items: center; gap: 10px; font-weight: 500; color: #2c3e50;'>
                <span>{s['icon']}</span> {s['name']}
            </div>
            <div style='font-weight: 600; display: flex; align-items: center; gap: 8px;'>
                {s['value']} <div style='width: 8px; height: 8px; border-radius: 50%; background: #27ae60;'></div>
            </div>
        </div>
        """
    
    return widgets.HTML(f"""
    <div class='card'>
        <div class='card-title'>Sensor Status</div>
        {rows}
    </div>
    """)

def create_alerts_card(plant):
    rows = ""
    for a in plant['alerts']:
        icon = "⚠️" if a['type'] == 'warning' else "✓"
        bg_color = "#fef9e7" if a['type'] == 'warning' else "#eafaf1"
        border_color = "#f1c40f" if a['type'] == 'warning' else "#27ae60"
        
        rows += f"""
        <div style='padding: 12px; border-radius: 8px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: flex-start; background: {bg_color}; border-left: 4px solid {border_color};'>
            <div style='display: flex; gap: 10px;'>
                <div style='font-size:16px;'>{icon}</div>
                <div>
                    <div style='font-weight:600; font-size:13px;'>{a['msg']}</div>
                    <div style='font-size:11px; color:#666;'>{a['sub']}</div>
                </div>
            </div>
            <div style='font-size: 11px; color: #7f8c8d; white-space: nowrap;'>{a['time']}</div>
        </div>
        """
    
    return widgets.HTML(f"""
    <div class='card'>
        <div class='card-title'>Recent Alerts</div>
        {rows}
    </div>
    """)

def create_actions_card():
    # We use HTML buttons here for visual consistency with the design
    return widgets.HTML("""
    <div class='card'>
        <div class='card-title'>Quick Actions</div>
        <div style='display: flex; gap: 12px; margin-top: 10px;'>
            <button class='btn btn-primary' style='flex:1;'>⚡ View Sensors</button>
            <button class='btn btn-outline' style='flex:1;'>📷 Analyze Image</button>
            <button class='btn btn-outline' style='flex:1;'>💬 Ask AI</button>
        </div>
    </div>
    """)
