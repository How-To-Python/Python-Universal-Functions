from setuptools import setup, find_packages
'''
setuptools: Modern Python packaging library (better than older distutils)
setup: Main function that defines the package
find_packages(): Automatically finds all Python packages in your directory
'''


'''
Package Metadata
    - name: Package name (what you'll pip install)
    - version: Semantic versioning (major.minor.patch)
    - description: Short description shown in package lists
    - author & author_email: Package creator info
    - packages: Use find_packages() to include all packages
        - find_packages(): Automatically scans directory for __init__.py files to identify packages
                    ├── setup.py
                    ├── README.md
                    ├── example_custom_lib/
                    │   ├── __init__.py
                    │   ├── filename.py
                    │   ├── utilities.py
                    │   └── helpers.py
                    └── tests/
                        └── test_functions.py
        - this will find example_custom_lib as a package
        - Alternative: packages=['example_custom_lib'] (manual specification), but find_packages() is more flexible because it auto-detects packages and sub-packages
    - python_requires: Minimum Python version required
        - Prevents installation on incompatible Python versions
        - This package works on Python 3.6 and newer
    - install_requires: List of dependencies to install with your package
        - Example: install_requires=['requests', 'numpy>=1.20.0', 'pandas' etc...]
        - leave empty if your functions don't need external libraries
    - entry_points: Define command-line scripts if needed
        - Example: 'command-name=example_custom_lib.filename:function_name'
            - creates a terminal command 'command-name' that runs function_name() from filename.py
    - classifiers: Metadata for package indexing (e.g., PyPI)
    - long_description: Detailed description of your package (supports Markdown)
    - long_description_content_type: Format of the long description (e.g., text/markdown)
'''
setup(
    name="my-package-name",
    version="0.1.0",
    description="My custom Python utility library",
    author="Bilbo Baggins",
    author_email="bilbo.baggins@example.com",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        # Add any dependencies here if needed
    ],
    entry_points={
        'console_scripts': [
            # Add command-line scripts here if needed
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",# Alpha (early development), Beta (testing), or Production
        "Intended Audience :: Developers",# Who should use this package
        "License :: OSI Approved :: MIT License",# Legal terms (MIT is permissive)
        "Programming Language :: Python :: 3",# Version classifiers Indicates Python 3 support
        "Programming Language :: Python :: 3.6",# Version classifiers Indicates Python 3.6 support
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)