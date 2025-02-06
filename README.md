# Code Compiler Web App

This is a simple Flask-based web app that allows users to input and execute code in multiple programming languages (Python, C++, Java) directly from a browser.

## Features

- **Supports multiple languages**: Python, C++, Java.
- **Web interface**: A user-friendly interface where users can paste their code, select the language, and execute it.
- **Error handling**: The app captures runtime errors and displays them to the user.
- **Temporary file cleanup**: Automatically cleans up the temporary files after code execution.

## Technologies Used

- **Flask**: Web framework for creating the app.
- **Subprocess**: To execute code in different languages.
- **Python**: Backend logic and handling of code execution.

## Setup and Installation

### Prerequisites

Ensure you have the following installed on your local machine:

1. **Python** (for running Python code):
   - Install from [python.org](https://www.python.org/downloads/).
   - Add Python to your `PATH`.

2. **G++** (for compiling C++ code):
   - Install **G++** (the GNU C++ compiler) via [MinGW](https://sourceforge.net/projects/mingw-w64/) or package managers like `apt` (Linux) or `brew` (macOS).
   - Ensure that `g++` is added to your `PATH`.

3. **Java** (for compiling and running Java code):
   - Install **Java** Development Kit (JDK) from [Oracle JDK](https://www.oracle.com/java/technologies/javase-downloads.html) or [OpenJDK](https://adoptopenjdk.net/).
   - Ensure `javac` and `java` commands are accessible from the command line (`PATH`).

4. **pip** (Python package manager):
   - Ensure you have `pip` installed to manage Python dependencies.

### Clone the Repository

```bash
git clone https://github.com/yourusername/code-compiler-web-app.git
cd code-compiler-web-app
