
import ipywidgets as widgets

def create_image_upload_card():
    return widgets.HTML("""
    <div class='card'>
        <div class='card-title'>Plant Image</div>
        <div style='background: #d5f5e3; border-radius: 12px; height: 300px; display: flex; align-items: center; justify-content: center; font-size: 80px; margin-bottom: 20px;'>
            🌿
        </div>
        <div style='display: flex; gap: 10px;'>
            <button class='btn btn-primary btn-full'>⬆ Upload Image</button>
            <button class='btn btn-outline btn-full'>📷 Take Photo</button>
        </div>
    </div>
    """)

def create_results_card(data):
    issues_html = ""
    for issue in data['issues']:
        issues_html += f"""
        <div style='background: {issue['bg']}; border-left: 4px solid {issue['color']}; padding: 12px; border-radius: 8px; margin-bottom: 10px;'>
            <div style='font-weight: 600; color: #2c3e50; display: flex; align-items: center; gap: 8px;'>
                <span>{issue['icon']}</span> {issue['title']}
            </div>
            <div style='font-size: 13px; color: #7f8c8d; margin-top: 4px;'>{issue['desc']}</div>
        </div>
        """
    
    recs_html = ""
    for rec in data['recommendations']:
        recs_html += f"<li>{rec}</li>"
        
    return widgets.HTML(f"""
    <div class='card'>
        <div class='card-title'>Analysis Results</div>
        
        <div style='margin-bottom: 20px;'>
            <div style='font-size: 12px; color: #7f8c8d; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;'>Detected Issues</div>
            {issues_html}
        </div>
        
        <div style='margin-bottom: 20px;'>
            <div style='font-size: 12px; color: #7f8c8d; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;'>Confidence</div>
            <div style='display: flex; align-items: center; gap: 10px;'>
                <div style='flex: 1; height: 8px; background: #eee; border-radius: 4px; overflow: hidden;'>
                    <div style='width: {data['confidence']}%; height: 100%; background: #2ecc71;'></div>
                </div>
                <div style='font-weight: 600; font-size: 13px;'>{data['confidence']}%</div>
            </div>
        </div>
        
        <div>
            <div style='font-size: 12px; color: #7f8c8d; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;'>Recommendations</div>
            <ul style='padding-left: 20px; font-size: 14px; color: #2c3e50; line-height: 1.6;'>
                {recs_html}
            </ul>
        </div>
        
        <div style='display: flex; gap: 10px; margin-top: 20px;'>
            <button class='btn btn-primary btn-full'>Run New Analysis</button>
            <button class='btn btn-outline btn-full'>📄 Generate PDF</button>
        </div>
    </div>
    """)
