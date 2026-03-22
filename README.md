# AI Job Assistant

A lightweight Python project for analyzing job descriptions and classifying AI-related roles using a weighted keyword taxonomy.

## Features

- Define AI job categories in `taxonomy.py`
- Classify job descriptions with weighted keyword scoring
- Support multi-label score distribution
- Read input from `sample_jd.txt`
- Save analysis results to `report.txt`
- Visualize category scores with charts

## Project Structure

ai-job-assistant/
- taxonomy.py
- classifier.py
- visualize.py
- sample_jd.txt
- report.txt
- README.md
- .gitignore

## How It Works

The classifier uses a weighted keyword scoring mechanism.

For each category:
- it checks whether keywords appear in the job description
- counts keyword frequency
- multiplies frequency by keyword weight
- sums the scores for each category

The category with the highest score is selected as the primary direction.

## Example Categories

- Model_Algo
- AI_Infra
- Perception
- Decision_Planning
- Engineering_Tooling

## How to Run

### 1. Run the classifier
```bash
python classifier.py