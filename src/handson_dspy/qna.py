"""Basic DSPy module with example functionality.

This module demonstrates core DSPy features including:
- Creating language model modules
- Defining signatures for tasks
- Building simple pipelines
"""

import os
import dspy

class QnASignature(dspy.Signature):
    """Signature for question answering task."""
    question = dspy.InputField(desc="Question to be answered")
    answer = dspy.OutputField(desc="Answer to the question based on the context")

class QnA(dspy.Module):
    """Question answering module using DSPy."""
    
    def __init__(self, provider=None):
        super().__init__()
        self.qa = dspy.ChainOfThought(QnASignature)
        if provider:
            dspy.settings.configure(lm=provider)
    
    def forward(self, question):
        """
        Answer a question based on the provided context.
        
        Args:
            question (str): Question to be answered
            
        Returns:
            str: Answer to the question
        """
        prediction = self.qa(question=question)
        return prediction

def qna(args):
    """Run question answering task.
    
    Args:
        args (argparse.Namespace): Command line arguments
    """
    # Create task
    qna = QnA()
    answer = qna(question=args.question)

    # Answer
    print("❓Question:", args.question)
    print("✅ Answer:", answer.answer)
    print("🔎 Reasoning:", answer.reasoning)

def main(args):
    """Run question answering task."""
    if args.question:
        qna(args)