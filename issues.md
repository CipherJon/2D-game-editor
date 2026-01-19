# Issues

## Fixed Issues
- **Black Screen Issue**: The black screen issue has been resolved by integrating the `EditorWindow` class into the `App` class and ensuring that the panels are rendered properly.

## Current Issues
- **Tile Palette Panel**: The `TilePalettePanel` needs to be stylized and made functional.
- **Toolbar Panel**: The `ToolbarPanel` needs to be stylized and made functional.

## Current Issue: Black Screen on Launch

### Description
The project launches successfully, but only displays a black screen. No visible content or UI elements are rendered.

### Steps to Reproduce
1. Launch the application.
2. Observe that the window opens but remains entirely black.

### Expected Behavior
The application should display the expected UI, game editor, or other visual elements.

### Possible Causes
- Rendering pipeline issue.
- Missing or incorrect initialization of the graphics context.
- Shader compilation or linking errors.
- Missing assets or resources.
- Incorrect camera or viewport setup.

### Debugging Steps
1. Check the rendering logs for errors or warnings.
2. Verify that all required assets and shaders are loaded correctly.
3. Ensure the graphics context is properly initialized.
4. Test with minimal rendering to isolate the issue.

### Additional Notes
- This issue may require further investigation into the rendering system and initialization process.