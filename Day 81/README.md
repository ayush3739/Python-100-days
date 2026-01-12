# Multivariable Regression and Valuation Model

A comprehensive Jupyter notebook building a multivariable linear regression model to estimate Boston house prices. This project demonstrates feature analysis, model training, evaluation, residual analysis, and using data transformations to improve predictions.

## Features

- **Multivariable Regression**: Predict prices using multiple features simultaneously
- **Feature Analysis**: Understand impact of each characteristic on price
- **Train-Test Split**: Proper model validation methodology
- **Model Evaluation**: R², residuals, and coefficient analysis
- **Data Transformation**: Log transformations to improve model fit
- **Prediction System**: Estimate property values from characteristics
- **Residual Analysis**: Check model assumptions and identify issues
- **Feature Engineering**: Create and test new predictive variables
- **Interactive Visualization**: Plotly for exploring relationships

## Real-World Application

### Business Context
You're working for a real estate development company in 1970s Boston. Your task is to build a model that can value residential properties before starting new projects.

### Prediction Features
- Number of rooms
- Distance to employment centers
- Area demographics (wealth/poverty indicators)
- Student-teacher ratios in local schools
- Property tax rates
- Crime rates
- Air quality
- And more...

## How to Use

1. Install required dependencies:
   ```bash
   pip install jupyter pandas numpy matplotlib seaborn plotly scikit-learn
   ```

2. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. Open `Multivariable_Regression_and_Valuation_Model_(complete).ipynb`

4. Run cells from top to bottom

5. Experiment with feature combinations

## Dataset Information

### Source
- **File**: `boston.csv`
- **Origin**: Boston Housing Dataset (Harrison & Rubinfeld, 1978)
- **Samples**: 506 houses in Boston suburbs
- **Target**: Median home value ($1000s)

### Features (13 total)

**Property Characteristics**:
- **RM**: Average number of rooms per dwelling
- **AGE**: Proportion of owner-occupied units built before 1940
- **LSTAT**: % lower status of the population

**Location & Access**:
- **DIS**: Weighted distances to employment centers
- **RAD**: Index of accessibility to radial highways
- **TAX**: Property tax rate per $10,000

**Environment**:
- **CRIM**: Per capita crime rate
- **NOX**: Nitric oxides concentration (air quality)
- **INDUS**: Proportion of non-retail business acres
- **ZN**: Proportion of residential land zoned for large lots

**Schools & Services**:
- **PTRATIO**: Pupil-teacher ratio
- **B**: 1000(Bk - 0.63)² where Bk is proportion of Black residents

**Geography**:
- **CHAS**: Charles River dummy (1 if bounds river, 0 otherwise)

## Analysis Workflow

### 1. Data Exploration
- Load and examine dataset structure
- Check for missing values
- Calculate descriptive statistics
- Visualize distributions
- Identify correlations

### 2. Exploratory Data Analysis
- Create scatter plots for each feature
- Identify strongest correlations
- Check for non-linear relationships
- Detect outliers
- Understand feature ranges

### 3. Data Preparation
- Train-test split (80/20 or 70/30)
- Feature scaling (if needed)
- Handle outliers
- Check for multicollinearity

### 4. Model Training
- Fit multivariable linear regression
- Use all features initially
- Analyze coefficients
- Interpret results

### 5. Model Evaluation
- Calculate R² on training set
- Calculate R² on test set
- Analyze residuals
- Check assumptions
- Identify weaknesses

### 6. Model Improvement
- Apply log transformations
- Remove outliers
- Engineer new features
- Test different combinations
- Compare performance

### 7. Making Predictions
- Use model to estimate new property values
- Provide confidence intervals
- Interpret predictions
- Understand limitations

## Technical Details

### Libraries Used
- **Pandas**: Data manipulation
- **NumPy**: Numerical operations
- **Matplotlib**: Static visualizations
- **Seaborn**: Statistical plots
- **Plotly Express**: Interactive charts
- **Scikit-learn**: Machine learning (LinearRegression, train_test_split)

### Linear Regression Equation
```
Price = β₀ + β₁(RM) + β₂(LSTAT) + β₃(DIS) + ... + β₁₃(CHAS)

where:
- β₀ = intercept
- β₁...β₁₃ = coefficients for each feature
```

### Model Evaluation Metrics

**R² (R-squared)**:
- Proportion of variance explained by model
- Range: 0 to 1 (higher is better)
- 1 = perfect predictions, 0 = no better than mean

**Residuals**:
- Difference between actual and predicted values
- Should be randomly distributed
- Check for patterns indicating problems

**Mean Squared Error (MSE)**:
- Average squared difference between predictions and actuals
- Lower is better
- Sensitive to outliers

**Root Mean Squared Error (RMSE)**:
- Square root of MSE
- Same units as target variable
- Interpretable error magnitude

### Data Transformations

**Log Transformation**:
- Applied to skewed features
- Reduces impact of outliers
- Can improve linearity
- Makes relationships multiplicative

**Benefits**:
- Better model fit
- Improved R²
- More normal residuals
- Better predictions

## File Structure

```
Day 81/
├── Multivariable_Regression_and_Valuation_Model_(complete).ipynb
└── boston.csv
```

## Learning Concepts

### Regression Analysis
- Multiple linear regression
- Coefficient interpretation
- Feature importance
- Model assumptions

### Model Validation
- Train-test split methodology
- Cross-validation concepts
- Overfitting vs underfitting
- Generalization to new data

### Feature Engineering
- Creating new features
- Transforming existing features
- Combining features
- Scaling and normalization

### Residual Analysis
- Plotting residuals
- Checking for patterns
- Identifying outliers
- Validating assumptions

### Statistical Concepts
- Correlation vs causation
- Multicollinearity
- Heteroscedasticity
- Normal distribution

## Key Insights

### Most Important Features
- **RM (Rooms)**: More rooms = higher price
- **LSTAT (Lower Status)**: Higher % = lower price
- **PTRATIO (Student-Teacher)**: Higher ratio = lower price
- **DIS (Distance)**: Distance from employment affects price

### Model Performance
- Base model typically achieves R² ~0.70-0.75
- Log transformations can improve to R² ~0.80-0.85
- Some variation difficult to capture with linear model
- Outliers significantly impact predictions

### Business Applications
- Quick property valuation estimates
- Investment decision support
- Development planning
- Market analysis

## Requirements

- Python 3.x
- Jupyter Notebook
- pandas (data manipulation)
- numpy (numerical operations)
- matplotlib (visualization)
- seaborn (statistical plots)
- plotly (interactive charts)
- scikit-learn (machine learning)

## Environment Setup

### Windows (PowerShell):
```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install jupyter pandas numpy matplotlib seaborn plotly scikit-learn
jupyter notebook
```

### macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install jupyter pandas numpy matplotlib seaborn plotly scikit-learn
jupyter notebook
```

## How the Code Works

1. **Data Loading**: Import Boston housing dataset
2. **Exploration**: Examine features, distributions, correlations
3. **Visualization**: Plot relationships between features and price
4. **Split Data**: Separate training and testing sets
5. **Train Model**: Fit multivariable regression on training data
6. **Evaluate**: Calculate R², analyze residuals on test set
7. **Transform**: Apply log transformations to improve fit
8. **Retrain**: Fit new model on transformed data
9. **Compare**: Evaluate improvement in performance
10. **Predict**: Use final model to estimate new property values

## Real-World Applications

### Real Estate
- Property valuation
- Investment analysis
- Development feasibility
- Market pricing

### Finance
- Mortgage risk assessment
- Portfolio valuation
- Investment strategy
- Market analysis

### Urban Planning
- Policy impact analysis
- Zoning decisions
- Infrastructure planning
- Community development

## Common Patterns

### Training a Model
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
r_squared = model.score(X_test, y_test)
```

### Making Predictions
```python
# Predict on new data
new_property = [[6, 15.5, 3.5, ...]]  # feature values
predicted_price = model.predict(new_property)
```

## Next Steps/Improvements

- Add polynomial features
- Try regularization (Ridge, Lasso)
- Implement cross-validation
- Add feature selection
- Test non-linear models
- Create prediction intervals
- Build interactive dashboard
- Add more recent data
- Include neighborhood features
- Implement ensemble methods
- Add geographical visualization
- Create API for predictions

Perfect for learning multivariable regression, model evaluation, data transformation techniques, and building practical predictive models for real-world valuation problems!
