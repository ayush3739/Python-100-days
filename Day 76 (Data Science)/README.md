# Google Play Store App Analytics

A comprehensive Jupyter notebook analyzing thousands of Android apps from the Google Play Store. This project explores app categories, ratings, pricing, installs, and reviews to understand the Android app market landscape.

## Features

- **Category Analysis**: Explore app distribution across different categories
- **Rating Analysis**: Understand app quality and user satisfaction
- **Price Analysis**: Compare free vs paid apps and pricing strategies
- **Install Analysis**: Identify most downloaded apps and categories
- **Review Analysis**: Correlate reviews with ratings and installs
- **Size Analysis**: Study app size trends across categories
- **Interactive Visualizations**: Plotly Express charts for exploration
- **Data Cleaning**: Handle duplicates, missing values, and inconsistent formats

## How to Use

1. Install required dependencies:
   ```bash
   pip install jupyter pandas plotly
   ```

2. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. Open `Google Play Store App Analytics (start).ipynb`

4. Run cells from top to bottom (Shift + Enter)

5. Interact with Plotly visualizations

## Dataset Information

### Source
- **File**: `apps.csv`
- **Source**: Scraped from Google Play Store by Lavanya Gupta (2018)
- **Original**: Available on Kaggle

### Columns
- **App**: Application name
- **Category**: App category (Games, Business, etc.)
- **Rating**: Average user rating (1-5 stars)
- **Reviews**: Number of user reviews
- **Size**: App size (varies by unit: KB, MB, etc.)
- **Installs**: Number of installs (ranges like 1,000+, 10,000+)
- **Type**: Free or Paid
- **Price**: Price in dollars
- **Content Rating**: Age appropriateness (Everyone, Teen, Mature, etc.)
- **Genres**: Detailed genre classification
- **Last Updated**: Most recent update date
- **Current Ver**: Current version number
- **Android Ver**: Minimum Android version required

## Analysis Performed

### Data Cleaning
- Remove duplicate entries
- Handle missing values
- Convert data types (size strings to numbers, installs to integers)
- Clean price strings (remove $ sign)
- Standardize category names

### Exploratory Analysis
- App distribution by category
- Free vs Paid app comparison
- Price distribution analysis
- Rating distribution and statistics
- Install count patterns
- Review count correlation with ratings

### Visualizations
- Bar charts: Apps per category
- Scatter plots: Rating vs Reviews
- Box plots: Rating distribution by category
- Histogram: Price distribution
- Pie charts: Free vs Paid apps
- Bubble charts: Rating vs Installs (sized by reviews)

## Technical Details

### Libraries Used
- **Pandas**: Data loading, cleaning, and manipulation
- **Plotly Express**: Interactive, publication-quality visualizations
- **NumPy**: Numerical operations (implicit with Pandas)

### Data Processing Techniques
- String cleaning and normalization
- Type conversion and casting
- Handling missing data with strategies
- Aggregation and grouping
- Statistical calculations
- Outlier detection and handling

### Visualization Features
- Interactive hover information
- Zoom and pan capabilities
- Color-coded categories
- Size-based encoding
- Multiple chart types
- Professional styling

## File Structure

```
Day 76 (Data Science)/
├── Google Play Store App Analytics (start).ipynb
└── apps.csv
```

## Learning Concepts

### Data Analysis Skills
- Real-world data cleaning challenges
- Handling inconsistent data formats
- Dealing with missing values appropriately
- Converting strings to numeric types
- Aggregating data for insights

### Statistical Analysis
- Descriptive statistics (mean, median, mode)
- Distribution analysis
- Correlation identification
- Comparative analysis
- Outlier detection

### Visualization Techniques
- Choosing appropriate chart types
- Interactive visualization with Plotly
- Color and size encoding
- Creating publication-quality graphics
- Storytelling with data

### Business Intelligence
- Market analysis techniques
- Competitive analysis
- Pricing strategy insights
- User behavior patterns
- Success factor identification

## Key Insights Discovered

### App Categories
- Which categories have most apps
- Most competitive categories
- Niche vs mainstream categories
- Category growth trends

### Pricing Strategies
- Free vs Paid app distribution
- Price ranges by category
- Premium app characteristics
- Monetization approaches

### User Engagement
- Correlation between ratings and reviews
- Most reviewed apps and why
- Rating distribution patterns
- User satisfaction indicators

### Success Factors
- Characteristics of top-rated apps
- Relationship between size and success
- Update frequency impact
- Category-specific success patterns

## Requirements

- Python 3.x
- Jupyter Notebook
- pandas (data manipulation)
- plotly (interactive visualization)

## Environment Setup

### Windows (PowerShell):
```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install jupyter pandas plotly
jupyter notebook
```

### macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install jupyter pandas plotly
jupyter notebook
```

## How the Code Works

1. **Data Loading**: Reads apps.csv into Pandas DataFrame
2. **Initial Exploration**: Checks shape, columns, and data types
3. **Data Cleaning**: Removes duplicates, handles missing values, converts types
4. **Analysis**: Groups, aggregates, and calculates statistics
5. **Visualization**: Creates interactive Plotly charts
6. **Insights**: Draws conclusions from patterns and correlations

## Common Issues and Solutions

### Data Type Issues
- **Problem**: Size column contains mixed units (KB, MB)
- **Solution**: Parse strings and convert all to MB

### Missing Values
- **Problem**: Some apps have missing ratings
- **Solution**: Decide to drop or fill based on analysis needs

### Outliers
- **Problem**: Some installs or prices are extreme
- **Solution**: Filter or transform for better visualization

### String Formatting
- **Problem**: Install counts have "+" and "," characters
- **Solution**: Strip characters and convert to integers

## Next Steps/Improvements

- Add time-series analysis of update dates
- Sentiment analysis on app descriptions
- Predict app success using machine learning
- Compare categories in more detail
- Add review text analysis (if review data available)
- Create dashboard with multiple linked visualizations
- Analyze version number patterns
- Study Android version requirements trends
- Build recommendation system
- Perform competitive analysis by category

Perfect for learning data cleaning, exploratory data analysis, interactive visualization with Plotly, and understanding mobile app market dynamics!
