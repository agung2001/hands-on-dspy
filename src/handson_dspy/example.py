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
def example_qna(args):
    """Run an example question answering task."""
    # Configure the language model
    provider = LLMProvider()
    lm = provider.configure()

    # Set default question
    if not args.question:
        question = "What is the capital of Indonesia?"
    else:
        question = args.question

    # Create QnA task
    qna = dspy.Predict('question -> answer')
    response = qna(question=question)

    print('❓Question:', question)
    print('✅ Answer:')
    print(response.answer)
    print()

    # Print history
    lm.inspect_history()

    return response

def main(args):
    """Main function"""
    if args.example:
        example_qna(args)
