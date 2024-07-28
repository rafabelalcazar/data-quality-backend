# Data Quality Back

This project aims to ensure the quality of data in our system by implementing various data validation and cleansing techniques.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Data quality is crucial for any organization to make informed decisions and maintain accurate records. This project focuses on the backend implementation of data quality checks and processes.

## Features
- Data validation: Implementing validation rules to ensure data integrity.
- Data cleansing: Removing or correcting inaccurate or inconsistent data.
- Data profiling: Analyzing data to identify patterns, anomalies, and data quality issues.
- Data monitoring: Continuously monitoring data quality to detect and resolve issues in real-time.

## Installation
1. Clone the repository: `git clone https://github.com/your-username/data-quality-back.git`
2. Run the local environment: `source .venv/Scripts/activate `
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage
1. Run the server in dev mode `fastapi dev main.py`.
2. Make post to test the server : `http://127.0.0.1:8000/test/`
3. Make post, and upload a file  `http://127.0.0.1:8000/upload-dataset/`

## Contributing
Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md) when making changes to this project.

## License
This project is licensed under the [MIT License](LICENSE).
