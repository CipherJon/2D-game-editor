# Configuration settings for the 2D Game Editor
# This file contains global and project-specific configurations.


class Config:
    def __init__(self):
        # Window settings
        self.window_title = "2D Game Editor"
        self.window_width = 1280
        self.window_height = 720
        self.window_resizable = True

        # Grid settings
        self.grid_enabled = True
        self.grid_cell_size = 32
        self.grid_color = (200, 200, 200, 100)

        # Default paths
        self.default_project_path = "projects/"
        self.default_assets_path = "resources/"

        # Editor settings
        self.max_undo_steps = 50
        self.auto_save_interval = 300  # 5 minutes in seconds


# Global configuration instance
config = Config()
