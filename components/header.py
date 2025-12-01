
import ipywidgets as widgets

class Header:
    def __init__(self, on_nav_click):
        self.on_nav_click = on_nav_click
        self.active_page = "home"
        self.nav_items = {
            "home": "🏠 Home",
            "sensors": "📈 Sensors",
            "analysis": "📊 Analysis",
            "chat": "💬 AI Chat",
            "rewards": "🏆 Rewards",
            "alerts": "🔔 Alerts"
        }
        self.widget = widgets.HTML()
        self.render()

    def set_active(self, page_key):
        self.active_page = page_key
        self.render()

    def render(self):
        nav_html = ""
        for key, label in self.nav_items.items():
            active_class = "active" if key == self.active_page else ""
            # We use a custom onclick handler mechanism via the main app loop or 
            # since we can't easily bind JS events back to Python in standard HTML widgets without custom jslink,
            # we will use a workaround: The main app will render buttons or we use a different approach.
            # 
            # BETTER APPROACH for ipywidgets: Use Button widgets styled as links or text, 
            # but to match the exact CSS design, we might need to use a HBox of Buttons/HTML.
            #
            # However, to keep the "HTML" look from the design, we'll use a trick:
            # We will render the HTML for the header, but the actual navigation might need to be 
            # handled by a separate hidden control or we just use standard ipywidgets Buttons styled with CSS.
            pass

        # Re-thinking: To make "divs" clickable and call Python, we need `ipyevents` or standard Buttons.
        # Standard Buttons are easiest. Let's style them to look like the nav items.
        pass

    def create_widget(self):
        # Brand
        brand = widgets.HTML("""
        <div class='brand'>
            <div class='brand-icon'>🌱</div>
            Smart Plant Monitor
        </div>
        """)

        # Nav Buttons
        self.buttons = []
        for key, label in self.nav_items.items():
            btn = widgets.Button(description=label.split(" ")[1], icon=label.split(" ")[0])
            btn.layout.width = 'auto'
            btn.add_class('nav-item') # We need to override the default button styles in CSS
            # We'll use a special class to style these buttons to look like the design
            btn.style.button_style = '' # Reset
            btn.on_click(lambda b, k=key: self.on_nav_click(k))
            self.buttons.append(btn)
        
        # We need to inject some specific CSS to make ipywidgets buttons look like our div nav items
        # This is a bit hacky but works. Or we can just use the HTML header and rely on a simpler tab system?
        # Let's stick to the visual design.
        
        # Alternative: Use a ToggleButtons widget? It has an 'active' state built-in.
        # But styling is harder.
        
        # Let's go with a HBox of Buttons and style them.
        nav_box = widgets.HBox(self.buttons, layout=widgets.Layout(grid_gap='10px'))
        
        header_box = widgets.HBox([brand, nav_box], layout=widgets.Layout(
            justify_content='space-between', 
            align_items='center',
            border_bottom='1px solid #eee',
            padding='0 0 16px 0',
            margin='0 0 24px 0'
        ))
        
        return header_box

    def update_active_state(self, page_key):
        # Update button styles
        for btn in self.buttons:
            # This is tricky with standard buttons. We might need to add/remove classes.
            # ipywidgets 8.x supports add_class/remove_class dynamically.
            # Assuming we are on a version that supports it.
            key = [k for k, v in self.nav_items.items() if v.split(" ")[1] == btn.description][0]
            if key == page_key:
                btn.add_class('active')
            else:
                btn.remove_class('active')

# Redefining to use a simpler approach compatible with the CSS we wrote:
# We will use the HTML header for display, but for interaction, we might have to compromise 
# OR use the ToggleButtons which is robust.
# Let's use ToggleButtons for the Menu to ensure functionality, and style it.

class Navigation:
    def __init__(self, on_change):
        self.options = [
            ("🏠 Home", "home"),
            ("📈 Sensors", "sensors"),
            ("📊 Analysis", "analysis"),
            ("💬 AI Chat", "chat"),
            ("🏆 Rewards", "rewards"),
            ("🔔 Alerts", "alerts")
        ]
        self.widget = widgets.ToggleButtons(
            options=self.options,
            value="home",
            style={'button_width': 'auto'},
            layout=widgets.Layout(width='auto')
        )
        self.widget.observe(lambda change: on_change(change['new']), names='value')
        
        # We will add a custom class to this widget to style it like the nav menu
        self.widget.add_class('custom-nav')

