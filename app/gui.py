from PyQt6 import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


dark_theme = {
    "bg_color": "#202020", #dark grey
    "button color": "#444444",
    "button_active_color": "#555555",
    "font_color": "#ffffff",
    "home_logo": "pictures\maison_white.png",
    "tasks_logo": "pictures\todo_white.png",
    "calendar_logo": "pictures\calendar_white.png",
    "settings_logo": "pictures\settings_white.png",
    "completed_logo": "pictures\done_white.png",
    "menu_logo": "pictures\menu_white.png",
    "add_logo": "pictures\add_white.png",
    #add delete when tasks are implemented
    "theme_logo": "pictures\sun.png",
    "important_logo": "pictures\important_white.png"
}

light_theme = {
    "bg_color": "#f0f0f0", #light grey
    "button_color": "#ffffff", #white
    "tertiary_color": "#f0f0f0", 
    "font_color": "#000000", #black
    "home_logo": "pictures\maison.png",
    "tasks_logo": "pictures\todo_black.png",
    "calendar_logo": "pictures\calendar_black.png",
    "settings_logo": "pictures\settings_black.png",
    "completed_logo": "pictures\done_black.png",
    "menu_logo": "pictures\menu_black.png",
    "add_logo": "pictures\add_black.png",
    #add delete when tasks are implemented
    "theme_logo": "pictures\moon.png",
    "important_logo": "pictures\important_black.png"
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
        self.sidebar.minimumWidth = 55
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
        self.toggle_sidebar_button = QPushButton(icon=QIcon("pictures\menu.png"), text="Collapse")
        self.toggle_sidebar_button.setIcon(QIcon("pictures\menu.png"))
        self.toggle_sidebar_button.setStyleSheet(f"background-color: RED")
        self.toggle_sidebar_button.clicked.connect(self.toggle_sidebar)
        sidebar_layout.addWidget(self.toggle_sidebar_button)

        #sidebar buttons, will be in sidebar container
        self.home_button = QPushButton(icon=QIcon("pictures\maison.png"), text="Home")
        self.home_button.setStyleSheet(f"background-color: {theme['button_color']}")
        sidebar_layout.addWidget(self.home_button)

        self.tasks_button = QPushButton(icon=QIcon("pictures\liste.png"), text="Tasks")
        self.tasks_button.setStyleSheet(f"background-color: {theme['button_color']}")
        sidebar_layout.addWidget(self.tasks_button)

        self.completed_button = QPushButton(icon=QIcon("pictures\liste.png"),text="Completed Tasks")
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


        #check if sidebar is out or not
        self.sidebar_out = True

    def set_theme(self, theme):
        #change the theme of the app
        pass

    def toggle_sidebar(self):
        #hide or show the sidebar
        if self.sidebar_out:
            self.sidebar.setFixedWidth(50)
            self.sidebar_out = False
            for button in self.sidebar.children():
                if isinstance(button, QPushButton):
                    button.setText("")
        elif self.sidebar_out == False:
            self.sidebar.setFixedWidth(200)
            self.sidebar_out = True
            self.toggle_sidebar_button.setText("Collapse")
            self.home_button.setText("Home")
            self.tasks_button.setText("Tasks")
            self.completed_button.setText("Completed Tasks")
            self.calendar_button.setText("Calendar")
            self.settings_button.setText("Settings")
        pass

        
