# Contributing to 100 Days of Python Bootcamp

First off, thank you for considering contributing to this project! 🎉

This document provides guidelines for contributing to the 100 Days of Python Bootcamp repository. Following these guidelines helps maintain code quality and makes the contribution process smooth for everyone involved.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Project Structure](#project-structure)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Community](#community)

---

## 📜 Code of Conduct

This project adheres to a code of conduct that all contributors are expected to follow:

- **Be respectful** and considerate in your communication
- **Be collaborative** and open to feedback
- **Be patient** with beginners and help them learn
- **Focus on what is best** for the community and learning
- **Show empathy** towards other community members

---

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **Screenshots** if applicable
- **Environment details** (OS, Python version, etc.)

**Bug Report Template:**
```markdown
**Description:**
A clear description of what the bug is.

**To Reproduce:**
1. Go to '...'
2. Run '...'
3. See error

**Expected behavior:**
What you expected to happen.

**Screenshots:**
If applicable, add screenshots.

**Environment:**
- OS: [e.g., Windows 10, macOS 12.0, Ubuntu 20.04]
- Python Version: [e.g., 3.8.5]
- Browser (if web-related): [e.g., Chrome 95]
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear title** describing the enhancement
- **Provide detailed description** of the suggested enhancement
- **Explain why** this enhancement would be useful
- **List alternatives** you've considered
- **Provide examples** or mockups if applicable

### Code Contributions

#### Types of Contributions Welcome:

1. **Bug fixes** - Fix existing issues
2. **New project solutions** - Alternative approaches to daily challenges
3. **Documentation improvements** - Better explanations, typo fixes
4. **Code optimization** - Performance improvements
5. **Test additions** - Unit tests for existing code
6. **Tutorial additions** - Step-by-step guides for projects

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- A GitHub account
- Basic knowledge of Python and Git

### Setup Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork locally:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/100DaysOfPythonBootCamp.git
   cd 100DaysOfPythonBootCamp
   ```

3. **Add the upstream repository:**
   ```bash
   git remote add upstream https://github.com/CemRoot/100DaysOfPythonBootCamp.git
   ```

4. **Create a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Create a new branch for your work:**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

---

## 🔄 Development Workflow

1. **Keep your fork up to date:**
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Make your changes** in your feature branch

3. **Test your changes** thoroughly

4. **Commit your changes** following our commit guidelines

5. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request** from your fork to the main repository

---

## 📝 Code Standards

### Python Style Guide

We follow **PEP 8** - the official Python style guide. Key points:

#### Naming Conventions

```python
# Variables and functions: lowercase with underscores
user_name = "John"
def calculate_total():
    pass

# Classes: PascalCase
class CoffeeMachine:
    pass

# Constants: UPPERCASE with underscores
MAX_RETRY_COUNT = 3
API_KEY = "your-api-key"

# Private methods/variables: leading underscore
def _internal_method():
    pass
```

#### Code Formatting

```python
# Indentation: 4 spaces (not tabs)
def example_function(param1, param2):
    if param1 > 0:
        return param1 + param2
    return 0

# Line length: Maximum 79 characters
# Break long lines appropriately
result = some_function_with_long_name(
    argument1,
    argument2,
    argument3
)

# Blank lines:
# - 2 blank lines between top-level functions and classes
# - 1 blank line between methods in a class

class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass


def standalone_function():
    pass
```

#### Imports

```python
# Standard library imports first
import os
import sys
from datetime import datetime

# Third-party imports second
import requests
import pandas as pd
from flask import Flask

# Local application imports last
from my_module import my_function
```

#### Documentation

```python
def calculate_area(width, height):
    """
    Calculate the area of a rectangle.

    Args:
        width (float): The width of the rectangle
        height (float): The height of the rectangle

    Returns:
        float: The area of the rectangle

    Raises:
        ValueError: If width or height is negative
    """
    if width < 0 or height < 0:
        raise ValueError("Dimensions must be positive")
    return width * height
```

#### Comments

```python
# Good: Explain WHY, not WHAT
# Calculate tax separately to avoid rounding errors
tax = price * 0.18

# Bad: State the obvious
# Multiply price by 0.18
tax = price * 0.18
```

### Code Quality Checklist

Before submitting, ensure your code:

- ✅ Follows PEP 8 style guidelines
- ✅ Has descriptive variable and function names
- ✅ Includes docstrings for functions and classes
- ✅ Has no commented-out code (remove it)
- ✅ Has no unnecessary print statements
- ✅ Handles errors gracefully
- ✅ Is tested and works as expected
- ✅ Doesn't break existing functionality

---

## 💬 Commit Message Guidelines

Good commit messages help others understand your changes. Follow these guidelines:

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

#### Type

Must be one of the following:

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Code style changes (formatting, missing semicolons, etc.)
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **chore**: Changes to build process or auxiliary tools

#### Scope

The scope should be the name of the day or project affected:

- `day-1`, `day-7`, `day-20-21`
- `snake-game`, `password-manager`, `flask-blog`
- `readme`, `contributing`, `requirements`

#### Subject

- Use imperative, present tense: "add" not "added" or "adds"
- Don't capitalize first letter
- No period (.) at the end
- Maximum 50 characters

#### Body (Optional)

- Explain **what** and **why**, not **how**
- Wrap at 72 characters
- Separate from subject with blank line

#### Footer (Optional)

- Reference issues: `Closes #123`, `Fixes #456`

### Examples

**Good commit messages:**

```bash
feat(day-7): add hangman game with ASCII art

- Implement word selection from word list
- Add ASCII art for different stages
- Include win/lose game logic

Closes #15

---

fix(snake-game): resolve collision detection bug

The snake was passing through walls in certain conditions.
Added boundary checking for all four walls.

Fixes #42

---

docs(readme): update installation instructions

Add steps for creating virtual environment and
installing dependencies on different operating systems.

---

refactor(day-10): improve calculator code structure

Extract arithmetic operations into separate functions
for better readability and maintainability.
```

**Bad commit messages:**

```bash
# Too vague
update code

# Not descriptive
fixed bug

# Past tense
added new feature

# Too long subject
feat(day-7): add hangman game with ASCII art, word selection, and complete game logic including win/lose conditions
```

---

## 🔃 Pull Request Process

### Before Creating a PR

1. **Update your branch** with the latest main branch
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Test your changes** thoroughly

3. **Review your changes** yourself first
   ```bash
   git diff main..your-branch
   ```

4. **Clean up your commits** if needed
   ```bash
   git rebase -i HEAD~3  # Interactive rebase last 3 commits
   ```

### Creating a Pull Request

1. **Push your branch** to your fork

2. **Go to the repository** on GitHub and click "New Pull Request"

3. **Fill out the PR template:**

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Related Issue
Closes #(issue number)

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
Describe how you tested your changes:
- Test 1
- Test 2

## Screenshots (if applicable)
Add screenshots here

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have tested my code and it works as expected
```

4. **Request review** from maintainers

### During Review

- **Be responsive** to feedback
- **Make requested changes** in new commits
- **Don't force push** after review has started (unless requested)
- **Be patient** - reviews take time
- **Be open** to suggestions and alternative approaches

### After Approval

- Maintainers will merge your PR
- Your contribution will be added to the project
- You can delete your feature branch

---

## 📁 Project Structure

When adding new content, follow the existing structure:

```
100DaysOfPythonBootCamp/
│
├── 1)Beginner-Project/
│   └── [DAY-X]/                    # Use this format for new days
│       ├── main.py                 # Main project file
│       ├── supporting_file.py      # Additional modules
│       └── README.md               # Project-specific README (optional)
│
├── 2)Intermadiate-Project/
├── 3)Intermadiate-Plus-Project/
└── 4)Advanced-Project/
```

### File Naming Conventions

- **Project files**: `[DAY-X]/main.py` or `[DAY-X]Project-Name.py`
- **Supporting files**: descriptive names (e.g., `hangman_words.py`, `snake.py`)
- **README files**: Always `README.md` (uppercase)

---

## 🧪 Testing Guidelines

### Manual Testing

For each contribution:

1. **Run the code** and verify it works
2. **Test edge cases** and invalid inputs
3. **Test on different Python versions** if possible
4. **Document any dependencies** needed

### Example Test Cases

```python
# Example: Testing password generator
def test_password_generator():
    # Test length
    password = generate_password(10)
    assert len(password) == 10

    # Test character types
    password = generate_password(20)
    assert any(c.isupper() for c in password)
    assert any(c.islower() for c in password)
    assert any(c.isdigit() for c in password)
```

---

## 📖 Documentation

### Code Documentation

- **Docstrings**: Add to all functions and classes
- **Comments**: Explain complex logic
- **Type hints**: Use when it improves clarity

### Project Documentation

When adding a new project:

1. **Update main README.md** if needed
2. **Create project README** (optional) with:
   - Project description
   - How to run
   - Features implemented
   - Concepts learned
   - Screenshots/demos

Example project README structure:

```markdown
# Day X - Project Name

## Description
Brief description of the project.

## Features
- Feature 1
- Feature 2

## How to Run
```bash
cd 1)Beginner-Project/[DAY-X]
python main.py
```

## Concepts Learned
- Concept 1
- Concept 2

## Screenshots
[Add screenshots here]
```

---

## 🌐 Community

### Getting Help

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and general discussions
- **Email**: koyluoglu.cem@lll.kpi.ua

### Staying Updated

- **Watch** the repository for updates
- **Star** the repository to bookmark it
- **Follow** @CemRoot on GitHub

---

## 🙏 Recognition

Contributors will be recognized in the following ways:

- Listed in project contributors
- Mentioned in release notes (for significant contributions)
- Public acknowledgment in the README (for major features)

---

## 📝 License

By contributing to this project, you agree that your contributions will be licensed under the same [MIT License](First-Read-Me-Folder/license.md) that covers the project.

---

## ✨ Thank You!

Thank you for contributing to 100 Days of Python Bootcamp! Your efforts help make this learning resource better for everyone.

**Happy Coding! 🐍**

---

<div align="center">

**Questions?** Feel free to reach out!

[![Email](https://img.shields.io/badge/Email-koyluoglu.cem%40lll.kpi.ua-red?style=flat&logo=gmail)](mailto:koyluoglu.cem@lll.kpi.ua)
[![GitHub](https://img.shields.io/badge/GitHub-CemRoot-black?style=flat&logo=github)](https://github.com/CemRoot)

</div>
