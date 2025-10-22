# 📁 `.egg-info` folder

### 🤨 What is the `.egg-info` folder?
**The `.egg-info` folder is essentially Python's way of saying `This package is officially installed and ready to use` It's the bridge between your source code and Python's import system.**

### 👀 Where Does The `.egg-info` Folder Come From?
- automatically created by Python's packaging system when you run
    - **`pip install -e .`** (Development installation)
    - **`pip install .`** (Regular installation)
    - **`python setup.py develop`** (Older method)
    - **`python setup.py install`** (Older method)
- `.egg-info` should be added to the `.gitignore` file
    ```
        *.egg-info/
        __pycache__/
    ```
- it is metadata storage created by Python's packaging tools (setuptools in the `setup.py` file) when you install a package
- contains information about your installed package
- `.egg-info` allows the package to work from anywhere on your system, all you have to do is import it
    - Without `.egg-info` the package will only work with manual path setup
        ```
            import sys
            sys.path.append(r'C:\path\to\your\directory')
            from example_custom_lib import function_1, function_2
        ```

        
### 🗃️ What's Inside `.egg-info`? 

    ```
    YourCustomLibrary/
        ├── setup.py
        ├── README.md
        ├── example_python_utils.egg-info/
            ├── dependency_links.txt
            ├── PKG-INFO
            ├── SOURCES.txt
            └── top_level.txt
        ├── example_custom_lib/
    ```
- **dependency_links.txt**
    - **Contains:** External dependency links (usually empty)
    - **Purpose:** Points to custom package repositories if needed
- **PKG-INFO**
    - **Contains:** All metadata from your setup.py
    - **Purpose:** Python's package management system reads this to know:
        - Package name, version, author
        - Python version requirements
        - License and classifiers
        - Dependencies (if any)
- **SOURCES.txt**
    - **Contains:** List of all files included in the package
    - **Purpose:**
        - Tracks what files belong to this package
        - Used for uninstalling (knows what to remove)
        - Used for building distributions
- **top_level.txt**
    - **Contains:** Top-level package names that can be imported
    - **Purpose:** Tells Python what you can import from this package
    **This is why `from example_custom_lib import function_1, function_2`works!**

### 🤷🏾‍♀️ Why Does Python Create `.egg-info`?

#### 📦 Package Management
- **`pip list`**: shows your package in installed packages
- **`pip show example_custom_lib`**: shows detailed info from PKG-INFO
- **`pip uninstall example_custom_lib`**: uses this info to remove files

#### 📩 Import System
- Python checks `top_level.txt` to know that `example_custom_lib` is available for import
- `from example_custom_lib import function_1, function_2` works because of `top_level.txt`

#### 🏗️Development Mode
- Since `pip install -e .`was used
    - **Editable installation:** Changes to your code are immediately available
    - **Links to source:** Points to your development directory
    - **No copying:** Doesn't copy files to site-packages



### Should You Keep `.egg-info`?
**✅ Keep it if:**
- You want the package to remain installed
- You're actively developing the package
- You want to use from example_custom_lib import ... anywhere
**🗑️ Remove it if:**
- You want to uninstall the package
- You're moving the directory
- You want to start fresh
- `pip uninstall example_custom_lib` removes the .egg-info directory and uninstalls the package

### 🔀 What If Changes Are Made To The Package?
- Reinstall after major changes
    - `pip uninstall example_custom_lib`
    - `pip install -e .`
