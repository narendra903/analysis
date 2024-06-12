# MyDataAnalysisProject

A data analysis project to scrape and analyze laptop data from 91mobiles.com.

![Human guiding robots in data analysis](docs/images/robot_data_analysis.png)

## Table of Contents
- [Project Description](#project-description)
- [Getting Started](#getting-started)
- [Directory Structure](#directory-structure)

## Project Description

This project involves web scraping and data analysis of laptop data from the 91mobiles.com website. The primary objective is to collect comprehensive information about various laptops, including their specifications, prices, and performance metrics. Using this data, we aim to derive insights that can help consumers make informed purchasing decisions.

Key features of this project include:
- **Web Scraping**: Automated data collection from 91mobiles.com using Selenium and Pyppeteer.
- **Data Cleaning**: Processing and cleaning raw data to ensure accuracy and consistency.
- **Data Analysis**: Analyzing the cleaned data to extract meaningful insights and trends.
- **Visualization**: Creating visual representations of the data to facilitate easy understanding.
- **Reporting**: Generating reports to summarize the findings and insights.

Technologies used:
- **Python**: The primary programming language for data scraping and analysis.
- **Selenium & Pyppeteer**: Tools for web scraping.
- **Pandas**: A powerful data manipulation and analysis library.
- **Matplotlib & Seaborn**: Libraries for data visualization.

![Project Roadmap](docs/images/project_roadmap.png)

## Getting Started

To get started with this project, follow the steps below to set up your local development environment.

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.x**: The programming language used for this project.
- **pip**: Python package installer.

### Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
   Clone this repository to your local machine using the following command:
    ```bash
    git clone https://github.com/yourusername/my_data_analysis_project.git
    cd my_data_analysis_project
    ```

2. **Create a virtual environment** (optional but recommended):
   Create and activate a virtual environment to manage dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
   Install the necessary Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Jupyter Notebook**:
   Launch Jupyter Notebook to start working with the provided notebooks:
    ```bash
    jupyter notebook
    ```

5. **Download and place the raw data**:
   Ensure that the raw data (`laptops_data.csv`) is placed in the `data/raw` directory:
    ```bash
    mv path/to/laptops_data.csv data/raw/laptops_data.csv
    ```

Now you are ready to explore the notebooks and perform data analysis on the scraped laptop data.



## Documentation

- [Web Scraping Documentation](docs/web_scraping_documentation.md)


## Directory Structure



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
