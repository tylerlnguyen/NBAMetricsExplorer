import matplotlib.pyplot as plt
from data_handler import get_data


def visualize_points_vs_fg(df_stats):
    if not df_stats.empty:
        # Sort DataFrame by 'PTS' in ascending order
        df_sorted = df_stats.sort_values(by='PTS', ascending=True)

        # Exclude the first three players with the lowest average points
        df_filtered = df_sorted.iloc[3:].reset_index(drop=True)

        # Scatter Plot with FG% on the y-axis and Points on the x-axis
        plt.figure(figsize=(12, 8))
        players = df_filtered['Players']
        fg_percentage = df_filtered['FG%']
        points = df_filtered['PTS']

        for i, player in enumerate(players):
            # Plot the point
            plt.scatter(points[i], fg_percentage[i], alpha=0.5)

            # Display the player name with stats underneath
            plt.text(points[i], fg_percentage[i] + 0.5, f"{player}\n({df_filtered['PTS'][i]:.1f}pts, {df_filtered['FG%'][i]:.1f}%FG)",
                     fontsize=10, ha='center', va='bottom', alpha=0.7)

        plt.xlabel("Points (PTS)")
        plt.ylabel("Field Goal Percentage (FG%)")
        plt.title("Scatter Plot of Player Points vs. FG% (Excluding Lowest 3)")
        plt.show()
    else:
        print("DataFrame is empty. Unable to create the scatter plot.")


# Main Execution
df_stats = get_data()

# Visualize Points vs. FG%
visualize_points_vs_fg(df_stats)
