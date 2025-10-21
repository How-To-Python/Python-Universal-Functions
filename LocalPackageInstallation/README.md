# ✨ LOCAL PACKAGE INSTALLATION (RECOMMENDED)

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
- The `__init__.py` file marks a folder as a package
- Without `__init__.py`, `example_custom_lib` is just a folder not a package
- It's the "front door" to your package that controls what happens when someone imports it.
- Namespace Control: `__init__.py` lets you organize internal structure while presenting clean external interface
    - Internal structure
    ```
        example_custom_lib/
        ├── __init__.py
        ├── filename.py
        ├── utilities.py
        └── helpers.py
    ```
    - External interface (what users see): `from example_custom_lib import function_1, function_2, utils_function, helper_function`
- The `__init__.py` file transforms a collection of Python files into a professional, user-friendly package that's easy to import and use
- see `example__init__.py`

###### Key Benefits of `__init__.py`:
1. Professional Package Structure: Standard Python packaging
2. Clean User Experience: Simple imports for users
3. Flexible Organization: Change internal structure without breaking user code
4. Documentation: Self-documenting package interface
5. Tool Integration: Better IDE support and package management
6. Future-Proof: Easy to add new modules without changing user code

### 2️⃣ Create setup.py file
- `setup.py` is the build script for Python packages
- tells Python how to install your package, what it contains, and its metadata
- This **`setup.py`** transforms your simple Python files into a professional, installable package that can be used across all your projects
- see `example_setup.py`

### 🗝️ Key Benefits of `setup.py`:
1. Professional Structure: Standard Python packaging
2. Easy Distribution: Can upload to PyPI later
3. Dependency Management: Handles required packages
4. Version Control: Tracks package versions
5. Cross-Platform: Works on Windows, macOS, Linux
6. IDE Integration: Better autocomplete and error checking

### 3️⃣ Install in development mode
- Development Installation: `pip install -e .`
- **`-e`:** "Editable" mode, so changes to your code are immediately available
- Links to your source directory instead of copying files, perfect for development
- **During Installation:**
    **1. Package Registration:** Python knows about `my-package-name`(this is the name you gave in the `setup()` function in the `setup.py` file)
    **2. Import Path:** example_custom_lib becomes importable everywhere
    **3. Dependency Resolution:** Installs any required packages
    **4. Console Scripts:** Creates any command-line tools
- **Usage After Installation:** `from example_custom_lib import function_1, function2 etc....`
