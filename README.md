# PubMed Paper Scraper

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://pubmed-paper-scraper.streamlit.app/)

This project is a simple Streamlit web application that allows users to search for academic papers on PubMed based on a specific topic. The app retrieves a list of PubMed IDs (PMIDs) for relevant papers and displays details such as the title, journal, publication date, and abstract for each paper.

## Features

- **Search by Topic:** Users can input a topic (e.g., "machine learning in healthcare") to find relevant academic papers.
- **Rate Limiting:** The app uses rate limiting to adhere to PubMed API usage policies.
- **Error Handling:** The app gracefully handles errors such as HTTP and URL errors, providing meaningful feedback to the user.
- **Paper Details:** For each paper, the app displays the title, journal, publication date, and abstract, with a link to read more on PubMed.

## How to Use

1. **Enter a Topic:** Type in the topic you want to search for in the provided text input box.
2. **Search:** Click on the "Search" button to start retrieving papers related to your topic.
3. **View Results:** The app will display the first few papers it finds, including the title, journal, publication date, and abstract. You can click the link provided to read more on PubMed.

## Deployment

This app is deployed and live on Streamlit Cloud. You can access it [here](https://pubmed-paper-scraper.streamlit.app/).

## Running Locally

To run this app locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mathew-2/pubmed-paper-scraper.git
   cd pubmed-paper-scraper

2. **Install the required dependencies:**
   Ensure you have Python installed, then install the necessary Python packages using pip:
   ```bash
   pip install -r requirements.txt
3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
4. **Open your browser:**
   Once the app is running, it should automatically open in your default web browser. If not, go to *http://localhost:8501* to access the app.

## Requirements
- Python 3.7 or above
- The following Python packages:
  - streamlit
  - ratelimit
  - urllib3
These can be installed using the requirements.txt file provided in the repository.

## Acknowledgments
- This app utilizes the PubMed API to fetch data on academic papers.
- The application is built using Streamlit, an open-source app framework for Machine Learning and Data Science.

## Links
Live App: https://pubmed-paper-scraper.streamlit.app/
