
import ipywidgets as widgets

def create_gauge(data):
    title = data['title']
    value = data['value']
    unit = data['unit']
    min_val = data['min']
    max_val = data['max']
    color = data['color']
    target_range = data['target']
    
    percent = int(((value - min_val) / (max_val - min_val)) * 100)
    percent = max(0, min(100, percent))
    
    dash_array = f"{percent}, 100"
    
    svg = f"""
    <svg viewBox="0 0 36 36" style="display: block; margin: 0 auto; max-width: 150px;">
      <path style="fill: none; stroke: #eee; stroke-width: 3;"
        d="M18 2.0845
          a 15.9155 15.9155 0 0 1 0 31.831
          a 15.9155 15.9155 0 0 1 0 -31.831"
      />
      <path style="fill: none; stroke-width: 3; stroke-linecap: round; animation: progress 1s ease-out forwards;"
        stroke="{color}"
        stroke-dasharray="{dash_array}"
        d="M18 2.0845
          a 15.9155 15.9155 0 0 1 0 31.831
          a 15.9155 15.9155 0 0 1 0 -31.831"
      />
      <text x="18" y="20" style="fill: #2c3e50; font-family: 'Inter', sans-serif; font-weight: bold; font-size: 0.5em; text-anchor: middle;">{value}{unit}</text>
      <text x="18" y="25" style="fill: #7f8c8d; font-family: 'Inter', sans-serif; font-size: 0.15em; text-anchor: middle;">Optimal</text>
    </svg>
    """
    
    return widgets.HTML(f"""
    <div class='card'>
        <div class='card-title'>{title}</div>
        <div style='display: flex; flex-direction: column; align-items: center; justify-content: center; height: 180px;'>
            {svg}
            <div style='background: #f8f9fa; padding: 4px 12px; border-radius: 12px; font-size: 12px; color: #7f8c8d; margin-top: 10px;'>
                Target: {target_range}
            </div>
        </div>
    </div>
    """)

def create_history_chart(data):
    points_moisture = data['moisture_points']
    points_temp = data['temp_points']
    
    svg = f"""
    <svg viewBox="0 0 400 100" style="width: 100%; height: 200px; overflow: visible;">
        <!-- Grid -->
        <line x1="0" y1="0" x2="400" y2="0" stroke="#eee" stroke-width="1" />
        <line x1="0" y1="25" x2="400" y2="25" stroke="#eee" stroke-width="1" stroke-dasharray="4" />
        <line x1="0" y1="50" x2="400" y2="50" stroke="#eee" stroke-width="1" stroke-dasharray="4" />
        <line x1="0" y1="75" x2="400" y2="75" stroke="#eee" stroke-width="1" stroke-dasharray="4" />
        <line x1="0" y1="100" x2="400" y2="100" stroke="#eee" stroke-width="1" />
        
        <!-- Lines -->
        <polyline points="{points_moisture}" fill="none" stroke="#2ecc71" stroke-width="2" />
        <polyline points="{points_temp}" fill="none" stroke="#3498db" stroke-width="2" />
        
        <!-- Labels -->
        <text x="0" y="115" fill="#999" font-size="10">00:00</text>
        <text x="100" y="115" fill="#999" font-size="10">04:00</text>
        <text x="200" y="115" fill="#999" font-size="10">08:00</text>
        <text x="300" y="115" fill="#999" font-size="10">12:00</text>
        <text x="380" y="115" fill="#999" font-size="10">16:00</text>
    </svg>
    """
    
    return widgets.HTML(f"""
    <div class='card'>
        <div class='card-title'>24-Hour History</div>
        <div style='padding: 20px 0;'>
            {svg}
        </div>
    </div>
    """)

def create_summary_card(data):
    return widgets.HTML(f"""
    <div class='card'>
        <div class='card-title'>Summary</div>
        <div style='margin-bottom: 20px;'>
            <div style='font-size: 12px; color: #7f8c8d;'>Last Updated</div>
            <div style='font-weight: 600;'>{data['last_updated']}</div>
        </div>
        <div style='margin-bottom: 20px;'>
            <div style='font-size: 12px; color: #7f8c8d;'>Data Points</div>
            <div style='font-weight: 600;'>{data['data_points']}</div>
        </div>
        <div>
            <div style='font-size: 12px; color: #7f8c8d;'>Overall Status</div>
            <div class='status-badge badge-success' style='display: inline-block; margin-top: 5px;'>{data['status']}</div>
        </div>
    </div>
    """)
