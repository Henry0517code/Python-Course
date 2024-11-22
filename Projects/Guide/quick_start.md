# How to Setup Python Path and Run a Python Project

## 1. Setup Python Path in PowerShell

### Change Environment Variable (Windows)
Environment variables help your system locate Python when you type `python` in the terminal.

#### Steps:
1. Open PowerShell and check if Python is installed by typing:
   ```bash
   python --version
   ```
   If not recognized, you'll need to add Python to your system's environment path.
2. Search for "Environment Variables" in Windows and click **Edit the system environment variables**.
3. Click **Environment Variables** in the dialog box.
4. Under **System Variables**, find `Path` and click **Edit**.
5. Click **New** and add the path to your Python installation (usually something like `C:\PythonXX` or `C:\Users\<YourName>\AppData\Local\Programs\Python\PythonXX`).
6. Click **OK** to save everything.

For more detailed help, follow a tutorial like [this video](https://www.youtube.com/watch?v=9QrDn_hRSGs).

### Re-download Python (if needed)
If Python isn’t installed, visit [python.org](https://www.python.org) and download the latest version for your OS. During installation, ensure you **check the box** that says "Add Python to PATH."

You can follow a guide like this [video tutorial](https://www.youtube.com/watch?v=_ErLKQ-tJQ8).

---

## 2. A Brief Introduction to the Terminal

### Terminal in VSCode
1.	Click on the View menu at the top of the screen.
2.	Select Terminal from the dropdown, or use the shortcut:

- Ctrl + ` on Windows and Linux.
- Cmd + ` on macOS.


### Folder Hierarchy and Navigation
The terminal allows you to interact with your computer’s file system via text commands.

Here’s the updated version with Windows Command Prompt commands:

---

#### Key Commands (Windows Command Prompt):
- **cd**: Displays the current folder you’re in (Change Directory). It also changes the directory (folder) you're in.

  To display current directory:
  ```cmd
  cd
  ```

  To change to a specific directory:
  ```cmd
  cd <folder-name>
  ```

  Example:
  ```cmd
  cd Documents\Projects
  ```

- **dir**: Lists all files and folders in your current directory.
  ```cmd
  dir
  ```

*Tip*: To move to a parent folder, use:
```cmd
cd ..
```

--- 

## 3. What’s `pip`?

`pip` is a package manager for Python. It allows you to install and manage third-party libraries.

#### Common `pip` Commands:
- To install a package:
  ```bash
  pip install <package-name>
  ```

  Example:
  ```bash
  pip install numpy
  ```

- To check if `pip` is installed:
  ```bash
  pip --version
  ```

If `pip` isn’t installed, follow [this guide](https://pip.pypa.io/en/stable/installation/) to set it up.

---

## 4. General Steps to Run a Python Project

### Step 1: Download or Clone the Project
- If the project is hosted on GitHub, copy the repository URL and use:
  ```bash
  git clone <repository-url>
  ```
  Alternatively, download the project as a `.zip` file and extract it.

### Step 2: Install Python
- Make sure Python is installed. You can check by typing:
  ```bash
  python --version
  ```

- If Python is not installed, download and install it from [python.org](https://www.python.org).

### Step 3: Open a Terminal
- On **Windows**: Open **PowerShell**.
- On **macOS/Linux**: Open the **Terminal** application.

### Step 4: Navigate to the Project Folder
Use the `cd` command to change into the directory where the project files are stored.

Example:
```bash
cd Downloads/YourProjectFolder
```

### Step 5: Install Required Libraries
Most Python projects come with a `requirements.txt` file listing all the needed libraries. To install them, type:
```bash
pip install -r requirements.txt
```

### Step 6: Run the Program
Typically, the main Python file is called something like `main.py` or `app.py`. To run it, type:
```bash
python main.py
```

*Note*: If the project has additional instructions, they will usually be in a `README.md` file. Be sure to read it for any specific steps.