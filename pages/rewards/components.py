
import ipywidgets as widgets

def create_level_card(data):
    percent = int((data['current_xp'] / data['next_level_xp']) * 100)
    
    return widgets.HTML(f"""
    <div class='card'>
        <div class='card-title'>Your Level</div>
        <div style='display: flex; align-items: center; gap: 20px;'>
            <div style='width: 80px; height: 80px; background: #2ecc71; border-radius: 50%; display: flex; flex-direction: column; align-items: center; justify-content: center; color: white; box-shadow: 0 4px 10px rgba(46, 204, 113, 0.3);'>
                <div style='font-size: 24px; font-weight: 700;'>{data['level']}</div>
                <div style='font-size: 12px;'>Level</div>
            </div>
            <div style='flex: 1;'>
                <div style='display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 8px;'>
                    <span style='font-weight: 600;'>{data['current_xp']:,} XP</span>
                    <span style='color: #7f8c8d;'>{data['next_level_xp']:,} XP</span>
                </div>
                <div style='height: 8px; background: #eee; border-radius: 4px; overflow: hidden;'>
                    <div style='width: {percent}%; height: 100%; background: #2ecc71;'></div>
                </div>
                <div style='font-size: 12px; color: #7f8c8d; margin-top: 8px;'>{data['next_level_remaining']} XP to Level {data['level'] + 1}</div>
            </div>
        </div>
    </div>
    """)

def create_missions_card(missions):
    rows = ""
    for m in missions:
        bg = "#d5f5e3" if m['done'] else "transparent"
        icon = "⚡" if m['done'] else "◎"
        color = "#27ae60" if m['done'] else "#2c3e50"
        
        rows += f"""
        <div style='display: flex; justify-content: space-between; align-items: center; padding: 12px; border-radius: 8px; background: {bg}; margin-bottom: 10px;'>
            <div style='display: flex; align-items: center; gap: 10px; color: {color};'>
                <span>{icon}</span> {m['task']}
            </div>
            <div style='font-size: 12px; font-weight: 600; color: {color}; opacity: 0.7;'>{m['progress']}</div>
        </div>
        """
        
    return widgets.HTML(f"""
    <div class='card'>
        <div class='card-title'>Daily Missions</div>
        {rows}
    </div>
    """)

def create_achievements_card(badges):
    grid_items = ""
    for b in badges:
        opacity = "1" if b['earned'] else "0.4"
        bg = "#d5f5e3" if b['earned'] else "#f8f9fa"
        
        grid_items += f"""
        <div style='background: {bg}; border-radius: 12px; padding: 15px; text-align: center; opacity: {opacity};'>
            <div style='font-size: 24px; margin-bottom: 5px;'>{b['icon']}</div>
            <div style='font-size: 11px; font-weight: 600; color: #2c3e50;'>{b['name']}</div>
        </div>
        """
        
    return widgets.HTML(f"""
    <div class='card'>
        <div class='card-title'>Recent Achievements</div>
        <div style='display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;'>
            {grid_items}
        </div>
    </div>
    """)

def create_streak_card(data):
    day_html = ""
    for d in data['days']:
        bg = "#d5f5e3" if d == "✓" else "#f8f9fa"
        color = "#27ae60" if d == "✓" else "#bdc3c7"
        day_html += f"<div style='width: 30px; height: 30px; background: {bg}; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: {color}; font-weight: bold;'>{d}</div>"
        
    return widgets.HTML(f"""
    <div class='card' style='display: flex; justify-content: space-between; align-items: center;'>
        <div>
            <div style='font-weight: 600; color: #2c3e50; display: flex; align-items: center; gap: 10px;'>
                <span style='font-size: 24px; color: #2ecc71;'>🎖️</span> Daily Care Streak
            </div>
            <div style='font-size: 12px; color: #7f8c8d; margin-top: 4px;'>Keep it up! Your plant is thriving.</div>
        </div>
        <div style='display: flex; gap: 8px;'>
            {day_html}
        </div>
        <div style='background: #e8f8f5; padding: 6px 12px; border-radius: 20px; color: #27ae60; font-weight: 700;'>
            {data['count']} Days 🔥
        </div>
    </div>
    """)
