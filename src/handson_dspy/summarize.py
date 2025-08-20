"""Basic DSPy module with example functionality.

This module demonstrates core DSPy features including:
- Creating language model modules
- Defining signatures for tasks
- Building simple pipelines
"""

import os
import dspy
from .provider import LLMProvider

# Define a signature for a simple task
class Summarize(dspy.Signature):
    """Signature for text summarization task."""
    text = dspy.InputField()
    summary = dspy.OutputField()

# Create a module that implements the signature
class TextSummarizer(dspy.Module):
    """A simple DSPy module for text summarization."""
    
    def __init__(self):
        super().__init__()
        self.summarize = dspy.Predict(Summarize)
    
    def forward(self, text):
        """Generate a summary for the given text."""
        result = self.summarize(text=text)
        return result.summary

def summarize_text(args):
    """Run text summarization task."""
    # Configure the language model
    provider = LLMProvider()
    provider.configure_provider()
    
    # Create the summarizer
    summarizer = TextSummarizer()

    # Read text from file
    with open(args.path_file, 'r') as file:
        text = file.read()
    
    # Generate and print the summary
    print("📄 Original Text:")
    print(text)
    print()

    print("📝 Generated Summary:")
    summary = summarizer(text)
    print(summary)
    
    return summary

def main(args):
    """Run summarization task."""
    if args.summarize and args.path_file:
        summarize_text(args)
    