"""Basic DSPy module with example functionality.

This module demonstrates core DSPy features including:
- Creating language model modules
- Defining signatures for tasks
- Building simple pipelines
"""

import os
import sys
import dspy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
ollama_api_base = os.getenv("OLLAMA_API_BASE")

class LLMProvider:
    """A class to configure and provide language model instances for DSPy."""
    
    def __init__(self, provider_type="ollama"):
        """Initialize the LLM provider.
        
        Args:
            provider_type (str): Type of LLM provider ('openai' or 'ollama')
        """
        self.provider_type = provider_type.lower()
        
    def configure_provider(self):
        """Configure and return a language model for use with DSPy."""
        try:
            if self.provider_type == "openai":
                if not openai_api_key:
                    raise ValueError("OPENAI_API_KEY not found in environment variables")
                llm = dspy.LM("gpt-3.5-turbo", api_key=openai_api_key)
            elif self.provider_type == "ollama":
                llm = dspy.LM("ollama_chat/gemma3:4b", api_base=ollama_api_base, api_key='')
            else:
                raise ValueError(f"Unsupported provider type: {self.provider_type}")
            
            dspy.configure(lm=llm)
            return llm
            
        except Exception as e:
            print(f"Error configuring language model: {e}")
            print("Using a local mock LM for demonstration purposes.")
            sys.exit(1)
