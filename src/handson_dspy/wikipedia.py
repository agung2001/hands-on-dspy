"""Basic DSPy module with example functionality.

This module demonstrates core DSPy features including:
- Creating language model modules
- Defining signatures for tasks
- Building simple pipelines
"""

import dspy

# Define a Tool
def wikipedia_search(query: str) -> list[str]:
    """Retrieves abstracts from Wikipedia."""
    # Existing Wikipedia Abstracts Server
    results = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')(query, k=3) 
    return [x['text'] for x in results]

# Define a Signature
class WikipediaSearch(dspy.Signature):
    """Search for abstracts on Wikipedia."""
    question = dspy.InputField()
    answer = dspy.OutputField()

class Wikipedia(dspy.Module):
    """Wikipedia module using DSPy."""
    
    def __init__(self, provider=None):
        super().__init__()
        self.qa = dspy.ReAct(WikipediaSearch, tools=[wikipedia_search])
        if provider:
            dspy.settings.configure(lm=provider)
    
    def forward(self, question):
        """
        Search for abstracts on Wikipedia.
        
        Args:
            question (str): Question to be answered
            
        Returns:
            str: Answer to the question
        """
        prediction = self.qa(question=question)
        return prediction

def search_wikipedia(args):
    """Run wikipedia search task."""
    # Define ReAct Module
    react_module = dspy.ReAct('question -> response', tools=[wikipedia_search])

    # Run
    react_response = react_module(question=args.question)

    print("Answer: ", react_response.response)
    print("\nReasoning: ", react_response.reasoning)

def main(args):
    """Run question answering task."""
    if args.wikipedia and args.question:
        search_wikipedia(args)
