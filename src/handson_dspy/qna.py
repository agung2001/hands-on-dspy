"""Basic DSPy module with example functionality.

This module demonstrates core DSPy features including:
- Creating language model modules
- Defining signatures for tasks
- Building simple pipelines
"""

import os
import dspy
from .provider import LLMProvider

class QnASignature(dspy.Signature):
    """Signature for question answering task."""
    context = dspy.InputField(desc="Reference text containing the answer")
    question = dspy.InputField(desc="Question to be answered")
    answer = dspy.OutputField(desc="Answer to the question based on the context")

class QnA(dspy.Module):
    """Question answering module using DSPy."""
    
    def __init__(self, provider=None):
        super().__init__()
        self.qa = dspy.ChainOfThought(QnASignature)
        if provider:
            dspy.settings.configure(lm=provider)
    
    def forward(self, context, question):
        """
        Answer a question based on the provided context.
        
        Args:
            context (str): Reference text containing information
            question (str): Question to be answered
            
        Returns:
            str: Answer to the question
        """
        prediction = self.qa(context=context, question=question)
        return prediction.answer
