# Dr. Semmelweis and the Handwashing Discovery

A fascinating data analysis notebook recreating Dr. Ignaz Semmelweis's 1847 discovery that handwashing dramatically reduces childbed fever mortality. This project uses historical hospital data to understand one of medicine's most important breakthroughs.

## Features

- **Historical Data Analysis**: Work with real 1840s hospital mortality records
- **Statistical Significance**: Calculate and visualize dramatic mortality changes
- **Time Series Analysis**: Track death rates before and after handwashing policy
- **Multiple Visualizations**: Line charts, bar charts, and statistical plots
- **Scientific Method**: Follow data-driven discovery process
- **Comparative Analysis**: Compare two clinics with different practices
- **Data Storytelling**: Present compelling evidence for intervention effectiveness

## Historical Context

### Dr. Ignaz Semmelweis (1818-1865)
- Hungarian physician at Vienna General Hospital
- Noticed mysteriously high mortality in maternity wards
- Discovered connection between autopsies and childbed fever
- Introduced handwashing with chlorinated lime solution
- Results were dramatic but initially rejected by medical establishment

### The Problem
- Women died from childbed fever (puerperal fever) after delivery
- One clinic had much higher death rates than another
- Cause was unknown - theories included "bad air" and "evil spirits"
- Medical students went directly from autopsies to deliveries

### The Discovery
- **Observation**: Clinic 1 (medical students) had 10% mortality vs Clinic 2 (midwives) with 4%
- **Hypothesis**: Something on doctors' hands transferred disease
- **Intervention**: Mandatory handwashing with chlorinated lime (1847)
- **Result**: Mortality dropped from 10% to under 2%

## How to Use

1. Install required dependencies:
   ```bash
   pip install jupyter pandas numpy matplotlib seaborn plotly scipy
   ```

2. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. Open `Dr_Semmelweis_Handwashing_Discovery_(start).ipynb`

4. Run cells to recreate the historical analysis

5. Explore the data and visualizations

## Dataset Information

### Files Included
- **`annual_deaths_by_clinic.csv`**: Yearly data for both clinics
- **`monthly_deaths.csv`**: Monthly mortality rates before/after handwashing

### Data Columns

**Annual Data**:
- `year`: Year of record
- `births`: Number of deliveries
- `deaths`: Number of deaths from childbed fever
- `clinic`: Which clinic (Clinic 1 or Clinic 2)

**Monthly Data**:
- `date`: Month and year
- `births`: Number of deliveries that month
- `deaths`: Number of maternal deaths
- `proportion_deaths`: Death rate (deaths/births)

### Time Periods
- **Before Handwashing**: 1841-1847 (June)
- **Handwashing Introduced**: June 1847
- **After Handwashing**: 1847 (June) - 1849

## Analysis Performed

### Exploratory Analysis
1. Load and examine both datasets
2. Calculate death rates (proportion)
3. Compare two clinics
4. Identify time trends
5. Find anomalies and patterns

### Statistical Analysis
1. Calculate mean death rates before/after
2. Measure percentage decrease
3. Test statistical significance
4. Analyze month-by-month changes
5. Identify confidence intervals

### Visualizations Created
- **Time Series**: Death rates over time
- **Comparison Charts**: Clinic 1 vs Clinic 2
- **Before/After**: Impact of handwashing intervention
- **Statistical Plots**: Distribution of death rates
- **Annotated Charts**: Mark handwashing introduction

## Technical Details

### Libraries Used
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Static plotting
- **Matplotlib.dates**: Date axis formatting
- **Seaborn**: Statistical visualizations
- **Plotly Express**: Interactive charts
- **SciPy.stats**: Statistical testing

### Statistical Methods

**Descriptive Statistics**:
- Mean death rate
- Median death rate
- Standard deviation
- Minimum and maximum

**Comparative Analysis**:
- Before vs after comparison
- Percentage change
- Absolute reduction
- Relative risk reduction

**Statistical Testing** (if performed):
- T-tests for significance
- Confidence intervals
- P-values
- Effect size

### Visualization Techniques
- Line charts with annotations
- Multiple y-axes for different scales
- Date formatting on x-axis
- Color coding for different periods
- Highlighting significant events
- Professional styling

## File Structure

```
Day 80/
├── Dr_Semmelweis_Handwashing_Discovery_(start).ipynb
├── annual_deaths_by_clinic.csv
└── monthly_deaths.csv
```

## Learning Concepts

### Data Analysis
- Working with historical data
- Time series manipulation
- Calculating rates and proportions
- Comparing groups
- Identifying trends

### Statistical Thinking
- Hypothesis testing with data
- Evidence-based conclusions
- Statistical significance
- Confounding factors
- Causation vs correlation

### Data Visualization
- Effective storytelling with data
- Annotating charts for clarity
- Choosing appropriate chart types
- Date formatting on axes
- Making data accessible

### Scientific Method
- Observation and question formation
- Hypothesis development
- Testing through data collection
- Drawing evidence-based conclusions
- Importance of reproducibility

## Key Findings

### Before Handwashing (1841-1847)
- Clinic 1 mortality: ~10% (1 in 10 women died)
- Clinic 2 mortality: ~4% (1 in 25 women died)
- Dramatic difference between clinics unexplained

### After Handwashing (June 1847 onwards)
- Mortality dropped to under 2%
- 80%+ reduction in deaths
- Both clinics achieved similar low rates
- Sustained improvement over time

### Impact
- Thousands of lives saved
- Proof of germ theory before germs discovered
- Foundation for modern infection control
- Evidence-based medicine demonstrated

## Requirements

- Python 3.x
- Jupyter Notebook
- pandas (data manipulation)
- numpy (numerical operations)
- matplotlib (visualization)
- seaborn (statistical plots)
- plotly (interactive charts)
- scipy (statistical tests)

## Environment Setup

### Windows (PowerShell):
```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install jupyter pandas numpy matplotlib seaborn plotly scipy
jupyter notebook
```

### macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install jupyter pandas numpy matplotlib seaborn plotly scipy
jupyter notebook
```

## How the Code Works

1. **Data Loading**: Read historical CSV files
2. **Exploration**: Examine structure and contents
3. **Calculation**: Compute death rates and proportions
4. **Comparison**: Analyze clinic differences
5. **Visualization**: Create time series showing mortality trends
6. **Intervention Analysis**: Identify change point (June 1847)
7. **Impact Measurement**: Calculate before/after statistics
8. **Conclusion**: Present evidence for handwashing effectiveness

## Real-World Lessons

### Medical History
- Importance of data-driven medicine
- Resistance to new ideas
- How scientific discoveries happen
- Evolution of hygiene practices

### Statistical Thinking
- Power of data visualization
- Importance of comparison groups
- Natural experiments
- Evidence vs intuition

### Public Health
- Infection control basics
- Simple interventions save lives
- Importance of hygiene
- Evidence-based policy

## Modern Parallels

### COVID-19 Pandemic
- Hand hygiene recommendations
- Data-driven policy decisions
- Visualizing infection rates
- Measuring intervention effectiveness

### Healthcare Quality
- Hospital infection rates
- Quality improvement initiatives
- Evidence-based protocols
- Data transparency

## Next Steps/Improvements

- Add confidence intervals to estimates
- Perform formal statistical tests (t-tests)
- Calculate lives saved estimates
- Add interactive dashboards
- Compare with modern data
- Study seasonal patterns
- Analyze by cause of death
- Create animated visualizations
- Build predictive models
- Study adoption timelines

Perfect for learning data analysis, statistical thinking, time series visualization, and understanding how data can save lives and drive scientific discovery!
