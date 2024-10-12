# Rich Menu Command Line Tool

## Introduction
This project is a command line tool that allows users to navigate through a menu of commands and execute them.

## Description
The Rich Menu Command Line Tool leverages Python's standard libraries to create an interactive user experience. Users can navigate a grid of commands using their keyboard.

### JSON Structure
The structure of the menu items is represented as a JSON object:
```
data: value
```
Where `data` represents the menu items and `value` represents the CLI command. Pressing enter will execute the corresponding command.

Additionally, columns in the menu are divided based on the emoticon at the start of the data items.

## Installation Guide
To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage Guide
1. **Clone the repository:**
   
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the project directory:**
   
   ```bash
   cd <project-directory>
   ```

3. **Run the script:**
   
   ```bash
   python rich-menu-col.py
   ```

4. **Navigation:**
   - Use the **arrow keys** to navigate through the commands.
   - Press **Enter** to select a command.
   - To exit, press **Ctrl+C** at any time.

5. **Default Command:**
   - The initial command selected by default is the **shell command**.

## Functionality Overview
- **get_input()**: Captures user keyboard input for menu navigation, supporting arrow keys and enter key for selection.
- **execute_command(command_value)**: Executes the command associated with the selected menu item using the `subprocess` module.
- **exit_application()**: Gracefully exits the application.
- **main()**: Coordinates the application's flow, handling input and rendering the menu.
- **load_commands()**: (Assumed) Loads command data for the menu.
- **group_commands(commands)**: (Assumed) Groups commands into columns based on some criteria.
- **render_menu(columns, selected_row, selected_col)**: Displays the command menu in a structured format, highlighting the selected item.

## Release Notes
### Version 1.0.0
- Initial release of the Rich Menu Command Line Tool.
