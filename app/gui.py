from PyQt6 import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QColor


dark_theme = {
    "bg_color": "#202020", #dark grey
    "button_color": "#444444", #grey 
    "button_hover_color": "#05b0ec", #blue
    "button_active_color": "#05b0ec", #blue
    "font_color": "#ffffff", #white
    "button_font_color": "#ffffff", #white
    "button_font_hover_color": "#000000", #black
    #logos
    "home_logo": "pictures\maison_white.png",
    "tasks_logo": "pictures\\todo_white.png",
    "calendar_logo": "pictures\calendar_white.png",
    "settings_logo": "pictures\param_white.png",
    "done_logo": "pictures\done_white.png",
    "menu_logo": "pictures\menu_white.png",
    "add_logo": "pictures\\add_white.png",
    #add delete when tasks are implemented
    "theme_logo": "pictures\sun.png",
    "important_logo": "pictures\important_white.png"
}

light_theme = {
    "bg_color": "#dadada", #light grey
    "button_color": "#f0f0f0", #light grey
    "button_hover_color": "#05b0ec",
    "button_active_color": "#05b0ec", 
    "font_color": "#000000", #black
    "button_font_color": "#000000", #black
    "button_font_hover_color": "#000000",
    #logos
    "home_logo": "pictures\maison.png",
    "tasks_logo": "pictures\\todo_black.png",
    "calendar_logo": "pictures\calendar_black.png",
    "settings_logo": "pictures\param_black.png",
    "done_logo": "pictures\done_black.png",
    "menu_logo": "pictures\menu_black.png",
    "add_logo": "pictures\\add_black.png",
    #add delete when tasks are implemented
    "theme_logo": "pictures\moon.png",
    "important_logo": "pictures\important_black.png"
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sidebar_out = True
        self.dark_on = True
        self.theme =  dark_theme 
        #self.theme = light_theme

        self.setWindowTitle("Task Manager with Eisenhower Matrix")
        self.setGeometry(100, 100, 800, 600)

        #all window container
        self.window = QWidget()
        self.window.setStyleSheet(f"background-color: {self.theme['bg_color']}")
        self.setCentralWidget(self.window)
        main_layout = QHBoxLayout()
        self.window.setLayout(main_layout)

        #sidebar container, will be in all window
        self.sidebar = QWidget()
        #self.sidebar.setStyleSheet(f"background-color: {self.theme['bg_color']}")
        sidebar_layout = QVBoxLayout()
        self.sidebar.setLayout(sidebar_layout)
        main_layout.addWidget(self.sidebar)
        
        #main content container, will be in all window
        self.main_content = QWidget()
        self.main_content.setStyleSheet("background-color: RED")
        main_content_layout = QGridLayout()
        self.main_content.setLayout(main_content_layout)
        main_layout.addWidget(self.main_content)
        
        
        self.setStyleSheet("""
            QPushButton#sidebar_button{
                border: 1px solid green;
                background-color: green;
                padding: 0px 0px 0px 10px;
                font-size: 14px
            }
            #sidebar_button QPushButton:hover{
                border: 1px solid #05b0ec;
                background-color: #05b0ec;
                color: yellow;
            }
        """)

        #button to toggle sidebar, will be in sidebar container
        self.toggle_sidebar_button = QPushButton(icon=QIcon(self.theme["menu_logo"]), text="Collapse")
        self.toggle_sidebar_button.setStyleSheet(f"background-color: {self.theme['button_color']}; color: {self.theme['button_font_color']};")
        self.toggle_sidebar_button.setIconSize(QSize(40,40))
        self.toggle_sidebar_button.setObjectName("sidebar_button")
        self.toggle_sidebar_button.clicked.connect(self.toggle_sidebar)
        sidebar_layout.addWidget(self.toggle_sidebar_button)

        #home button, will be in sidebar container
        self.home_button = QPushButton(icon=QIcon(self.theme["home_logo"]), text="Home")
        self.home_button.setStyleSheet(f"background-color: {self.theme['button_color']}; color: {self.theme['button_font_color']};")
        self.home_button.setIconSize(QSize(40,40))
        self.home_button.setObjectName("sidebar_button")
        sidebar_layout.addWidget(self.home_button)

        #important tasks button, will be in sidebar container
        self.important_button = QPushButton(icon=QIcon(self.theme["important_logo"]), text="Important Tasks")
        self.important_button.setStyleSheet(f"background-color: {self.theme['button_color']}; color: {self.theme['button_font_color']};")
        self.important_button.setIconSize(QSize(40,40))
        self.important_button.setObjectName("sidebar_button")
        sidebar_layout.addWidget(self.important_button)

        #tasks button, will be in sidebar container
        self.tasks_button = QPushButton(icon=QIcon(self.theme["tasks_logo"]), text="Tasks")
        self.tasks_button.setStyleSheet(f"background-color: {self.theme['button_color']}; color: {self.theme['button_font_color']};")
        self.tasks_button.setIconSize(QSize(40,40))
        self.tasks_button.setObjectName("sidebar_button")
        sidebar_layout.addWidget(self.tasks_button)

        #completed tasks button, will be in sidebar container
        self.completed_button = QPushButton(icon=QIcon(self.theme["done_logo"]), text="Completed Tasks")
        self.completed_button.setStyleSheet(f"background-color: {self.theme['button_color']}; color: {self.theme['button_font_color']};")
        self.completed_button.setIconSize(QSize(40,40))
        self.completed_button.setObjectName("sidebar_button")
        sidebar_layout.addWidget(self.completed_button)

        #calendar button, will be in sidebar container
        self.calendar_button = QPushButton(icon=QIcon(self.theme["calendar_logo"]), text="Calendar")
        self.calendar_button.setStyleSheet(f"background-color: {self.theme['button_color']}; color: {self.theme['button_font_color']};")
        self.calendar_button.setIconSize(QSize(40,40))
        self.calendar_button.setObjectName("sidebar_button")
        sidebar_layout.addWidget(self.calendar_button)

        #change theme button, will be in sidebar container
        self.change_theme_button = QPushButton(icon=QIcon(self.theme["theme_logo"]), text="Change Theme")
        self.change_theme_button.setStyleSheet(f"background-color: {self.theme['button_color']}; color: {self.theme['button_font_color']};")
        self.change_theme_button.setIconSize(QSize(40,40))
        self.change_theme_button.setObjectName("sidebar_button")
        self.change_theme_button.clicked.connect(self.set_theme)
        sidebar_layout.addWidget(self.change_theme_button)

        #settings button, will be in sidebar container
        self.settings_button = QPushButton(icon=QIcon(self.theme["settings_logo"]), text="Settings")
        self.settings_button.setStyleSheet(f"background-color: {self.theme['button_color']}; color: {self.theme['button_font_color']};")
        self.settings_button.setIconSize(QSize(40,40))
        self.settings_button.setObjectName("sidebar_button")
        sidebar_layout.addWidget(self.settings_button)

        #Ratio for sidebar width
        self.sidebar_expanded_ratio = 0.12
        self.sidebar_collapsed_ratio = 0.05
        self.sidebar_out = True  # Start with expanded sidebar
        self.adjust_sidebar()
        self.all_buttons_list = [self.toggle_sidebar_button, self.home_button, self.tasks_button, 
                                 self.completed_button, self.calendar_button, self.settings_button, 
                                 self.change_theme_button, self.important_button]



    def toggle_sidebar(self):
        #hide or show the sidebar
        if self.sidebar_out:
            self.sidebar_out = False
            for button in self.sidebar.children():
                if isinstance(button, QPushButton):
                    button.setText("")
        elif self.sidebar_out == False:
            self.sidebar_out = True
            self.toggle_sidebar_button.setText("Collapse")
            self.home_button.setText("Home")
            self.tasks_button.setText("Tasks")
            self.completed_button.setText("Completed Tasks")
            self.calendar_button.setText("Calendar")
            self.settings_button.setText("Settings")
            self.change_theme_button.setText("Change Theme")
            self.important_button.setText("Important Tasks")
        self.adjust_sidebar()

    def adjust_sidebar(self):
        # Calculate width based on window size and sidebar state
        window_width = self.width()
        if self.sidebar_out:
            sidebar_width = int(window_width * self.sidebar_expanded_ratio) if window_width > 1375 else 165
        else:
            sidebar_width = int(window_width * self.sidebar_collapsed_ratio) if window_width > 1100 else 55

        self.sidebar.setFixedWidth(sidebar_width)

    def resizeEvent(self, event):
        # Ensure sidebar resizes proportionally with the window
        self.adjust_sidebar()
        super().resizeEvent(event)

    def set_theme(self):
        #change the theme of the app
        if self.dark_on == True:
            self.theme = light_theme
            self.dark_on = False
        elif self.dark_on == False:
            self.theme = dark_theme
            self.dark_on = True
        self.apply_theme()

    def apply_theme(self):
        self.window.setStyleSheet(f"background-color: {self.theme['bg_color']}")
        self.sidebar.setStyleSheet(f"background-color: {self.theme['bg_color']}")
        #make the changes for all the widgets and logos.
        self.toggle_sidebar_button.setIcon(QIcon(self.theme["menu_logo"]))
        self.home_button.setIcon(QIcon(self.theme["home_logo"]))
        self.tasks_button.setIcon(QIcon(self.theme["tasks_logo"]))
        self.completed_button.setIcon(QIcon(self.theme["done_logo"]))
        self.calendar_button.setIcon(QIcon(self.theme["calendar_logo"]))
        self.settings_button.setIcon(QIcon(self.theme["settings_logo"]))
        self.change_theme_button.setIcon(QIcon(self.theme["theme_logo"]))
        self.important_button.setIcon(QIcon(self.theme["important_logo"]))
        #self.add_button.setIcon(QIcon(self.theme["add_logo"]))

        for button in self.all_buttons_list:
            button.setStyleSheet(f"background-color: {self.theme['button_color']}")

