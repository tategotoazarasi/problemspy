# problemspy

A collection of competitive programming solutions written in Python. This repository serves as a personal log of solved problems from various platforms like Kattis and LeetCode.

## Project Structure

The project is organized into modules based on the problem platform.

- `main.py`: The main script used to discover and run all unit tests.
- `kattis.py`, `leetcode.py`: Modules containing solutions for problems from the respective platforms.
- `test_kattis.py`, `test_leetcode.py`: Unit tests for the solutions, using Python's built-in `unittest` framework.
- `requirements.txt`: A list of Python packages required for documentation.
- `docs/`: Contains configuration files for Sphinx documentation.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/tategotoazarasi/problemspy.git
    cd problemspy
    ```

2.  **Install dependencies (for documentation):**
    ```bash
    pip install -r requirements.txt
    ```

## Testing

The project uses Python's standard `unittest` framework. A test runner is configured in `main.py`.

To run all tests, execute the `main.py` script:

```bash
python main.py
```

Alternatively, you can use the `unittest` module to discover and run tests:

```bash
python -m unittest discover
```

## Documentation

The project uses Sphinx to automatically generate API documentation from the docstrings in the code.

1.  **Generate the documentation:**
    ```bash
    sphinx-build -b html docs docs/_build/html
    ```

2.  **View the documentation:**
    Open the `docs/_build/html/index.html` file in your web browser to view the generated documentation.
