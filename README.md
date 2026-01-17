# 2D Game Editor

A lightweight and extensible 2D game editor for creating and managing game scenes, tilemaps, and entities.

## Features

- **Scene Management**: Create, edit, and organize game scenes with layers.
- **Tilemap Editor**: Design levels using tilemaps with support for multiple tilesets.
- **Entity System**: Place and manage game entities with customizable properties.
- **Asset Management**: Import and organize sprites, textures, and other assets.
- **Undo/Redo Support**: Full history tracking for all editor actions.
- **Customizable Tools**: Brush, eraser, fill, and selection tools for level design.
- **Grid and Gizmos**: Visual aids for precise placement and alignment.

## Installation

### Prerequisites

- Python 3.8 or higher
- Pygame 2.0 or higher
- NumPy 1.20 or higher
- Pillow 8.0 or higher

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/2d-game-editor.git
   cd 2d-game-editor
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the editor:
   ```bash
   python -m src.main
   ```

## Project Structure

```
2D-game-editor/
├── src/
│   ├── core/               # Core application logic
│   ├── editor/             # Editor-specific functionality
│   ├── rendering/          # Rendering and visualization
│   ├── scene/              # Scene and layer management
│   ├── tools/              # Editor tools (brush, eraser, etc.)
│   ├── assets/             # Asset management
│   ├── ui/                # User interface components
│   └── utils/              # Utility functions and helpers
├── resources/             # Game assets and resources
├── projects/              # Example projects
├── tests/                 # Unit tests
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── pyproject.toml         # Build configuration
```

## Usage

1. **Create a New Scene**: Start by creating a new scene and setting its dimensions.
2. **Add Layers**: Organize your scene using layers for better management.
3. **Place Tiles**: Use the tilemap editor to design your levels.
4. **Add Entities**: Place game entities and customize their properties.
5. **Save Your Work**: Save your scene to a file for later editing.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Now, let's update the `requirements.txt` file to ensure all dependencies are listed correctly.

<file_path>
2D-game-editor/requirements.txt
</file_path>

<edit_description>
Update requirements.txt with all dependencies
</edit_description>
```

pygame>=2.0
pygame_gui>=0.6
numpy>=1.20
Pillow>=8.0
toml>=0.10