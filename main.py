import pandas as pd
from selenium import webdriver
import matplotlib.pyplot as plt

# Set Constants
DRIVER_PATH = '/Users/tyler/Documents/chromedriver-mac-arm64/chromedriver'

# Web Scraping and Data Extraction
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://www.nba.com/stats/team/1610612746/players-traditional?LastNGames=15")

# Extract data table
try:
    df_stats = pd.read_html(driver.page_source)[3]
except IndexError as e:
    print(f"Error: {e}. Unable to extract data table.")
    df_stats = pd.DataFrame()

# Close WebDriver
driver.close()

# Check if the DataFrame is not empty
if not df_stats.empty:
    # Scatter Plot with FG% on the y-axis and Points on the x-axis
    plt.figure(figsize=(10, 6))
    players = df_stats['Players']
    fg_percentage = df_stats['FG%']
    points = df_stats['PTS']  # Use 'PTS' for Points

    plt.scatter(points, fg_percentage, alpha=0.5)
    for i, player in enumerate(players):
        plt.annotate(player, (points[i], fg_percentage[i]), fontsize=10, alpha=0.7)
    plt.xlabel("Points (PTS)")
    plt.ylabel("Field Goal Percentage (FG%)")
    plt.title("Scatter Plot of Points vs. FG% with Player Names")
    plt.show()
else:
    print("DataFrame is empty. Unable to create the scatter plot.")
