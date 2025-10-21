# LOCAL PACKAGE INSTALLATION (RECOMMENDED)


### Key Benefits of This Method:
1. Professional Structure: Standard Python packaging
2. Easy Distribution: Can upload to PyPI later
3. Dependency Management: Handles required packages
4. Version Control: Tracks package versions
5. Cross-Platform: Works on Windows, macOS, Linux
6. IDE Integration: Better autocomplete and error checking


### STEP 1: Create a proper package structure

```
YourCustomLibrary/
├── setup.py
├── README.md
├── your_custom_lib/
│   ├── __init__.py
│   ├── filename.py
│   ├── utilities.py
│   └── helpers.py
└── tests/
    └── test_functions.py
```

### STEP 2: Create setup.py file
- `setup.py` is the build script for Python packages
- tells Python how to install your package, what it contains, and its metadata
- see `example_setup.py`

### STEP 3: Install in development mode
- Development Installation: `pip install -e .`
- **`-e`:** "Editable" mode, so changes to your code are immediately available
- Links to your source directory instead of copying files, perfect for development
- **During Installation:**
    **1. Package Registration:** Python knows about `my-package-name`(this is the name you gave in the `setup()` function in the `setup.py` file)
    **2. Import Path:** your_custom_lib becomes importable everywhere
    **3. Dependency Resolution:** Installs any required packages
    **4. Console Scripts:** Creates any command-line tools
- **Usage After Installation:** `from your_custom_lib import function_1, function2 etc....`
- This **`setup.py`** transforms your simple Python files into a professional, installable package that can be used across all your projects