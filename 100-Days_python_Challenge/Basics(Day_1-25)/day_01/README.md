# Getting Started with Python, Jupyter Notebook, and VSCode

Welcome!This guide will help you install Python, Jupyter Notebook, and Visual Studio Code (VSCode), and teach you how to create and run your first Python script and Jupyter notebook. Whether you are a beginner or just setting up your environment, this step-by-step tutorial will get you started smoothly.

---

## Table of Contents

- [1. Installing Python](#1-installing-python)
- [2. Installing Jupyter Notebook](#2-installing-jupyter-notebook)
- [3. Installing Visual Studio Code (VSCode)](#3-installing-visual-studio-code-vscode)
- [4. Creating and Running Your First Python Script](#4-creating-and-running-your-first-python-script)
- [5. Creating and Running Your First Jupyter Notebook](#5-creating-and-running-your-first-jupyter-notebook)
- [6. Additional Tips](#6-additional-tips)

---

## 1. Installing Python

Python is a popular, easy-to-learn programming language widely used for web development, data science, automation, and more.

### Step-by-step installation:

1. **Download Python:**

   - Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Download the latest stable version for your operating system (Windows, macOS, Linux).

2. **Run the Installer:**

   - **Windows:**  
     - Run the downloaded `.exe` file.  
     - **Important:** Check the box **Add Python to PATH** before clicking "Install Now".  
     - Follow the prompts to complete installation.

   - **macOS:**  
     - Open the downloaded `.pkg` file and follow the instructions.  
     - Alternatively, use Homebrew:  
       ```bash
       brew install python
       ```

   - **Linux:**  
     - Use your package manager, e.g., for Ubuntu/Debian:  
       ```bash
       sudo apt update
       sudo apt install python3 python3-pip
       ```

3. **Verify Installation:**

   Open a terminal or command prompt and type:

   ```bash
   python --version
   ```

   or

   ```bash
   python3 --version
   ```

   You should see the installed Python version.

---

## 2. Installing Jupyter Notebook

Jupyter Notebook is an interactive web application that allows you to create and share documents containing live code, equations, visualizations, and narrative text.

### Installation steps:

1. **Install via pip (Python package manager):**

   Open your terminal or command prompt and run:

   ```bash
   pip install notebook
   ```

2. **Verify Installation:**

   Run:

   ```bash
   jupyter notebook
   ```

   This command will start the Jupyter Notebook server and open the interface in your default web browser.

---

## 3. Installing Visual Studio Code (VSCode)

VSCode is a free, powerful, and lightweight code editor with great support for Python development.

### Installation steps:

1. **Download VSCode:**

   - Visit [https://code.visualstudio.com/](https://code.visualstudio.com/)
   - Download the installer for your operating system.

2. **Install VSCode:**

   - Run the installer and follow the setup instructions.

3. **Install Python Extension:**

   - Open VSCode.
   - Go to the Extensions view by clicking the square icon on the sidebar or pressing `Ctrl+Shift+X` (`Cmd+Shift+X` on macOS).
   - Search for **Python** by Microsoft.
   - Click **Install**.

4. **Configure Python Interpreter:**

   - Press `Ctrl+Shift+P` (`Cmd+Shift+P` on macOS) to open the Command Palette.
   - Type `Python: Select Interpreter` and select the Python version you installed.

---

## 4. Creating and Running Your First Python Script

### Steps:

1. **Create a Python file:**

   - Open VSCode.
   - Click **File > New File**.
   - Save the file as `hello.py`.

2. **Write your first Python code:**

   ```python
   print("Hello, world!")
   ```

3. **Run the script:**

   - Open the integrated terminal in VSCode (`Ctrl+`` or `View > Terminal`).
   - Run the script by typing:

     ```bash
     python hello.py
     ```

   - You should see the output:

     ```
     Hello, world!
     ```

---

## 5. Creating and Running Your First Jupyter Notebook

### Steps:

1. **Launch Jupyter Notebook:**

   - Open your terminal or command prompt.
   - Run:

     ```bash
     jupyter notebook
     ```

   - Your default browser will open the Jupyter interface.

2. **Create a new notebook:**

   - Click **New > Python 3** (or your installed Python version).

3. **Write your first notebook cell:**

   ```python
   print("Hello, Jupyter!")
   ```

4. **Run the cell:**

   - Press `Shift + Enter` or click the **Run** button.
   - The output will appear below the cell:

     ```
     Hello, Jupyter!
     ```

---

## 6. Additional Tips

- **Using VSCode with Jupyter Notebooks:**

  VSCode supports Jupyter notebooks natively. You can open `.ipynb` files directly in VSCode and run cells interactively.

- **Managing Python packages:**

  Use `pip` to install additional packages:

  ```bash
  pip install package_name
  ```

- **Virtual Environments:**

  To avoid package conflicts, consider using virtual environments:

  ```bash
  python -m venv myenv
  source myenv/bin/activate  # macOS/Linux
  myenv\Scripts\activate     # Windows
  ```

---

## Summary

You have now:

- Installed Python, Jupyter Notebook, and VSCode.
- Created and run your first Python script.
- Created and run your first Jupyter notebook.

You are ready to explore Python programming and data science with powerful tools!

---

## References

- [Python Official Website](https://www.python.org/)
- [Jupyter Project](https://jupyter.org/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Python Extension for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

---

*Happy coding!* 
