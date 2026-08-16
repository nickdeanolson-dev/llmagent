# How the Calculator Renders Results to the Console

## Overview
The calculator application uses a modular approach to evaluate mathematical expressions and render results to the console. The rendering process involves three key components:

1. **Calculator Class** (`pkg/calculator.py`) - Handles expression evaluation
2. **Renderer** (`pkg/render.py`) - Formats output as JSON
3. **Main Application** (`main.py`) - Orchestrates the workflow

## Rendering Process

### Step 1: Expression Evaluation
The `Calculator` class parses and evaluates mathematical expressions using operator precedence and stack-based evaluation.

### Step 2: Result Formatting
The `format_json_output` function in `render.py` creates a structured JSON representation:
```json
{
  "expression": "input_expression",
  "result": computed_result
}
```

### Step 3: Console Output
The `main.py` script coordinates the process:
1. Takes expression from command-line arguments
2. Evaluates using `Calculator`
3. Formats result using `format_json_output`
4. Prints the formatted JSON to console

## Example
Running `python main.py "3 + 5"` produces:
```json
{
  "expression": "3 + 5",
  "result": 8
}
```

This approach ensures clear, structured output that clearly presents both the input expression and its computed result.