"""Basic DSPy module with example functionality.

This module demonstrates core DSPy features including:
- Creating language model modules
- Defining signatures for tasks
- Building simple pipelines
- Question answering task
"""

import os
import dspy
from .provider import LLMProvider

# Example function to demonstrate usage
def example_qna(question):
    """Run an example question answering task."""
    # Configure the language model
    provider = LLMProvider()
    lm = provider.configure_provider()

    # Create QnA task
    qna = dspy.Predict('question -> answer')
    response = qna(question=question)

    print('Question:', question)
    print('Answer:', response.answer)

    # Print history
    # lm.inspect_history()

    return response

def main(args):
    """Main function"""
    if args.example or args.question:
        example_qna(args.question)
