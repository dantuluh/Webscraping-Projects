# Webscraping-Projects

**Premier League 2024/25 Prediction**

**Overview**

This project aims to predict key factors for the 2024/25 Premier League season using match data extracted from Adam Choi's website. The data was collected through web scraping, cleaned, analyzed, and then used to build a predictive model.

**Project Structure**

/Football-Prediction-24-25
├── data/
│   ├── football_data.csv  # Collected dataset
├── scripts/
│   ├── script.py          # Web scraping script
│   ├── datastats.py       # Analysis & prediction script
├── notebooks/
│   ├── analysis.ipynb     # (If you used Jupyter)
├── README.md              # Project description
├── requirements.txt       # Python dependencies

**Data Collection**

**Source**: Data was extracted from Adam Choi's football statistics website.

**Technology Used**: Selenium for web scraping.

**Extraction Process:**

Opened the website using a Chrome WebDriver.

Clicked the "All matches" button.

Selected England as the country.

Extracted match details: date, home team, away team, home score, and away score.

Saved the data into football_data.csv.

**Data Analysis**

Loaded the dataset using Pandas.

Checked for and handled missing values:

Dropped rows with missing home_team, away_team, home_score, or away_score.

Ensured data validity:

Removed matches with negative scores.

Dropped duplicate records.

Performed exploratory data analysis (EDA) using Matplotlib and Seaborn:

Visualized match outcomes.

Analyzed goal trends and team performance.

**Prediction Model**

Machine Learning Model: Linear Regression.

Steps:

Preprocessed the dataset:

Used SimpleImputer to handle missing values.

Split the dataset into training and testing sets.

Trained a Linear Regression model.

Evaluated using Mean Squared Error (MSE).

**How to Run the Project**

**Clone the repository:**

git clone https://github.com/yourusername/Football-Prediction-24-25.git
cd Football-Prediction-24-25

**Install dependencies:**

pip install -r requirements.txt

**Run Web Scraping Script:**

python scripts/script.py

**Run Analysis & Prediction Script:**

python scripts/datastats.py

**Future Improvements**

Improve model accuracy by experimenting with different algorithms.

Expand analysis by incorporating additional metrics (e.g., possession, shots on target).

Automate data scraping at regular intervals for real-time predictions.

**Contributing**

Feel free to fork this repository and contribute! If you find any issues, open a pull request or report them in the issues section.

**License**

This project is open-source and available under the MIT License.

