# IPL Cricket Data Dictionary

## Dataset: ipl_matches_100.csv

### Field Definitions

| Field Name | Data Type | Description | Example | Notes |
|-----------|-----------|-------------|---------|-------|
| match_id | Integer | Unique identifier for each match | 1, 2, 3... | Primary key, sequential |
| team1 | String | First team in the match | MI, CSK, RCB | Team abbreviation |
| team2 | String | Second team in the match | SRH, DC, KKR | Team abbreviation |
| toss_winner | String | Team that won the coin toss | RCB, CSK, MI | One of the playing teams |
| match_winner | String | Team that won the match | MI, KKR, DC | One of the playing teams |
| venue | String | City/Stadium where match was played | Bangalore, Mumbai, Delhi | Geographic location |
| season | Integer | Year/Season of the match | 2021, 2022, 2023 | IPL season year |

---

## Team Abbreviations

| Abbreviation | Full Team Name | City | Established |
|--------------|----------------|------|-------------|
| MI | Mumbai Indians | Mumbai | 2008 |
| CSK | Chennai Super Kings | Chennai | 2008 |
| RCB | Royal Challengers Bangalore | Bangalore | 2008 |
| KKR | Kolkata Knight Riders | Kolkata | 2008 |
| DC | Delhi Capitals | Delhi | 2008 |
| SRH | Sunrisers Hyderabad | Hyderabad | 2013 |

---

## Venue Reference

### Cricket Stadiums in Dataset

| Venue | City | Capacity | Surface | Notes |
|-------|------|----------|---------|-------|
| Bangalore | Bangalore | 55,000 | Hard court | M. Chinnaswamy Stadium |
| Mumbai | Mumbai | 33,000 | Hard court | Wankhede Stadium |
| Delhi | Delhi | 41,810 | Hard court | Feroz Shah Kotla |
| Hyderabad | Hyderabad | 39,000 | Hard court | Rajiv Gandhi Oval |
| Kolkata | Kolkata | 68,000 | Hard court | Eden Gardens |
| Chennai | Chennai | 38,000 | Hard court | MA Chidambaram Stadium |

---

## Data Quality Specifications

### Missing Values Policy
- **Handling**: Drop rows with ANY missing values
- **Expected**: Minimal missing data in this dataset
- **Check**: Display missing value count during data loading

### Data Validation Rules

1. **match_id**:
   - Must be unique
   - Must be positive integer
   - Range: 1 to 100

2. **Teams (team1, team2)**:
   - Must be valid IPL team code
   - Allowed values: MI, CSK, RCB, KKR, DC, SRH
   - team1 ≠ team2 (different teams)

3. **toss_winner**:
   - Must be either team1 or team2
   - Valid values: MI, CSK, RCB, KKR, DC, SRH

4. **match_winner**:
   - Must be either team1 or team2
   - Valid values: MI, CSK, RCB, KKR, DC, SRH
   - Generally ≠ toss_winner (but not always)

5. **venue**:
   - Allowed values: Mumbai, Delhi, Bangalore, Hyderabad, Kolkata, Chennai
   - Case-sensitive in current dataset

6. **season**:
   - Must be 4-digit year
   - Realistic range: 2008-2024
   - In this dataset: 2018-2023 expected

---

## Data Collection Methodology

### Source:
- Historical IPL match records
- Official IPL statistics

### Sample Size:
- **100 matches** (representative sample)
- Multiple seasons represented
- All major venues included

### Data Period:
- Spans multiple IPL seasons
- Recent seasons (2021-2023)
- Mix of regular season matches

---

## Calculated Fields (Generated During Analysis)

### During Analysis:

1. **toss_winner_won_match** (Boolean)
   - Derived: toss_winner == match_winner
   - Purpose: Toss impact analysis

2. **Win_Count** (Integer)
   - By: match_winner groupby
   - Purpose: Total wins per team

3. **Win_Percentage** (Float)
   - Calculation: (Wins / Total_Matches) * 100
   - Purpose: Normalized team performance

4. **Total_Matches** (Integer)
   - By: Concatenate team1 & team2, value_counts
   - Purpose: Participation metric

---

## Data Limitations & Assumptions

### Limitations:
1. **Sample Size**: 100 matches is relatively small
2. **Time Period**: Limited to specific seasons
3. **No Player Data**: Team-level analysis only
4. **No Performance Metrics**: Only wins/losses tracked

### Assumptions:
1. All matches are formal IPL matches
2. Teams always have 2 options (team1, team2)
3. There are no incomplete/cancelled matches
4. Data is accurate and up-to-date
5. Venue names are standardized

---

## Statistical Properties

### Team Distribution:
- 6 major teams in dataset
- Approximately equal representation across seasons
- Different participation levels possible

### Toss Statistical Properties:
- Binary outcome (toss_winner_won_match: True/False)
- Expected distribution: ~50-50 if toss independent
- Actual distribution: To be determined by analysis

### Venue Distribution:
- Multiple venues across India
- Geographic spread indicates national tournament
- Potential home advantage effects

---

## Analysis Specifications

### Grouping Levels:
1. **Team-level**: By match_winner or team1/team2
2. **Venue-level**: By venue name
3. **Season-level**: By year
4. **Toss-level**: By toss_winner vs match_winner

### Aggregation Methods:
1. **Count**: Match frequency
2. **Sum**: Total wins
3. **Percentage**: Success rates
4. **Unique**: Winner count per venue

---

## Output Data Format

### CSV Output Columns:
- Team, Wins, Total_Matches, Win_Percentage
- Venue, Total_Matches, Unique_Winners
- Outcome, Count, Percentage

### Chart Data:
- Categorical (Team names, Venue names)
- Numerical (Win counts, Percentages)
- Boolean (Toss impact analysis)

---

## Data Access & Privacy

### Availability:
- Public domain IPL data
- No sensitive information
- Educational use authorized

### Usage Rights:
- Free for educational projects
- Proper attribution recommended
- Commercial use may require IPL permission

---

## Notes for Future Enhancement

1. **Add**: Runs scored, wickets, match duration
2. **Add**: Player names and individual performance
3. **Add**: Toss decision preference (bat/field)
4. **Add**: Weather data, pitch conditions
5. **Link**: External data for context enrichment
