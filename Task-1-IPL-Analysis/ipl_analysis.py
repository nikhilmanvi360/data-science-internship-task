"""
IPL Cricket Data Analytics Project
Comprehensive analysis of IPL match data including team performance,
toss impact analysis, and venue performance trends.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

# Set visualization style for professional appearance
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

# Define color palettes
TEAM_COLORS = {
    'MI': '#004BA0',
    'CSK': '#FFEB3B',
    'RCB': '#DC143C',
    'KKR': '#9933CC',
    'DC': '#1E90FF',
    'SRH': '#FF8C00'
}

TOSS_COLORS = ['#2ecc71', '#e74c3c']
VENUE_COLORS = sns.color_palette("husl", 8)

# ============================================================================
# DATA LOADING & CLEANING
# ============================================================================

def load_and_clean_data(filepath):
    """
    Load IPL match data and perform initial cleaning.

    Parameters:
    -----------
    filepath : str
        Path to the CSV file

    Returns:
    --------
    pd.DataFrame
        Cleaned dataframe
    """
    df = pd.read_csv(filepath)

    # Handle missing values
    print("=" * 70)
    print("DATA QUALITY CHECK")
    print("=" * 70)
    print(f"Dataset shape: {df.shape}")
    print(f"\nMissing values:\n{df.isnull().sum()}")

    # Remove rows with missing values if any
    df = df.dropna()

    return df

# ============================================================================
# 1. MOST SUCCESSFUL TEAMS ANALYSIS
# ============================================================================

def analyze_successful_teams(df):
    """
    Identify the most successful IPL teams based on total wins.

    Parameters:
    -----------
    df : pd.DataFrame
        Match data

    Returns:
    --------
    tuple
        (team_wins_series, team_stats_df)
    """
    # Count wins for each team
    team_wins = df['match_winner'].value_counts()

    # Calculate total matches for each team
    team_matches = pd.concat([df['team1'], df['team2']]).value_counts()

    # Create comprehensive statistics
    team_stats = pd.DataFrame({
        'Wins': team_wins,
        'Total_Matches': team_matches
    }).fillna(0)

    team_stats['Win_Percentage'] = (team_stats['Wins'] / team_stats['Total_Matches'] * 100).round(2)
    team_stats = team_stats.sort_values('Wins', ascending=False)

    return team_wins, team_stats

def print_team_success(team_stats):
    """Print top 5 successful teams in professional format."""
    print("\n" + "=" * 70)
    print("TOP 5 MOST SUCCESSFUL IPL TEAMS")
    print("=" * 70)
    print(f"{'Rank':<6}{'Team':<8}{'Wins':<8}{'Matches':<10}{'Win %':<10}")
    print("-" * 70)

    for rank, (team, row) in enumerate(team_stats.head(5).iterrows(), 1):
        print(f"{rank:<6}{team:<8}{int(row['Wins']):<8}{int(row['Total_Matches']):<10}{row['Win_Percentage']:.1f}%")

def visualize_successful_teams(team_stats):
    """Create bar chart for top 5 teams."""
    fig, ax = plt.subplots(figsize=(10, 6))

    top_5_teams = team_stats.head(5)
    colors = [TEAM_COLORS.get(team, '#3498db') for team in top_5_teams.index]

    bars = ax.bar(range(len(top_5_teams)), top_5_teams['Wins'],
                   color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)

    # Add value labels on bars
    for i, (bar, value) in enumerate(zip(bars, top_5_teams['Wins'])):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                f'{int(value)}', ha='center', va='bottom', fontweight='bold', fontsize=11)

    ax.set_xlabel('Teams', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Wins', fontsize=12, fontweight='bold')
    ax.set_title('Top 5 Most Successful IPL Teams (By Wins)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(range(len(top_5_teams)))
    ax.set_xticklabels(top_5_teams.index, fontsize=11, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    ax.set_ylim(0, top_5_teams['Wins'].max() * 1.15)

    plt.tight_layout()
    plt.savefig('outputs/01_successful_teams.png', dpi=300, bbox_inches='tight')
    plt.show()

    return fig

# ============================================================================
# 2. TOSS IMPACT ANALYSIS
# ============================================================================

def analyze_toss_impact(df):
    """
    Analyze the impact of toss on match outcomes.

    Parameters:
    -----------
    df : pd.DataFrame
        Match data

    Returns:
    --------
    tuple
        (toss_impact_df, toss_win_rate)
    """
    # Determine if toss winner won the match
    df['toss_winner_won_match'] = df['toss_winner'] == df['match_winner']

    # Calculate statistics
    toss_wins = df['toss_winner_won_match'].sum()
    total_matches = len(df)
    toss_win_rate = (toss_wins / total_matches) * 100

    # Create summary statistics
    toss_impact = pd.DataFrame({
        'Outcome': ['Toss Winner Won Match', 'Toss Winner Lost Match'],
        'Count': [toss_wins, total_matches - toss_wins],
        'Percentage': [toss_win_rate, 100 - toss_win_rate]
    })

    return df, toss_impact, toss_win_rate

def print_toss_impact(toss_impact, toss_win_rate):
    """Print toss impact analysis in professional format."""
    print("\n" + "=" * 70)
    print("TOSS IMPACT ANALYSIS")
    print("=" * 70)
    print(f"\nToss Winner Won Match: {int(toss_impact.iloc[0]['Count'])} times ({toss_win_rate:.2f}%)")
    print(f"Toss Winner Lost Match: {int(toss_impact.iloc[1]['Count'])} times ({toss_impact.iloc[1]['Percentage']:.2f}%)")
    print(f"\nKey Finding: Toss winners have a {toss_win_rate:.2f}% win rate")

def visualize_toss_impact(toss_impact):
    """Create visualizations for toss impact."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Pie Chart
    colors_pie = TOSS_COLORS
    explode = (0.05, 0)
    wedges, texts, autotexts = ax1.pie(
        toss_impact['Count'],
        labels=toss_impact['Outcome'],
        autopct='%1.1f%%',
        colors=colors_pie,
        explode=explode,
        startangle=90,
        textprops={'fontsize': 11, 'fontweight': 'bold'},
        wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}
    )

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(12)
        autotext.set_fontweight('bold')

    ax1.set_title('Toss Impact on Match Outcome', fontsize=13, fontweight='bold', pad=15)

    # Bar Chart
    bars = ax2.bar(toss_impact['Outcome'], toss_impact['Count'],
                    color=colors_pie, edgecolor='black', linewidth=1.5, alpha=0.8)

    for bar, value in zip(bars, toss_impact['Count']):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{int(value)}', ha='center', va='bottom', fontweight='bold', fontsize=11)

    ax2.set_ylabel('Number of Matches', fontsize=11, fontweight='bold')
    ax2.set_title('Toss Impact: Count Distribution', fontsize=13, fontweight='bold', pad=15)
    ax2.set_xticklabels(toss_impact['Outcome'], rotation=15, ha='right')
    ax2.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig('outputs/02_toss_impact.png', dpi=300, bbox_inches='tight')
    plt.show()

    return fig

# ============================================================================
# 3. VENUE PERFORMANCE ANALYSIS
# ============================================================================

def analyze_venue_performance(df):
    """
    Analyze team performance across different venues.

    Parameters:
    -----------
    df : pd.DataFrame
        Match data

    Returns:
    --------
    pd.DataFrame
        Venue statistics
    """
    # Count matches per venue
    venue_matches = df['venue'].value_counts()

    # For each venue, calculate batting first vs chasing success
    venue_stats = []

    for venue in df['venue'].unique():
        venue_data = df[df['venue'] == venue]
        total_matches = len(venue_data)

        # Determine if team1 batted first (toss winner choosing to bat first)
        # and if they won
        team1_wins_at_venue = len(venue_data[venue_data['match_winner'] == venue_data['team1']])

        venue_stats.append({
            'Venue': venue,
            'Total_Matches': total_matches,
            'Unique_Winners': venue_data['match_winner'].nunique()
        })

    venue_df = pd.DataFrame(venue_stats).sort_values('Total_Matches', ascending=False)
    return venue_df

def print_venue_analysis(venue_df):
    """Print venue performance analysis."""
    print("\n" + "=" * 70)
    print("VENUE PERFORMANCE ANALYSIS")
    print("=" * 70)
    print(f"{'Venue':<20}{'Matches':<12}{'Unique Winners':<15}")
    print("-" * 70)

    for _, row in venue_df.iterrows():
        print(f"{row['Venue']:<20}{int(row['Total_Matches']):<12}{int(row['Unique_Winners']):<15}")

    print(f"\nMost Played Venue: {venue_df.iloc[0]['Venue']} ({int(venue_df.iloc[0]['Total_Matches'])} matches)")

def visualize_venue_performance(venue_df):
    """Create visualization for venue performance."""
    fig, ax = plt.subplots(figsize=(10, 6))

    colors = sns.color_palette("husl", len(venue_df))
    bars = ax.barh(range(len(venue_df)), venue_df['Total_Matches'],
                    color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)

    # Add value labels
    for bar, value in zip(bars, venue_df['Total_Matches']):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
                f'{int(value)}', va='center', fontweight='bold', fontsize=10)

    ax.set_yticks(range(len(venue_df)))
    ax.set_yticklabels(venue_df['Venue'], fontsize=11, fontweight='bold')
    ax.set_xlabel('Number of Matches', fontsize=12, fontweight='bold')
    ax.set_title('IPL Matches by Venue', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3)
    ax.set_xlim(0, venue_df['Total_Matches'].max() * 1.15)

    plt.tight_layout()
    plt.savefig('outputs/03_venue_performance.png', dpi=300, bbox_inches='tight')
    plt.show()

    return fig

# ============================================================================
# 4. STRATEGIC INSIGHTS
# ============================================================================

def generate_strategic_insights(team_stats, toss_impact, toss_win_rate, venue_df):
    """Generate strategic insights from the analysis."""
    insights = []

    # Insight 1: Top Team Strategy
    top_team = team_stats.index[0]
    top_team_winrate = team_stats.iloc[0]['Win_Percentage']
    insights.append(
        f"{top_team} is the most successful team with {int(team_stats.iloc[0]['Wins'])} "
        f"wins and a {top_team_winrate:.1f}% win rate. Their consistent performance "
        f"suggests strong team composition and strategy execution."
    )

    # Insight 2: Toss Impact
    if toss_win_rate > 50:
        insights.append(
            f"Toss Impact: Teams winning the toss have a {toss_win_rate:.2f}% advantage in winning matches. "
            f"This suggests that choosing to bat or field wisely has a significant impact on match outcomes. "
            f"Teams should develop data-driven toss strategies based on venue and match conditions."
        )
    else:
        insights.append(
            f"Toss Impact: Interestingly, toss winners only have {toss_win_rate:.2f}% win rate. "
            f"This suggests that factors beyond toss decision (team strength, form, strategy) play a more crucial role."
        )

    # Insight 3: Venue Dominance
    top_venue = venue_df.iloc[0]['Venue']
    top_venue_matches = venue_df.iloc[0]['Total_Matches']
    insights.append(
        f"Venue Analysis: {top_venue} hosts the most IPL matches ({int(top_venue_matches)}) "
        f"with high competition. Teams playing at familiar venues often have home advantage. "
        f"Performance consistency across venues is a mark of elite teams."
    )

    return insights

def print_strategic_insights(insights):
    """Print strategic insights in a formatted way."""
    print("\n" + "=" * 70)
    print("STRATEGIC INSIGHTS & RECOMMENDATIONS")
    print("=" * 70)

    for i, insight in enumerate(insights, 1):
        print(f"\n{i}. {insight}")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""

    # Load and clean data
    print("\n" + "LOADING DATA..." + "\n")
    filepath = Path('data/ipl_matches_100.csv')

    if not filepath.exists():
        print(f"Error: {filepath} not found!")
        return

    df = load_and_clean_data(filepath)
    print(f"Data loaded successfully: {df.shape[0]} matches")

    # ========== Analysis 1: Successful Teams ==========
    print("\nANALYZING SUCCESSFUL TEAMS...\n")
    team_wins, team_stats = analyze_successful_teams(df)
    print_team_success(team_stats)
    print("\nGenerating visualization...\n")
    visualize_successful_teams(team_stats)

    # ========== Analysis 2: Toss Impact ==========
    print("\nANALYZING TOSS IMPACT...\n")
    df, toss_impact, toss_win_rate = analyze_toss_impact(df)
    print_toss_impact(toss_impact, toss_win_rate)
    print("\nGenerating visualizations...\n")
    visualize_toss_impact(toss_impact)

    # ========== Analysis 3: Venue Performance ==========
    print("\nANALYZING VENUE PERFORMANCE...\n")
    venue_df = analyze_venue_performance(df)
    print_venue_analysis(venue_df)
    print("\nGenerating visualization...\n")
    visualize_venue_performance(venue_df)

    # ========== Strategic Insights ==========
    print("\nGENERATING STRATEGIC INSIGHTS...\n")
    insights = generate_strategic_insights(team_stats, toss_impact, toss_win_rate, venue_df)
    print_strategic_insights(insights)

    # ========== Summary ==========
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
    print("\nAll visualizations saved:")
    print("   - outputs/01_successful_teams.png")
    print("   - outputs/02_toss_impact.png")
    print("   - outputs/03_venue_performance.png")
    print("\n" + "=" * 70 + "\n")

if __name__ == "__main__":
    main()
