import matplotlib.pyplot as plt
from data_handler import get_data

def visualize_points_vs_fg(player_stats_df):
    """
    Visualize player points vs field goal percentage.
    """
    if not player_stats_df.empty:
        # Sort DataFrame by 'PTS' in ascending order
        sorted_df = player_stats_df.sort_values(by='PTS', ascending=True)

        # Exclude the first three players with the lowest average points
        filtered_df = sorted_df.iloc[3:].reset_index(drop=True)

        # Scatter Plot with FG% on the y-axis and Points on the x-axis
        plt.figure(figsize=(12, 8))
        players = filtered_df['Players']
        fg_percentage = filtered_df['FG%']
        points = filtered_df['PTS']

        for i, player in enumerate(players):
            # Plot the point
            plt.scatter(points[i], fg_percentage[i], alpha=0.5)

            # Display the player name with stats underneath
            plt.text(points[i], fg_percentage[i] + 0.5, f"{player}\n({filtered_df['PTS'][i]:.1f}pts, {filtered_df['FG%'][i]:.1f}%FG)",
                     fontsize=10, ha='center', va='bottom', alpha=0.7)

        plt.xlabel("Points (PTS)")
        plt.ylabel("Field Goal Percentage (FG%)")
        plt.title("Scatter Plot of Player Points vs. FG% (Excluding Lowest 3)")
        plt.show()
    else:
        print("DataFrame is empty or does not contain necessary columns. Unable to create the scatter plot.")

import matplotlib.pyplot as plt

def visualize_rebounds(player_stats_df):
    """
    Visualize rebounds. OREB + DREB = REB (total)
    """
    if not player_stats_df.empty:
        plt.figure(figsize=(12, 8))

        # Bar graph with distinct colors for OREB and DREB
        bars = plt.bar(player_stats_df.index, player_stats_df['OREB'], color='orange', label='Offensive Rebounds (OREB)')
        plt.bar(player_stats_df.index, player_stats_df['DREB'], bottom=player_stats_df['OREB'], color='blue', label='Defensive Rebounds (DREB)')

        # Set x-axis ticks and labels with a 30-degree rotation
        plt.xticks(player_stats_df.index, player_stats_df['Players'], rotation=30, ha='right')

        # Add actual 'REB' values to the top of each bar
        for bar, reb in zip(bars, player_stats_df['REB']):
            plt.text(bar.get_x() + bar.get_width() / 2 - 0.1, reb, f'{reb}', ha='center', va='bottom', color='black', fontweight='bold')

        # Add legend
        plt.legend()

        plt.xlabel("Players")
        plt.ylabel("Number of Rebounds")
        plt.title("Bar Graph of Player Rebounds (OREB and DREB)")
        plt.show()
    else:
        print("DataFrame is empty or does not contain necessary columns. Unable to create the bar graph.")


# Main Execution
player_stats_df = get_data()

# Visualize
visualize_points_vs_fg(player_stats_df)
visualize_rebounds(player_stats_df)