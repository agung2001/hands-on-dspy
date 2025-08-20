"""Main entry point for the DSPy module.

This file allows the module to be run as a script using 'python -m dspy'.
"""

import argparse
import sys
import handson_dspy.example as example
import handson_dspy.qna as qna
import handson_dspy.summarize as summarize
# import handson_dspy.translate as translate

from . import __version__

def main():
    """Main entry point for the DSPy module."""
    parser = argparse.ArgumentParser(
        description="DSPy - A framework for programming with foundation models"
    )
    
    # Argument bool
    parser.add_argument("--version", action="version", version=f"DSPy {__version__}", help="Show the version and exit")
    parser.add_argument("--example",action="store_true",help="Run an example task")
    parser.add_argument("--summarize",action="store_true",help="Run summarization task")

    # Argument string
    parser.add_argument("--context", type=str, default="", help="Context for the task")
    parser.add_argument("--path-file", type=str, default="samples/dspy.md", help="Path to the file to be summarized")
    parser.add_argument("--question", type=str, default="", help="Question to be answered")
    
    # Parse args
    args = parser.parse_args()
    
    # Modules
    example.main(args)
    qna.main(args)
    summarize.main(args)

if __name__ == "__main__":
    sys.exit(main())