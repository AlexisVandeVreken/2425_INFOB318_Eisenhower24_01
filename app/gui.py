from PyQt6 import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

light_theme = {
    "bg_color": "#f0f0f0", #light grey
    "button_color": "#ffffff", #white
    "tertiary_color": "#f0f0f0", 
    "font_color": "#000000", #black
}
dark_theme = {
    "bg_color": "#202020", #dark grey
    "button color": "#444444",
    "button_active_color": "#555555",
    "font_color": "#ffffff",
}

theme = light_theme

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager with Eisenhower Matrix")
        self.setGeometry(100, 100, 800, 600)

        #all window container
        self.window = QWidget()
        self.window.setStyleSheet(f"background-color: {theme['bg_color']}")
        self.setCentralWidget(self.window)
        main_layout = QHBoxLayout()
        self.window.setLayout(main_layout)

        #sidebar container, will be in all window
        self.sidebar = QWidget()
        self.sidebar.setStyleSheet(f"background-color: {theme['tertiary_color']}")
        sidebar_layout = QVBoxLayout()
        self.sidebar.setLayout(sidebar_layout)
        self.sidebar.setFixedWidth(200)
        self.sidebar.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.sidebar)
        
        #main content container, will be in all window
        self.main_content = QWidget()
        self.main_content.setStyleSheet("background-color: RED")
        main_content_layout = QGridLayout()
        self.main_content.setLayout(main_content_layout)
        main_layout.addWidget(self.main_content)

        #button to toggle sidebar, will be in sidebar container
        self.toggle_sidebar_button = QPushButton(">")
        self.toggle_sidebar_button.setStyleSheet(f"background-color: RED")
        self.toggle_sidebar_button.clicked.connect(self.toggle_sidebar)
        sidebar_layout.addWidget(self.toggle_sidebar_button)

        #sidebar buttons, will be in sidebar container
        self.home_button = QPushButton("Home")
        self.home_button.setStyleSheet(f"background-color: {theme['button_color']}")
        sidebar_layout.addWidget(self.home_button)

        self.tasks_button = QPushButton("Tasks")
        self.tasks_button.setStyleSheet(f"background-color: {theme['button_color']}")
        sidebar_layout.addWidget(self.tasks_button)

        self.completed_button = QPushButton("Completed Tasks")
        self.completed_button.setStyleSheet(f"background-color: {theme['button_color']}")
        sidebar_layout.addWidget(self.completed_button)

        self.calendar_button = QPushButton("Calendar") 
        self.calendar_button.setStyleSheet(f"background-color: {theme['button_color']}")
        sidebar_layout.addWidget(self.calendar_button)

        self.settings_button = QPushButton("Settings")
        self.settings_button.setStyleSheet(f"background-color: {theme['button_color']}")
        sidebar_layout.addWidget(self.settings_button)

        #button to change theme, will be in sidebar container
        self.change_theme_button = QPushButton("*")
        self.change_theme_button.setStyleSheet(f"background-color: GREEN")
        self.change_theme_button.clicked.connect(self.set_theme)
        sidebar_layout.addWidget(self.change_theme_button)

        #button to add task, will be in main content container



    def set_theme(self, theme):
        #change the theme of the app
        pass

    def toggle_sidebar(self):
        #hide or show the sidebar
        pass

        
