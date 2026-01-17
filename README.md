# 2D Game Editor

A modular and extensible 2D game editor built with Python and Pygame.

## Features

- **Modular Architecture**: The editor is divided into several key components, each responsible for a specific aspect of the editor's functionality.
- **Scene Management**: Create, edit, and manage game scenes with layers, entities, and tilemaps.
- **Asset Management**: Load, manage, and preview assets such as sprites, textures, and other resources.
- **Tool System**: Use a variety of tools for manipulating the scene, including brush, eraser, select, move, fill, and entity placer tools.
- **Rendering**: High-level rendering helpers for drawing scenes, layers, and other visual elements.
- **Undo/Redo System**: Full support for undoing and redoing actions.
- **Customizable UI**: Reusable UI components and widgets for the editor.

## Installation

### Prerequisites

- Python 3.8 or higher
- Pygame
- Pillow (for image processing)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/2D-game-editor.git
   cd 2D-game-editor
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the editor:
   ```bash
   python -m src.main
   ```

## Usage

### Basic Usage

1. **Create a New Scene**:
   - Click on the "File" menu and select "New Scene".
   - Enter a name for the scene and click "OK".

2. **Add Layers**:
   - Click on the "Layer" menu and select "Add Layer".
   - Enter a name for the layer and click "OK".

3. **Add Entities**:
   - Select the "Entity Placer" tool from the toolbar.
   - Click on the scene to place an entity.

4. **Save the Scene**:
   - Click on the "File" menu and select "Save Scene".
   - Enter a name for the scene file and click "Save".

### Advanced Usage

1. **Customize the UI**:
   - Modify the `theme.py` file to change the editor's color scheme and styles.
   - Add custom widgets to the `widgets.py` file.

2. **Add New Tools**:
   - Create a new tool class that inherits from `BaseTool`.
   - Implement the required methods (`on_activate`, `on_deactivate`, `handle_event`, `update`, `draw`).
   - Register the tool with the `ToolManager`.

3. **Extend the Scene System**:
   - Add new entity types by creating classes that inherit from `Entity`.
   - Add new layer types by creating classes that inherit from `Layer`.

## Architecture

The editor is divided into several key components:

- **Core Module**: Contains the fundamental systems and base classes that form the backbone of the editor.
- **Editor Module**: Contains the logic and UI components for the editor itself.
- **Scene Module**: Manages the data and serialization of game scenes.
- **Rendering Module**: Handles all drawing and camera-related functionality.
- **Tools Module**: Contains individual editor tools for manipulating the scene.
- **Assets Module**: Manages asset loading, previewing, and caching.
- **UI Module**: Contains reusable UI components and utilities.
- **Utils Module**: Provides general-purpose helpers and utilities.

For more details, see the [Architecture Documentation](docs/architecture.md).

## Testing

To run the tests, use the following command:

```bash
python -m pytest tests/
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Roadmap

- **Short-term Goals**:
  - Improve error handling and logging.
  - Add more comprehensive tests.
  - Enhance the UI with more customizable widgets.

- **Long-term Goals**:
  - Add support for animations and particle effects.
  - Implement a plugin system for extending the editor.
  - Add support for exporting scenes to popular game engines.

## Contact

For questions or feedback, please contact the project maintainer at [your.email@example.com](mailto:your.email@example.com).
