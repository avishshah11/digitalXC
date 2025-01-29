# DigitalXC Secret Santa Coding Challenge

## Overview
This project contains the source code for the logic behind assigning employees to give secret presents to a randomly selected "child" each year. The assignment ensures that no one is assigned to themselves, and it avoids repeating pairings from previous years.

## Project Structure
- `src/`: Main source code for generating Secret Santa assignments, with the logic divided into modular subfiles for better organization and maintainability.
- `assets/`: Folder containing input data and the generated output file.
- `README.md`: Coding Challenge documentation.
- `requirements.txt`: Lists Python dependencies.

## Requirements
- Python 3.x
- Pandas library (included in `requirements.txt`)

## Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the code:
   ```bash
   cd src
   python main.py
   ```

## Output
The output file, `Secret_Santa_Challenge.csv`, will be saved in the `assets` directory.
