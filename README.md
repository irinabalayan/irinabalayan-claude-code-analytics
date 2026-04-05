# Project Overview

This project processes and analyzes telemetry logs to extract insights about API requests and tool usage. It includes data ingestion, cleaning, and visualization steps.

## Folder Structure

# Claude Code Analytics Platform

This project processes and analyzes telemetry logs to extract insights about API requests and tool usage. It includes data ingestion, cleaning, analysis, anomaly detection, and a Streamlit dashboard for visualization.

## Folder Structure

platform/
├── src/
│   ├── ingest.py           # Handles data loading
│   ├── process.py          # Cleans and preprocesses the data
│   ├── analyze.py          # Performs analysis, anomaly detection, prediction
│   ├── dashboard.py        # Creates visualizations for the dashboard
│   └── database.py         # Manages database interactions
├── data/
│   ├── raw/                # Raw telemetry logs (e.g., telemetry_logs.jsonl)
│   └── processed/          # Placeholder for processed data
├── output/                 # Analysis results and visualizations
│   ├── anomaly_detection.csv
│   ├── predicted_usage.csv
│   ├── api_tokens.png
│   ├── tool_success.png
│   └── trend.png
├── db/                     # SQLite database files
├── main.py                 # Main script to run analysis and dashboard
├── README.md
└── requirements.txt

resources/
├── generate_fake_data.py    # Script for generating fake data

venv/                         # Virtual environment for dependencies

## Features

- Dashboard visualizing token usage trends and anomalies
- Token usage prediction for future days
- Cost analysis by role/practice
- Session length and peak hour analysis
- Tool usage statistics

## Requirements

- Python 3.8 or higher
- Libraries:
  - pandas
  - matplotlib
  - seaborn
  - streamlit
  - scikit-learn
  - numpy

Install dependencies via:

```bash
pip install -r requirements.txt

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/irinabalayan/irinabalayan-claude-code-analytics.git
   cd irinabalayan-claude-code-analytics
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place raw telemetry logs in the `data/raw/` directory.
2. Run the main script:
   ```bash
   streamlit run main.py
   ```
3. Outputs will be saved in the `output/` directory.

## Outputs
Outputs will be saved in the output/ directory.

- **Anomaly Detection:** output/anomaly_detection.csv
- **Predicted Usage:** output/predicted_usage.csv
- **Visualizations:**
  - `api_tokens.png:` API token usage bar plot
  - `tool_success.png:` Tool success rates bar plot
  - `trend.png:` Line plot of token trends over time
 
## Notes

- Ensure the `data/raw/telemetry_logs.jsonl` file exists before running the script.
- Modify the scripts in `src/` as needed to customize the analysis.
- The repository contains large files (telemetry_logs.jsonl > 50MB). Consider using Git LFS for large datasets.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
