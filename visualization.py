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

# Main Execution
player_stats_df = get_data()

# Visualize Points vs. FG%
visualize_points_vs_fg(player_stats_df)
