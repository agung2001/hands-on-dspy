"""Basic DSPy module with example functionality.

This module demonstrates core DSPy features including:
- Creating language model modules
- Defining signatures for tasks
- Building simple pipelines
"""

import os
import dspy
from typing import Literal

# Define a signature for a simple task
class Summarize(dspy.Signature):
    """Signature for text summarization task."""
    # NOTE: you can also define without typing such as text = dspy.InputField()
    text: str = dspy.InputField(desc="Text to be summarized") 
    summary: str = dspy.OutputField(desc="Summary of the text")
    writing_style: Literal["academic", "casual", "business", "poetic"] = dspy.OutputField(desc="Writing style of the summary")

# Create a module that implements the signature
class TextSummarizer(dspy.Module):
    """A simple DSPy module for text summarization."""
    
    def __init__(self):
        super().__init__()
        self.summarize = dspy.Predict(Summarize)
    
    def forward(self, text):
        """Generate a summary for the given text."""
        result = self.summarize(text=text)
        return result

def summarize_text(args):
    """Run text summarization task."""    
    # Create the summarizer
    summarizer = TextSummarizer()

    # Read text from file
    with open(args.path_file, 'r') as file:
        text = file.read()
    
    summary = summarizer(text)

    # Generate and print the summary
    print("📄 Original Text:")
    print(text)
    print()

    print("📝 Generated Summary:")
    print(summary.summary)
    print()
    
    print("✍️ Writing Style:", summary.writing_style)
    
    return summary

def main(args):
    """Run summarization task."""
    if args.summarize and args.path_file:
        summarize_text(args)
    