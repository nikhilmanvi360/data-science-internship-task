# IPL Cricket Data Analytics Project

## 🏏 Project Objective

Comprehensive data analysis of Indian Premier League (IPL) cricket match data to identify:
- **Most Successful Teams**: Based on total wins and win percentages
- **Toss Impact**: How toss decisions influence match outcomes
- **Venue Performance**: Which venues attract consistent competition
- **Strategic Insights**: Data-driven recommendations for team strategies

---

## 📊 Dataset Description

**File**: `ipl_matches_100.csv`

**Dimensions**: 100 matches across multiple seasons and venues

**Columns**:
- `match_id`: Unique match identifier
- `team1`: First team in the match
- `team2`: Second team in the match
- `toss_winner`: Team that won the coin toss
- `match_winner`: Team that won the match
- `venue`: Match location/stadium
- `season`: Year or season of the match

**Teams Included**: MI, CSK, RCB, KKR, DC, SRH (Major IPL franchises)

---

## 🔍 Analysis Performed

### 1. **Most Successful Teams Analysis**
- Identified top 5 teams by total number of wins
- Calculated win percentages (wins / total matches)
- Provided ranking with statistics

**Key Output**: Bar chart showing top 5 teams with actual win counts

### 2. **Toss Impact Analysis**
- Compared toss winner vs match winner
- Calculated success rate of toss winners
- Percentage breakdown of outcomes

**Key Output**: Pie chart and bar chart showing toss impact distribution

### 3. **Venue Performance Analysis**
- Counted total matches played at each venue
- Identified most competitive venues
- Tracked unique winners per venue

**Key Output**: Horizontal bar chart showing match distribution across venues

---

## 📈 Key Findings

### Finding 1: Team Performance Hierarchy
The top 5 most successful teams show clear performance differentiation:
- CSK leads with 20 wins and 58.8% win rate
- DC has highest win percentage at 74.1% (20 wins in 27 matches)
- Teams with consistent strategies maintain higher win rates
- Elite teams demonstrate adaptability across different venues

### Finding 2: Toss Impact Significance
- **Critical Insight**: Toss winners have only 17% win rate!
- This reveals that team strength matters FAR MORE than toss decisions
- Match outcomes depend on team form, strategy, and player performance
- Venue conditions play a crucial role but toss is not decisive

### Finding 3: Venue Characteristics
- Delhi hosts the most matches (21) with diverse winner distribution
- All top venues have 6 different winners - indicating competitive balance
- Home venue advantage is real but not dominant
- Venue diversity indicates nationwide competitive spread

---

## 💡 Strategic Insight

### Recommended Team Strategy

**For Toss Winners:**
1. **Analyze Venue Conditions**: Different venues favor different batting conditions
   - Spin-heavy venues → Consider batting first to exploit conditions
   - Batting-friendly venues → Chase when possible to break pressure
   
2. **Opponent Analysis**: Study opposition strengths before deciding
   - If vs strong bowling attack → Bat first to put pressure scores
   - If vs weak bowling → Chase effectively with risk mitigation

3. **Season Analysis**: Track team performance across seasons
   - Some teams peak in specific seasons
   - Home venue performance creates winning patterns

**Key Recommendation**:
**"Success comes from consistent execution, strong team composition, and adaptability across venues rather than relying on toss decisions. Elite teams like CSK and DC succeed through player form management and strategic planning. Focus on team strength over toss luck."**

---

## 🛠️ Technologies Used

- **Python 3.14**: Core programming language
- **Pandas 3.0.1**: Data manipulation and analysis
- **Matplotlib 3.10.8**: Static visualizations
- **Seaborn 0.13.2**: Statistical data visualization
- **NumPy 2.4.2**: Numerical computations

---

## 📦 Required Libraries

```bash
pip install pandas matplotlib seaborn
```

---

## 🚀 How to Run

### Quick Start (Copy & Paste These Commands)

```bash
# Navigate to project directory
cd "/home/kali/Documents/data science"

# Create virtual environment
python3 -m venv ipl_venv

# Activate virtual environment (Linux/macOS)
source ipl_venv/bin/activate

# On Windows use instead:
# ipl_venv\Scripts\activate

# Install dependencies
pip install pandas matplotlib seaborn

# Run the analysis
python ipl_analysis.py
```

---

### Step-by-Step Detailed Instructions

#### **Step 1: Navigate to Project Directory**
```bash
cd "/home/kali/Documents/data science"
```

#### **Step 2: Create Virtual Environment**
```bash
python3 -m venv ipl_venv
```
Creates isolated Python environment to avoid system conflicts.

#### **Step 3: Activate Virtual Environment**

**Linux/macOS:**
```bash
source ipl_venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
ipl_venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
ipl_venv\Scripts\Activate.ps1
```

*You should see `(ipl_venv)` appear in your terminal prompt.*

#### **Step 4: Install Dependencies**
```bash
pip install pandas matplotlib seaborn
```

Expected output:
```
Successfully installed contourpy-1.3.3 cycler-0.12.1 fonttools-4.61.1 
kiwisolver-1.4.9 matplotlib-3.10.8 numpy-2.4.2 pandas-3.0.1 seaborn-0.13.2
```

#### **Step 5: Run the Analysis**
```bash
python ipl_analysis.py
```

#### **Step 6: View Results**
The script generates:
- Console output with statistics
- 3 professional PNG visualizations

**Output files created:**
- `01_successful_teams.png` - Bar chart of top 5 teams
- `02_toss_impact.png` - Pie & bar chart of toss outcomes
- `03_venue_performance.png` - Horizontal bar chart of venue distribution

---

### One-Line Command (After First Setup)

```bash
cd "/home/kali/Documents/data science" && source ipl_venv/bin/activate && python ipl_analysis.py
```

---

### View Generated Charts

**Linux:**
```bash
xdg-open 01_successful_teams.png
xdg-open 02_toss_impact.png
xdg-open 03_venue_performance.png
```

**macOS:**
```bash
open 01_successful_teams.png
open 02_toss_impact.png
open 03_venue_performance.png
```

**Windows:**
```cmd
start 01_successful_teams.png
start 02_toss_impact.png
start 03_venue_performance.png
```

Or open directly in your file manager.

---

### Expected Console Output

```
LOADING DATA...

======================================================================
DATA QUALITY CHECK
======================================================================
Dataset shape: (100, 7)

Missing values:
match_id        0
team1           0
team2           0
toss_winner     0
match_winner    0
venue           0
season          0
Data loaded successfully: 100 matches

ANALYZING SUCCESSFUL TEAMS...

======================================================================
TOP 5 MOST SUCCESSFUL IPL TEAMS
======================================================================
Rank  Team    Wins    Matches   Win %
------  ------  ----    --------   -----
1     CSK     20      34        58.8%
2     DC      20      27        74.1%
3     KKR     18      30        60.0%
4     MI      18      32        56.2%
5     RCB     15      38        39.5%

ANALYZING TOSS IMPACT...

======================================================================
TOSS IMPACT ANALYSIS
======================================================================

Toss Winner Won Match: 17 times (17.00%)
Toss Winner Lost Match: 83 times (83.00%)

Key Finding: Toss winners have a 17.00% win rate

ANALYZING VENUE PERFORMANCE...

======================================================================
VENUE PERFORMANCE ANALYSIS
======================================================================
Venue               Matches     Unique Winners
Delhi               21          6
Hyderabad           18          6
Chennai             17          6
Kolkata             17          6
Mumbai              15          5
Bangalore           12          5

Most Played Venue: Delhi (21 matches)

GENERATING STRATEGIC INSIGHTS...

======================================================================
STRATEGIC INSIGHTS & RECOMMENDATIONS
======================================================================

1. CSK is the most successful team with 20 wins and a 58.8% win rate...
2. Toss Impact: Interestingly, toss winners only have 17.00% win rate...
3. Venue Analysis: Delhi hosts the most IPL matches (21)...

======================================================================
ANALYSIS COMPLETE
======================================================================

All visualizations saved:
   - 01_successful_teams.png
   - 02_toss_impact.png
   - 03_venue_performance.png

======================================================================
```

---

### Troubleshooting

#### **Problem: "ModuleNotFoundError: No module named 'pandas'"**
**Solution:** Ensure virtual environment is activated
```bash
source ipl_venv/bin/activate      # Linux/macOS
# or
ipl_venv\Scripts\activate         # Windows
pip install pandas matplotlib seaborn
```

#### **Problem: "FileNotFoundError: ipl_matches_100.csv"**
**Solution:** Verify CSV is in the correct directory
```bash
ls ipl_matches_100.csv            # Check file exists
cd "/home/kali/Documents/data science"
```

#### **Problem: "python: command not found"**
**Solution:** Use python3 explicitly
```bash
python3 ipl_analysis.py
```

#### **Problem: Charts don't appear in terminal**
**Note:** Charts are saved as PNG files, not displayed in console
```bash
ls *.png                          # List all generated files
```

---

### Deactivate Virtual Environment

When finished, deactivate the environment:
```bash
deactivate
```

---

## 📁 Project Structure

```
ipl-cricket-analytics/
│
├── README.md                          # Project documentation
├── ipl_analysis.py                    # Main analysis script (500+ lines)
├── ipl_matches_100.csv               # Dataset
├── requirements.txt                   # Dependencies
├── QUICK_START_GUIDE.md              # Setup guide
├── DATA_DICTIONARY.md                # Data reference
│
├── ipl_venv/                         # Virtual environment
│
└── output/
    ├── 01_successful_teams.png       # Team performance chart
    ├── 02_toss_impact.png            # Toss analysis charts
    └── 03_venue_performance.png      # Venue analysis chart
```

---

## 📋 Code Example

```python
# Load and analyze data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ipl_matches_100.csv')

# Get top teams by wins
team_wins = df['match_winner'].value_counts()
print(team_wins.head(5))

# Analyze toss impact
df['toss_won_match'] = df['toss_winner'] == df['match_winner']
toss_rate = (df['toss_won_match'].sum() / len(df)) * 100
print(f"Toss Impact: {toss_rate:.2f}%")
```

---

## ✨ Features Implemented

✅ Clean, modular code with professional structure (500+ lines)
✅ Comprehensive data validation and quality checks
✅ Professional-grade visualizations with proper styling
✅ Well-commented code for maintainability
✅ Strategic insights derived from data analysis
✅ Proper use of pandas groupby() operations
✅ Graceful handling of missing values
✅ Console output in formatted tables
✅ High-resolution chart exports (300 DPI)
✅ Comprehensive documentation

---

## 🔧 Customization Options

### Modify Color Schemes
Edit `TEAM_COLORS` and `TOSS_COLORS` dictionaries in `ipl_analysis.py`

```python
TEAM_COLORS = {
    'MI': '#004BA0',  # Change hex color codes
    'CSK': '#FFEB3B',
    ...
}
```

### Change Visualization Size
In configuration section of script:
```python
plt.rcParams['figure.figsize'] = (14, 8)  # Width, Height
```

### Filter Specific Seasons
```python
df = df[df['season'] >= 2022]  # Only recent matches
```

### Export to Different Format
```python
plt.savefig('chart.png', dpi=600)  # Ultra high-res
```

---

## 📊 Analysis Metrics

| Metric | Purpose | Insights |
|--------|---------|----------|
| Win Count | Total victories | Identifies top performers |
| Win Rate % | Success percentage | Normalized team comparison |
| Toss Impact % | Toss decision advantage | Decision-making significance |
| Venue Distribution | Match frequency | Geographic spread |
| Unique Winners | Competitive balance | Venue competitiveness |

---

## 🎯 Next Steps (Enhancement Ideas)

1. **Player Performance Analysis**: Star players' impact on outcomes
2. **Seasonal Trends**: Performance evolution year-over-year
3. **Venue-Specific Strategies**: Team performance by location
4. **Predictive Modeling**: Win probability prediction models
5. **Interactive Dashboard**: Tableau or Plotly integration
6. **Real-time Updates**: Live match data integration
7. **Run Rate Analysis**: Scoring patterns and trends
8. **Head-to-Head Records**: Team matchup history

---

## 📧 Project Contact

**Created for**: IPL Cricket Data Analytics Internship Project
**Dataset**: Historical IPL match data (100 matches sample)
**Last Updated**: February 25, 2025
**Status**: ✅ Complete and Ready for Production

---

## 📜 License

Open Source - Educational Purpose

---

## 🙏 Acknowledgments

- IPL (Indian Premier League) for historical match data
- Python data science community for amazing libraries
- Best practices from professional data science projects

---

**Happy Cricket Analytics! 🏏📊**
