

# Package Documentation Docstring: Documents what your package does
    # Shows up in help(): When someone types help(example_custom_lib)
    # Professional appearance: Makes your package look polished
"""
Shannon's Python Utilities
==========================

A collection of useful utility functions for Python projects.

Available modules:
- filename: What this module does
- utilities: General utility functions
- helpers: Helper functions for common tasks
"""




'''
Import Statements: Import functions and classes from submodules
    - .filename: The dot means "from the current package"
    - Imports specific functions: Brings function_1 and function_2 into package namespace
    - Makes functions accessible: Users can import directly from package root
    - Without the import statements, you would have to verbosely do:
        from example_custom_lib.filename import function_1, function_2
    - With these imports, you can cleanly import the functions like this:
        from example_custom_lib import function_1, function_2
'''
from .filename import function_1, function_2
# Import other modules as you create them
# from .utilities import *
# from .helpers import *

# Package Metadata
# Accessible programmatically: print(example_custom_lib.__version__)
# Used by tools: IDEs, package managers, documentation generators
__version__ = "0.1.0"  # Package version (follows semantic versioning)
__author__ = "Bilbo Baggins"  # Author name


'''
Export Control: Defines what is accessible when using 'from package import *'
    - Controls from example_custom_lib import *: Only exports listed items
    - Lists public functions: Only function_1 and function_2 are exposed
    - Hides internal details: Other functions/classes remain private
    - Improves usability: Users see only intended API
    - Documentation: Shows what's intended to be public API
    - IDE support: Better autocomplete and suggestions
'''
# Make functions available at package level
__all__ = [
    "function_1",
    "function_2",
    # Add other function names here as you create them
]


# Advanced __init__.py Features not always needed but useful in some cases
'''
Initialization Code: Code that runs when the package is first imported
    - Executes on import: Runs when someone imports example_custom_lib
    - Setup tasks: Can initialize variables, check environment, etc.
    - Conditional imports: Can import modules based on conditions
    - Logging: Can log that the package was loaded
    - Note: Keep this minimal to avoid side effects on import
    - Example uses:
        - Print a message: print("Example Custom Lib loaded!")
        - Set up configuration: if os.environ.get('DEBUG'): ...
        - Import optional modules: try: from .advanced_module import ... except ImportError: ...
    - This code runs only once per session:
    - Avoid heavy computations: Keep it light to prevent slow imports
'''
# Example initialization code, not needed
# print("Shannon's utils loaded!")

# # Setup code
# import os
# if os.environ.get('DEBUG'):
#     print("Debug mode enabled")


'''
Conditional Imports: Import different modules based on environment or availability
    - Dynamic imports: Can import modules based on conditions
    - Optional features: Enable advanced features if dependencies are available
    - Graceful degradation: Fallback if advanced modules are missing
    
    - Useful for packages with optional dependencies
    - Keeps package flexible: Works in different environments
'''
# Import different modules based on environment or availability
# Example: Try to import advanced_colors module
# If available, add true_color_support to __all__
#######################################################################
# try:
#     from .advanced_colors import true_color_support
#     ADVANCED_COLORS = True
# except ImportError:
#     ADVANCED_COLORS = False
    
# if ADVANCED_COLORS:
#     __all__.append('true_color_support')
#######################################################################


'''
Lazy Loading: Delay importing submodules until they are accessed
    - Improves startup time: Reduces initial import time
    - Saves memory: Loads modules only when needed
    - Complex setup: Requires custom __getattr__ and __dir__ methods
    - Example use case: Large packages with many submodules
'''
# # Lazy load heavy modules only when needed
########################################################################
# def __getattr__(name):
#     """Lazy load heavy modules only when needed"""
#     if name == 'heavy_module':
#         from . import heavy_module
#         return heavy_module
#     raise AttributeError(f"module {__name__} has no attribute {name}")
##########################################################################