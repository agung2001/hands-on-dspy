"""Main entry point for the DSPy module.

This file allows the module to be run as a script using 'python -m dspy'.
"""

import argparse
import sys
import handson_dspy.example as example
from . import __version__

def main():
    """Main entry point for the DSPy module."""
    parser = argparse.ArgumentParser(
        description="DSPy - A framework for programming with foundation models"
    )
    
    # Argument bool
    parser.add_argument("--version", action="version", version=f"DSPy {__version__}", help="Show the version and exit")
    parser.add_argument("--example",action="store_true",help="Run an example task")

    # Argument string
    parser.add_argument("--question", type=str, default="What is the capital of Indonesia?", help="Question to be answered")
    
    args = parser.parse_args()
    
    # Modules
    example.main(args)

if __name__ == "__main__":
    sys.exit(main())