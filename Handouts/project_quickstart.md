---
marp: true
theme: default
paginate: true
---

<!-- slide: title -->

# 🚀 Python Project Quick‑Start  
### From install to running code in minutes

---

## Why This Guide?

- Get a new Python project working **fast**  
- Same steps for **Windows / macOS / Linux**  
- Slides structured so you can present or follow along

---

## 1️⃣ Check Python

```bash
python --version
pip --version
```

- **✅ Output appears:** jump ahead  
- **❌ “command not found”:** install Python next

---

## 2️⃣ Install / Re‑install Python

1. Download from **python.org/downloads** (3.x 64‑bit).  
2. **Windows**: tick “Add Python to PATH”.  
3. **macOS**: use the official pkg or **brew install python**.  
4. **Linux**: `sudo apt install python3 python3-pip`.

> Re‑open terminal to reload PATH.

---

## 3️⃣ Add Python to PATH (Windows)

1. Search **“Environment Variables”** → *Edit the system…*  
2. System Variables → **Path** → *Edit*  
3. *New* → paste install folder, e.g.  
   `C:\Users\<YOU>\AppData\Local\Programs\Python\Python312\`  
4. *OK* × 3 → reopen PowerShell  
5. Verify: `python --version`

---

## 4️⃣ Open a Terminal

| Editor | Shortcut |
|--------|----------|
| VS Code | **Ctrl/⌘ + \`** |
| PyCharm | **Alt + F12** |

Or launch **PowerShell / cmd / Terminal.app** directly.

---

## 5️⃣ Navigate the Filesystem

```bash
cd project_folder      # go in
cd ..                  # up one
dir          # Windows list
ls -la       # macOS/Linux list
```

Tip: Drag‑drop a folder into terminal to auto‑paste its path.

---

## 6️⃣ `pip` Essentials

| Task                 | Command                       |
|----------------------|-------------------------------|
| Install a library    | `pip install numpy`           |
| Upgrade a library    | `pip install -U numpy`        |
| Show installed pkgs  | `pip list`                    |
| Upgrade pip itself   | `python -m pip install -U pip`|

---

## 7️⃣ (Recommended) Virtual Environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

The prompt shows **(.venv)**.  
Install packages **inside** the env for project isolation.

---

## 8️⃣ Get the Code

```bash
# GitHub – preferred
git clone https://github.com/user/repo.git
# or download ZIP & extract
```

Move into the folder:

```bash
cd repo
```

---

## 9️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

If you see *ERROR: wheel not found*, first run

```bash
python -m pip install -U pip setuptools wheel
```

---

## 🔟 Run the Program

Common entry points:

```bash
python main.py
python -m package_name
streamlit run app.py
```

Read **README.md** for project‑specific commands or env vars (e.g. `FLASK_APP=app.py`).

---

## 1️⃣1️⃣ Common Errors & Fixes

| Error | Likely Cause | Quick Fix |
|-------|--------------|-----------|
| `ModuleNotFoundError` | package not installed / wrong env | Activate venv & `pip install` |
| `PermissionError` | file in use / admin rights | Close app or run as admin |
| `SyntaxError: invalid syntax` | using Python 2 vs 3 | Run with `python3` |

---

## 1️⃣2️⃣ Next Steps & Resources

- **Python Docs:** docs.python.org  
- **pip User Guide:** pip.pypa.io  
- **VS Code Python Ext.:** aka.ms/python-vscode  
- **More CLI Help:** `python -h`, `pip -h`, `git help`

---

## 🎉 You’re Ready!

Run code, experiment, break things & fix them.  
**Happy Pythoning!**

---

