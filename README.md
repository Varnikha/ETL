# Python-Based ETL Pipeline

## Overview
This project implements a Python-based ETL pipeline that extracts raw housing data,
cleans and transforms it, validates data quality, and loads an analytics-ready dataset.

## Project Structure
- data/raw: Original input dataset
- data/processed: Cleaned output dataset
- scripts: ETL pipeline code
- notebooks: Data exploration and visualization

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the ETL pipeline:
   python scripts/etl_pipeline.py

## Output
- Cleaned dataset saved to:
  data/processed/clean_housing_data.csv

## Features
- Modular ETL design
- Missing value handling
- Data validation checks
- Analytics-ready output
