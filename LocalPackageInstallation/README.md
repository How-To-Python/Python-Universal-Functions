# ✨ LOCAL PACKAGE INSTALLATION (RECOMMENDED)
**Install your package in "editable" mode using `pip install -e .` It will create a .egg-link file in site-packages that points to your development directory. The package will appear in pip list as if normally installed and changes to your code are immediately available without reinstalling. Best for active development, testing, and professional projects.**

#### Advantages
✅ **Development-friendly:** Edit code and see changes immediately

✅ **Professional:** Uses standard Python packaging tools

✅ **Reversible:** Easy to uninstall with pip uninstall

✅ **Version control:** Tracks installation in requirements.txt

✅ **Cross-platform:** Works on Windows, Mac, Linux


#### Disadvantages
❌ Requires proper package structure (setup.py, init.py)

❌ Per-environment installation needed

-------
## How To Create a Local Package Insatllation


### 1️⃣ Create a proper package structure

```
YourCustomLibrary/
├── setup.py
├── README.md
├── example_custom_lib/
│   ├── __init__.py
│   ├── filename.py
│   ├── utilities.py
│   └── helpers.py
└── tests/
    └── test_functions.py
```
#### What is `__init__.py`?
- The `__init__.py` file transforms a collection of Python files into a professional, user-friendly package that's easy to import and use
- see example file [`example__init__.py`](./example_custom_lib/example__init__.py)
- Learn More About [`__init__.py`](./UnderstandingFilesandFolders/understanding__init__.py.md)
----------

### 2️⃣ Create setup.py file
- `setup.py` is the build script for Python packages
- tells Python how to install your package, what it contains, and its metadata
- This **`setup.py`** transforms your simple Python files into a professional, installable package that can be used across all your projects
- see example file [`example_setup.py`](./example-setup.py)

#### 🗝️ Key Benefits of `setup.py`:
1. Professional Structure: Standard Python packaging
2. Easy Distribution: Can upload to PyPI later
3. Dependency Management: Handles required packages
4. Version Control: Tracks package versions
5. Cross-Platform: Works on Windows, macOS, Linux
6. IDE Integration: Better autocomplete and error checking
----------

### 3️⃣ Install in development mode
- Development Installation: navigate to package directory(YourCustomLibrary) and run `pip install -e .`
- Check installation status: `pip show example_custom_lib`
- **`-e`:** "Editable/Development" mode, so changes to your code are immediately available
- Links to your source directory instead of copying files, perfect for development
- **During Installation:**

    **1. Package Registration:** Python knows about `my-package-name`(this is the name you gave in the `setup()` function in the `setup.py` file)

    **2. Import Path:** example_custom_lib becomes importable everywhere

    **3. Dependency Resolution:** Installs any required packages

    **4. Console Scripts:** Creates any command-line tools
- **Usage After Installation:** `from example_custom_lib import function_1, function2 etc....`
----------

##### 📁 `.egg-info` folder

###### ❓ What is the `.egg-info` folder?
**The `.egg-info` folder is is metadata storage created by Python's packaging tools. Python's way of saying `This package is officially installed and ready to use` It's the bridge between your source code and Python's import system.**

###### 💭 Where Does The `.egg-info` Folder Come From?
- automatically created by Python's packaging system when you run `pip install -e .`
**Learn More About [`__init__.py`](./UnderstandingFilesandFolders/understanding__init__.py.md)**
----------
##### 📁 `__pycache__` Folder

###### ⁉️ What is `__pycache__`?
**The `__pycache__` folder is Python's `compiled bytecode cache` that stores pre-compiled versions of your Python files for faster execution.**

###### 💭 Where Does The `__pycache__` Folder Come From?
**`__pycache__` is automatically created by Python when you:**
- Import a module for the first time
- Run a Python script that imports other modules
- Execute any Python code that loads `.py` files
**Learn More About [`__pycache__.py`](./UnderstandingFilesandFolders/understanding__pycache__folder.md)**










