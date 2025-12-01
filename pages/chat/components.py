
import ipywidgets as widgets

def create_chat_area(messages):
    chat_html = ""
    for msg in messages:
        if msg['role'] == 'ai':
            chat_html += f"""
            <div style='display: flex; gap: 12px; margin-bottom: 20px;'>
                <div style='width: 32px; height: 32px; background: #2ecc71; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; flex-shrink: 0;'>🤖</div>
                <div style='background: #e8f8f5; padding: 12px 16px; border-radius: 0 12px 12px 12px; max-width: 80%; color: #2c3e50; font-size: 14px; line-height: 1.5;'>
                    {msg['content']}
                </div>
            </div>
            """
        else:
            chat_html += f"""
            <div style='display: flex; justify-content: flex-end; margin-bottom: 20px;'>
                <div style='background: #2ecc71; color: white; padding: 12px 16px; border-radius: 12px 12px 0 12px; max-width: 80%; font-size: 14px;'>
                    {msg['content']}
                </div>
            </div>
            """
            
    return widgets.HTML(f"""
    <div class='card' style='height: 600px; display: flex; flex-direction: column;'>
        <div class='card-title'>AI Plant Assistant</div>
        <div style='flex: 1; overflow-y: auto; padding-right: 10px;'>
            {chat_html}
        </div>
        <div style='margin-top: 20px; display: flex; gap: 10px;'>
            <input type='text' placeholder='Ask me anything about your plant...' style='flex: 1; padding: 10px 15px; border: 1px solid #ddd; border-radius: 8px; outline: none;'>
            <button class='btn btn-primary' style='width: 40px; padding: 0;'>➤</button>
        </div>
    </div>
    """)

def create_context_card(data):
    return widgets.HTML(f"""
    <div class='card'>
        <div class='card-title'>Plant Context</div>
        <div style='margin-bottom: 15px;'>
            <div style='font-size: 12px; color: #7f8c8d;'>Moisture</div>
            <div class='status-badge badge-success' style='display: inline-block; margin-top: 4px;'>{data['moisture']}</div>
        </div>
        <div style='margin-bottom: 15px;'>
            <div style='font-size: 12px; color: #7f8c8d;'>Temperature</div>
            <div class='status-badge badge-success' style='display: inline-block; margin-top: 4px;'>{data['temperature']}</div>
        </div>
        <div>
            <div style='font-size: 12px; color: #7f8c8d;'>Plant Type</div>
            <div style='background: #eee; padding: 4px 8px; border-radius: 12px; font-size: 12px; display: inline-block; margin-top: 4px;'>{data['plant_type']}</div>
        </div>
    </div>
    """)

def create_suggestions_card(questions):
    btns = ""
    for q in questions:
        btns += f"<button class='btn btn-outline btn-full' style='margin-bottom: 8px; text-align: left; justify-content: flex-start; font-weight: 400;'>{q}</button>"
        
    return widgets.HTML(f"""
    <div class='card'>
        <div class='card-title'>Suggested Questions</div>
        {btns}
    </div>
    """)
