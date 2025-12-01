
import ipywidgets as widgets
from IPython.display import display, HTML
from utils.styles import GLOBAL_CSS
from components.header import Navigation

# Import Pages (We will create these next)
# from pages.home.page import render as render_home
# from pages.sensors.page import render as render_sensors
# ...

class App:
    def __init__(self):
        self.content_area = widgets.Output()
        self.nav = Navigation(self.on_nav_change)
        
        # Header HTML (Brand part)
        self.brand = widgets.HTML("""
        <div class='brand'>
            <div class='brand-icon'>🌱</div>
            Smart Plant Monitor
        </div>
        """)
        
        # Combine Brand and Nav
        self.header = widgets.HBox(
            [self.brand, self.nav.widget], 
            layout=widgets.Layout(
                justify_content='space-between', 
                align_items='center',
                margin='0 0 20px 0',
                border_bottom='1px solid #eee',
                padding='0 0 10px 0'
            )
        )
        
        # Main Container
        self.container = widgets.VBox(
            [self.header, self.content_area]
        )
        self.container.add_class('dashboard-container')

    def on_nav_change(self, page_key):
        self.content_area.clear_output()
        with self.content_area:
            if page_key == "home":
                from pages.home.page import render
                display(render())
            elif page_key == "sensors":
                from pages.sensors.page import render
                display(render())
            elif page_key == "analysis":
                from pages.analysis.page import render
                display(render())
            elif page_key == "chat":
                from pages.chat.page import render
                display(render())
            elif page_key == "rewards":
                from pages.rewards.page import render
                display(render())
            elif page_key == "alerts":
                from pages.alerts.page import render
                display(render())
            else:
                print(f"Page {page_key} not implemented yet.")

    def run(self):
        display(HTML(GLOBAL_CSS))
        
        # Add some specific CSS for the ToggleButtons to match the design
        display(HTML("""
        <style>
            .custom-nav .widget-toggle-button {
                background: transparent !important;
                border: none !important;
                color: #7f8c8d !important;
                font-weight: 500 !important;
                box-shadow: none !important;
            }
            .custom-nav .widget-toggle-button.mod-active {
                background: #d1f2eb !important;
                color: #27ae60 !important;
                border-radius: 20px !important;
                font-weight: 700 !important;
            }
        </style>
        """))
        
        display(self.container)
        # Load initial page
        self.on_nav_change("home")

if __name__ == "__main__":
    app = App()
    app.run()
