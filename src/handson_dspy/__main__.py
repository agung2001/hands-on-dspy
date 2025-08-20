"""Main entry point for the DSPy module.

This file allows the module to be run as a script using 'python -m dspy'.
"""

import argparse
import sys

from . import __version__
from .module import example_summarization

def main():
    """Main entry point for the DSPy module."""
    parser = argparse.ArgumentParser(
        description="DSPy - A framework for programming with foundation models"
    )
    
    parser.add_argument("--version", action="version", version=f"DSPy {__version__}", help="Show the version and exit")
    parser.add_argument("--example",action="store_true",help="Run an example summarization task")
    
    args = parser.parse_args()
    
    if args.example:
        example_summarization()
    else:
        # If no arguments are provided, show help and run the example
        parser.print_help()
        print("\nRunning example summarization task...\n")
        example_summarization()

if __name__ == "__main__":
    sys.exit(main())