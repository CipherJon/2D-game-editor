# 2D Game Editor Architecture

## Overview
The 2D Game Editor is designed to provide a modular and extensible framework for creating 2D games. The architecture is divided into several key components, each responsible for a specific aspect of the editor's functionality.

## Core Components

### 1. Core Module (`src/core`)
The `core` module contains the fundamental systems and base classes that form the backbone of the editor.

- **`app.py`**: The main application class that manages the editor's lifecycle, including initialization, event handling, and rendering.
- **`config.py`**: Handles global and project-specific configurations, such as default settings and user preferences.
- **`events.py`**: Manages custom Pygame events and the event bus for inter-component communication.
- **`constants.py`**: Defines global constants used across the editor.
- **`types.py`**: Contains type aliases, `TypedDict`, and protocols for type safety and clarity.

### 2. Editor Module (`src/editor`)
The `editor` module contains the logic and UI components for the editor itself.

- **`editor_window.py`**: Composes the main editor window, including layout and panel management.
- **`tool_manager.py`**: Manages the switching and lifecycle of editor tools (e.g., brush, eraser, select).
- **`history.py`**: Implements the undo/redo system for user actions.
- **`selection.py`**: Handles selection logic for entities, tiles, and other editable elements.
- **`panels/`**: Contains individual UI panels for the editor:
  - **`hierarchy.py`**: Displays the scene hierarchy.
  - **`inspector.py`**: Shows properties of selected entities or tiles.
  - **`assets_browser.py`**: Manages and displays available assets.
  - **`tile_palette.py`**: Provides a palette for tile-based editing.
  - **`layer_panel.py`**: Controls layer visibility and ordering.
  - **`toolbar.py`**: Contains buttons and controls for tools and actions.

### 3. Scene Module (`src/scene`)
The `scene` module manages the data and serialization of game scenes.

- **`scene.py`**: The main container for scene data, including layers, entities, and tilemaps.
- **`layer.py`**: Defines the structure and behavior of layers within a scene.
- **`entity.py`**: Manages entities and their properties (if entity placement is supported).
- **`tilemap.py`**: Handles tilemap data and operations.
- **`scene_serializer.py`**: Implements saving and loading logic for scenes.

### 4. Rendering Module (`src/rendering`)
The `rendering` module is responsible for all drawing and camera-related functionality.

- **`camera.py`**: Manages the view and navigation of the scene.
- **`renderer.py`**: Provides high-level drawing helpers for rendering the scene.
- **`grid_renderer.py`**: Renders the grid for tile-based editing.
- **`gizmos.py`**: Draws transform and selection gizmos for visual feedback.

### 5. Tools Module (`src/tools`)
The `tools` module contains individual editor tools for manipulating the scene.

- **`base_tool.py`**: The base class for all tools, defining common functionality.
- **`brush_tool.py`**: Implements the brush tool for placing tiles or entities.
- **`eraser_tool.py`**: Implements the eraser tool for removing tiles or entities.
- **`select_tool.py`**: Implements the selection tool for selecting elements.
- **`move_tool.py`**: Implements the move tool for repositioning elements.
- **`fill_tool.py`**: Implements the fill tool for filling areas with tiles.
- **`entity_placer.py`**: Implements the entity placer tool for adding entities to the scene.

### 6. Assets Module (`src/assets`)
The `assets` module manages asset loading, previewing, and caching.

- **`asset_manager.py`**: The main class for managing assets, including loading and unloading.
- **`sprite_loader.py`**: Handles the loading of sprite assets.
- **`thumbnail_cache.py`**: Manages thumbnails for assets to improve performance.

### 7. UI Module (`src/ui`)
The `ui` module contains reusable UI components and utilities.

- **`widgets.py`**: Custom buttons, dropdowns, and other UI elements.
- **`imgui_utils.py`**: Helpers for ImGui-style UI, including styles and layouts.
- **`theme.py`**: Manages the editor's theme, including colors and styles.

### 8. Utils Module (`src/utils`)
The `utils` module provides general-purpose helpers and utilities.

- **`math.py`**: Mathematical utilities for the editor.
- **`file_dialog.py`**: Handles file dialogs for opening and saving files.
- **`color.py`**: Utilities for color manipulation.
- **`rect.py`**: Utilities for rectangle operations.
- **`logging.py`**: Logging utilities for debugging and monitoring.

## Data Flow

1. **Initialization**:
   - The `app.py` initializes the editor, loading configurations and setting up the main window.
   - The `asset_manager.py` loads necessary assets, such as icons and fonts.

2. **User Interaction**:
   - The `tool_manager.py` processes user input and delegates actions to the appropriate tool.
   - Tools modify the scene data, which is managed by the `scene.py` module.

3. **Rendering**:
   - The `renderer.py` draws the scene, including layers, entities, and tilemaps.
   - The `camera.py` manages the view, ensuring the user can navigate the scene.

4. **Saving and Loading**:
   - The `scene_serializer.py` handles saving and loading scenes, ensuring data persistence.

## Extensibility

The architecture is designed to be modular, allowing for easy extension and customization. New tools, panels, and features can be added by following the existing patterns and interfaces.

## Conclusion

This architecture provides a solid foundation for a 2D game editor, with clear separation of concerns and modular design. Each component is responsible for a specific aspect of the editor, making it easier to maintain and extend.