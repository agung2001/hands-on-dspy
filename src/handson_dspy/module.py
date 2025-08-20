"""Basic DSPy module with example functionality.

This module demonstrates core DSPy features including:
- Creating language model modules
- Defining signatures for tasks
- Building simple pipelines
"""

import os
import dspy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Configure a language model
def configure_llm():
    """Configure and return a language model for use with DSPy."""
    # This is a simple configuration using OpenAI
    # In a real application, you would use your API key
    # and potentially other configuration options
    try:
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        llm = dspy.OpenAI(model="gpt-3.5-turbo", api_key=api_key)
        dspy.settings.configure(lm=llm)
        return llm
    except Exception as e:
        print(f"Error configuring language model: {e}")
        print("Using a local mock LM for demonstration purposes.")
        # Fallback to a mock LM for demonstration
        return dspy.MockLM()

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

# Example function to demonstrate usage
def example_summarization():
    """Run an example summarization task."""
    # Configure the language model
    configure_llm()
    
    # Create the summarizer
    summarizer = TextSummarizer()
    
    # Example text to summarize
    text = """
    DSPy is a framework for algorithmically optimizing LM prompts and weights 
    to solve knowledge-intensive tasks. It provides a unified interface for 
    programming with foundation models, fine-tuning smaller models, and 
    optimizing prompts and pipelines. DSPy introduces a new paradigm for 
    programming with language models, focusing on declarative signatures, 
    composable modules, and optimizable programs.
    """
    
    # Generate and print the summary
    print("\nOriginal Text:")
    print(text)
    print("\nGenerated Summary:")
    summary = summarizer(text)
    print(summary)
    
    return summary