# Linear Regression and Data Visualization

A Jupyter notebook exploring the relationship between movie budgets and box office revenue using linear regression. This project demonstrates statistical analysis, data visualization, and predictive modeling using real movie financial data.

## Features

- **Data Cleaning**: Handle missing values and dirty data
- **Exploratory Analysis**: Understand dataset structure and distributions
- **Statistical Visualization**: Create scatter plots, regression lines, and residual plots
- **Linear Regression**: Build and evaluate a simple linear regression model
- **Residual Analysis**: Examine model fit and assumptions
- **Predictive Modeling**: Use the model to estimate revenue from budget
- **Correlation Analysis**: Measure relationship strength between variables

## How to Use

1. Install required dependencies:
   ```bash
   pip install jupyter pandas matplotlib
   ```

2. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. Open `Seaborn_and_Linear_Regression_(start).ipynb`

4. Run cells from top to bottom

5. Explore visualizations and modify code to experiment

## Dataset Information

### Source
- **File**: `cost_revenue_dirty.csv`
- **Source**: Scraped from the-numbers.com on May 1st, 2018
- **Content**: Movie budgets and financial performance data

### Columns
- **Movie Title**: Name of the film
- **Production Budget**: Money spent making the movie
- **Domestic Gross**: Box office revenue in the United States
- **Worldwide Gross**: Total global box office revenue
- **Release Date**: When the movie was released

### Research Question
**Do higher film budgets lead to more box office revenue?**

## Analysis Performed

### Data Cleaning Steps
1. Check for null values
2. Remove or impute missing data
3. Remove duplicate entries
4. Convert currency strings to numeric values
5. Handle outliers
6. Validate data types

### Exploratory Data Analysis
- Summary statistics (mean, median, min, max)
- Distribution of budgets
- Distribution of revenue
- Budget ranges by decade
- Revenue patterns over time
- Identify blockbusters and flops

### Visualization Techniques
- **Scatter Plots**: Budget vs Revenue relationship
- **Regression Lines**: Linear fit visualization
- **Residual Plots**: Model error distribution
- **Histograms**: Data distributions
- **Box Plots**: Outlier identification
- **Time Series**: Trends over years

### Linear Regression Analysis
- Fit linear model: `Revenue = β₀ + β₁ * Budget`
- Calculate correlation coefficient
- Determine R² (coefficient of determination)
- Analyze residuals
- Test model assumptions
- Make predictions

## Technical Details

### Libraries Used
- **Pandas**: Data manipulation and cleaning
- **Matplotlib**: Static plotting and visualization
- **pandas.plotting**: Additional plotting utilities
- **datetime**: Date handling and formatting

### Statistical Concepts

**Linear Regression Equation**:
```
y = mx + b
where:
- y = Predicted Revenue
- m = Slope (change in revenue per budget unit)
- x = Production Budget
- b = Y-intercept (baseline revenue)
```

**Model Evaluation Metrics**:
- **R² Score**: Proportion of variance explained (0-1)
- **Correlation (r)**: Strength of linear relationship (-1 to 1)
- **Residuals**: Differences between actual and predicted values
- **Mean Squared Error**: Average squared prediction error

### Regression Assumptions
1. **Linearity**: Relationship between X and Y is linear
2. **Independence**: Observations are independent
3. **Homoscedasticity**: Constant variance of residuals
4. **Normality**: Residuals are normally distributed

## File Structure

```
Day 78 (Scikit learn)/
├── Seaborn_and_Linear_Regression_(start).ipynb
└── cost_revenue_dirty.csv
```

## Learning Concepts

### Data Analysis Skills
- Cleaning real-world messy data
- Handling missing and inconsistent values
- Type conversion and data validation
- Outlier detection and treatment
- Data quality assessment

### Statistical Analysis
- Correlation vs causation
- Linear relationships
- Regression fundamentals
- Model fitting and evaluation
- Residual analysis
- Prediction intervals

### Visualization Best Practices
- Choosing appropriate chart types
- Clear axis labels and titles
- Legend placement
- Color selection
- Multiple subplot layouts
- Professional presentation

### Predictive Modeling
- Building simple models
- Training on historical data
- Making predictions
- Evaluating model performance
- Understanding model limitations

## Key Insights from Analysis

### Budget-Revenue Relationship
- Strong positive correlation between budget and revenue
- Higher budgets generally lead to higher revenue
- Relationship is approximately linear
- Some outliers (unexpected hits and flops)

### Industry Patterns
- Budget inflation over decades
- Revenue growth trends
- Risk vs reward in film production
- Importance of marketing budgets

### Model Performance
- How well budget predicts revenue
- Percentage of variance explained
- Prediction accuracy
- When model works best/worst

## Requirements

- Python 3.x
- Jupyter Notebook
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

## How the Code Works

1. **Data Loading**: Read CSV into DataFrame
2. **Exploration**: Check shape, columns, data types
3. **Cleaning**: Remove nulls, convert types, handle outliers
4. **Visualization**: Create scatter plots to see relationship
5. **Regression**: Fit linear model to data
6. **Evaluation**: Calculate R², check residuals
7. **Prediction**: Use model to estimate revenue for new budgets
8. **Interpretation**: Draw conclusions about relationship

## Common Patterns

### Data Cleaning
```python
# Check for missing values
df.isna().sum()

# Remove rows with missing data
df = df.dropna()

# Convert to numeric
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
```

### Visualization
```python
# Scatter plot
plt.scatter(df['budget'], df['revenue'])
plt.xlabel('Production Budget ($)')
plt.ylabel('Box Office Revenue ($)')
plt.title('Budget vs Revenue')
plt.show()
```

### Simple Regression
```python
# Calculate correlation
correlation = df['budget'].corr(df['revenue'])

# Fit line
from numpy import polyfit, polyval
m, b = polyfit(df['budget'], df['revenue'], 1)

# Make predictions
predicted = m * df['budget'] + b
```

## Real-World Applications

### Business Intelligence
- Investment decision making
- Risk assessment
- Budget allocation
- ROI prediction

### Financial Planning
- Project cost estimation
- Revenue forecasting
- Profit margin analysis
- Break-even calculations

### Strategic Planning
- Market analysis
- Competitive positioning
- Resource allocation
- Performance benchmarking

## Next Steps/Improvements

- Add multiple linear regression with more variables
- Include categorical variables (genre, rating)
- Use scikit-learn for more robust regression
- Add confidence intervals to predictions
- Implement polynomial regression
- Test for non-linear relationships
- Add time-series analysis
- Create interactive visualizations
- Build regression dashboard
- Compare different model types
- Add cross-validation
- Implement feature engineering

Perfect for learning linear regression basics, statistical analysis, data visualization, and understanding the relationship between variables in real-world datasets!
