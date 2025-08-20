[![Stop Prompt Engineering! Program Your LLMs with DSPy](https://img.youtube.com/vi/Zv4LjO8teqE/0.jpg)](https://www.youtube.com/watch?v=Zv4LjO8teqE)

Hands on dspy is a project to help you get started with dspy.

## Install 
Run this command to install the project
```bash
cp .env.example .env # Don't forget to configure the .env file
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m handson_dspy --help
```

## Usage
- Example: `--example`
- Question: `--question {question}`
- Summarize text: `--summarize --file-path {/path/to/file}`

## Modules
- Predict: Predict the answer to a question
- Chain of Thought: Generate a reasoning chain of thought
- Chain of Program: Generate a program to solve a problem
- ReAct: Implement Reasoning + Actiong by interleaving thought and action(via tools), and observations in a structured loop.
- Multi Chain Comparison: Compare multiple chains of thought and program to find the best one
- Majority: Use majority voting to combine the output of multiple chains of thought and program

## Resource
- [dspy](https://github.com/stanfordnlp/dspy)