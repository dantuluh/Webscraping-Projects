from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd


path = "/Users/new/Desktop/DATA FOR PROJECTS/FOOTBALL_WEB_SCRAPPING/chromedriver/chromedriver-mac-x64/chromedriver"
service = Service(path)
driver = webdriver.Chrome(service=service)

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
driver.get(website)

all_matches_button = driver.find_element('xpath', '//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element('id', 'country'))
dropdown.select_by_visible_text('England')

time.sleep(5)

matches = driver.find_elements('xpath', '//tr')

date = []
home_team = []
home_score = []  # New list for home team's score
away_score = []  # New list for away team's score
away_team = []

# Loop through each match row
for match in matches:
    try:
        # Skip rows with "Next match"
        if "Next match" in match.text:
            print("Skipping row with 'Next match'")
            continue

        # Extract data from the row
        match_date = match.find_element('xpath', './td[1]').text
        home = match.find_element('xpath', './td[3]').text
        score = match.find_element('xpath', './td[4]').text
        away = match.find_element('xpath', './td[5]').text

        # Split the score into home_score and away_score
        if '-' in score:
            home_goals, away_goals = score.split('-')
            home_goals = home_goals.strip()
            away_goals = away_goals.strip()

            date.append(match_date)
            home_team.append(home)
            home_score.append(int(home_goals))  # Convert to integer
            away_score.append(int(away_goals))  # Convert to integer
            away_team.append(away)
        else:
            # Handle invalid scores (e.g., "? - ?")
            print(f"Skipping row with invalid score: {score}")
    except Exception as e:
        print(f"Skipping a row due to error: {e}")
        continue

input("Press Enter to close the browser...")
driver.quit()

# Debug: Print the lengths of the lists
print(f"Length of date: {len(date)}")
print(f"Length of home_team: {len(home_team)}")
print(f"Length of home_score: {len(home_score)}")
print(f"Length of away_score: {len(away_score)}")
print(f"Length of away_team: {len(away_team)}")


df = pd.DataFrame({'date': date, 'home_team': home_team, 'home_score': home_score, 'away_score': away_score, 'away_team': away_team})

# Add the final_score column
df['final_score'] = df['home_team'] + ' ' + df['home_score'].astype(str) + ' - ' + df['away_score'].astype(str) + ' ' + df['away_team']

df.to_csv('football_data.csv', index=False)

print(df)
