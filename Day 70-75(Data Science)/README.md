# Data Science with Python - Pandas & Matplotlib

A collection of Jupyter notebooks covering essential data science skills including data cleaning, exploration, visualization, and analysis using Pandas and Matplotlib. These notebooks demonstrate real-world data analysis on various datasets.

## Projects Included

### Day 70: Programming Languages Popularity (StackOverflow Data)
- **File**: `Programming_Languages_(start).ipynb`
- **Dataset**: `QueryResults.csv` (StackOverflow tags over time)
- **Analysis**: Tracks popularity trends of programming languages from 2008-2024

### Day 72: College Salaries by Major
- **File**: `data(day 72).ipynb`
- **Dataset**: `salaries_by_college_major.csv`
- **Analysis**: Explores starting, mid-career, and percentile salaries by college major

### Day 75: Google Trends Data Visualization
- **Location**: `Google Trends Data Viz (Day 75)/` folder
- **File**: `Google Trends and Data Visualisation (start).ipynb`
- **Datasets**:
  - `Bitcoin Search Trend.csv` & `Daily Bitcoin Price.csv`
  - `TESLA Search Trend vs Price.csv`
  - `UE Benefits Search vs UE Rate 2004-19.csv`
  - `UE Benefits Search vs UE Rate 2004-20.csv`
- **Analysis**: Correlates Google search trends with real-world events and prices

### LEGO Dataset Analysis
- **Location**: `LEGO Notebook and Data (start)/` folder
- **File**: `Lego_Analysis_for_Course_(start).ipynb`
- **Dataset**: LEGO sets data with themes, pieces, and pricing
- **Analysis**: Explores LEGO product trends, themes, and set complexity

## Features

- **Data Cleaning**: Handle missing values, duplicates, and incorrect data types
- **Exploratory Analysis**: Use `.head()`, `.tail()`, `.shape`, `.info()`, `.describe()`
- **Data Transformation**: Sorting, filtering, and creating new columns
- **Grouping & Pivoting**: Excel-style pivot tables with `.groupby()`
- **Visualization**: Line charts, bar charts, scatter plots with Matplotlib
- **Statistical Analysis**: Mean, median, max, min, percentiles
- **Time Series**: Date handling and trend analysis
- **Correlation Analysis**: Finding relationships between variables

## How to Use

1. Install required dependencies:
   ```bash
   pip install jupyter pandas matplotlib
   ```

2. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. Open any notebook file (`.ipynb`)

4. Run cells sequentially from top to bottom (Shift + Enter)

5. Modify code and experiment with different analyses

## Data Exploration Techniques

### Basic DataFrame Operations
- **`df.head(n)`**: View first n rows
- **`df.tail(n)`**: View last n rows
- **`df.shape`**: Get dimensions (rows, columns)
- **`df.columns`**: List all column names
- **`df.info()`**: Data types and non-null counts
- **`df.describe()`**: Statistical summary of numeric columns

### Data Cleaning
- **`df.isna()`**: Find missing values
- **`df.dropna()`**: Remove rows with missing data
- **`df.fillna(value)`**: Replace missing values
- **`df.drop_duplicates()`**: Remove duplicate rows
- **`df.astype()`**: Convert column data types

### Data Selection & Filtering
- **`df['column']`**: Select single column
- **`df[['col1', 'col2']]`**: Select multiple columns
- **`df[df['col'] > value]`**: Filter rows by condition
- **`df.loc[index]`**: Access by label
- **`df.iloc[index]`**: Access by position

### Aggregation & Grouping
- **`df.groupby('column')`**: Group by values
- **`df['column'].sum()`**: Calculate sum
- **`df['column'].mean()`**: Calculate average
- **`df.max()` / `df.min()`**: Find extremes
- **`df.idxmax()` / `df.idxmin()`**: Find indices of extremes

## Technical Details

### Libraries Used
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Static plotting and visualization
- **NumPy**: Numerical operations (implicit with Pandas)

### Common Data Operations in These Notebooks

**Programming Languages Notebook**:
- Reading CSV with custom column names
- Grouping by tag and date
- Creating line charts for trends
- Multi-series plotting
- Date handling on x-axis

**Salaries Notebook**:
- Identifying and handling NaN values
- Sorting DataFrames
- Finding max/min values with `.idxmax()`/`.idxmin()`
- Creating new calculated columns
- Bar chart visualization

**Google Trends Notebook**:
- Multiple CSV file analysis
- Date parsing and formatting
- Matplotlib date formatting
- Correlation between search trends and real events
- Subplot creation for comparisons

**LEGO Analysis**:
- Data merging and joins
- Grouping by categories
- Calculating aggregates
- Trend analysis over time
- Bar charts and pie charts

## File Structure

```
Day 70-75(Data Science)/
├── Programming_Languages_(start).ipynb
├── QueryResults.csv
├── data(day 72).ipynb
├── salaries_by_college_major.csv
├── Google Trends Data Viz (Day 75)/
│   ├── Google Trends and Data Visualisation (start).ipynb
│   ├── Bitcoin Search Trend.csv
│   ├── Daily Bitcoin Price.csv
│   ├── TESLA Search Trend vs Price.csv
│   └── UE Benefits Search vs UE Rate 2004-19.csv
└── LEGO Notebook and Data (start)/
    ├── Lego_Analysis_for_Course_(start).ipynb
    ├── data/           # LEGO datasets
    └── assets/         # Images and resources
```

## Learning Concepts

### Data Science Fundamentals
- Loading data from CSV files
- Exploring dataset structure and contents
- Identifying data quality issues
- Cleaning and preparing data for analysis
- Asking questions of data

### Pandas Core Skills
- DataFrame creation and manipulation
- Column selection and filtering
- Row indexing and slicing
- Sorting and ranking
- Grouping and aggregation
- Pivot tables
- Merging and joining datasets

### Data Visualization
- Matplotlib basics (figure, axes, plots)
- Line charts for trends
- Bar charts for comparisons
- Customizing plots (titles, labels, legends)
- Multiple subplots
- Date formatting on axes
- Color and style customization

### Statistical Analysis
- Descriptive statistics
- Percentile calculations
- Trend identification
- Correlation analysis
- Distribution analysis

## Key Insights from Datasets

### Programming Languages
- Track rise and fall of language popularity
- Identify emerging technologies
- See impact of new language releases
- Understand community growth

### College Salaries
- Compare earning potential by major
- Identify highest-paying degrees
- Analyze salary growth over career
- Make informed education decisions

### Google Trends
- Correlate search interest with real-world events
- Predict market movements with search data
- Understand public interest patterns
- Identify seasonal trends

### LEGO Analysis
- Understand product line evolution
- Analyze pricing strategies
- Track theme popularity
- Study set complexity trends

## Requirements

- Python 3.x
- Jupyter Notebook or JupyterLab
- pandas (data manipulation)
- matplotlib (visualization)

## Environment Setup

### Windows (PowerShell):
```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install jupyter pandas matplotlib
jupyter notebook
```

### macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install jupyter pandas matplotlib
jupyter notebook
```

## Tips for Working with Notebooks

1. **Run Cells in Order**: Execute cells from top to bottom
2. **Save Frequently**: Use Ctrl+S or File → Save
3. **Restart Kernel**: If code behaves unexpectedly, restart kernel
4. **Check Variables**: Use `print()` to inspect data
5. **Read Errors**: Error messages point to problems
6. **Experiment**: Modify code to explore different analyses
7. **Comment Code**: Add notes to remember your thinking

## Common Pandas Patterns

```python
# Load data
df = pd.read_csv('filename.csv')

# Explore structure
df.head()
df.info()
df.describe()

# Clean data
df = df.dropna()  # Remove missing values
df = df.drop_duplicates()  # Remove duplicates

# Filter data
high_salary = df[df['salary'] > 100000]

# Group and aggregate
df.groupby('category')['value'].mean()

# Sort data
df.sort_values('column', ascending=False)

# Create visualizations
df.plot(x='date', y='value', kind='line')
plt.show()
```

## Next Steps/Improvements

- Add more advanced visualizations (seaborn)
- Implement statistical tests
- Create interactive plots (plotly)
- Add predictive modeling
- Automate data collection
- Build dashboards
- Export results to reports
- Add data validation checks
- Implement error handling
- Create reusable functions

Perfect for learning data science fundamentals, Pandas data manipulation, Matplotlib visualization, and practical data analysis skills!
