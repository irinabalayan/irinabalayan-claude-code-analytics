# Project Overview

This project processes and analyzes telemetry logs to extract insights about API requests and tool usage. It includes data ingestion, cleaning, and visualization steps.

## Folder Structure

draft/
├── src/
│   ├── ingest.py # Handles data loading
│   ├── process.py # Cleans and preprocesses the data
│   ├── analyze.py # Performs analysis on the data
│   ├── dashboard.py # Creates visualizations for the dashboard
│   └── database.py # Manages database interactions
├── data/
│   ├── raw/ # Contains raw telemetry logs (e.g., telemetry_logs.jsonl)
│   └── processed/ # Placeholder for processed data
├── output/
│   ├── llm_usage_summary.csv # Generated LLM usage log
│   ├── predicted_usage.csv # Predicted usage data
│   ├── api_tokens.png # Visualization of API token usage
│   ├── tool_success.png # Visualization of tool success rates
│   └── trend.png # Visualization of trends
├── dashboard/
│   └── app.py # Entry point for the dashboard application
├── db/ # Placeholder for database-related files
└── main.py # Main script to run the analysis and plots

resources/
├── generate_fake_data.py # Script for generating fake data

venv/ # Virtual environment for managing dependencies

## Requirements

- Python 3.8 or higher
- Libraries:
  - pandas
  - matplotlib
  - seaborn
  - flask

## Setup

1. Clone the repository:
   ```bash
   git clone <your-repo-link>
   cd draft
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
   python main.py
   ```
3. Outputs will be saved in the `output/` directory.
4. To launch the dashboard:
   ```bash
   python dashboard/app.py
   ```

## Outputs

- **LLM Usage Summary**: A CSV file summarizing token usage and costs, saved as `output/llm_usage_summary.csv`.
- **Predicted Usage**: A CSV file with predicted usage data, saved as `output/predicted_usage.csv`.
- **Visualizations**:
  - `api_tokens.png`: Bar plot of API token usage.
  - `tool_success.png`: Bar plot of tool success rates.
  - `trend.png`: Line plot of trends over time.

## Notes

- Ensure the `data/raw/telemetry_logs.jsonl` file exists before running the script.
- Modify the scripts in `src/` as needed to customize the analysis.
- The dashboard requires Flask to be installed.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
