# Analysis Summary – Customer Behaviour Analysis

## Objective
To transform raw customer transaction data into a clean, analysis-ready dataset and extract insights related to customer spending behavior, product performance, and time-based trends.

## Data Challenges
The raw dataset contained:
- Missing values in categorical and numerical columns
- Duplicate transaction records
- Inconsistent category labels
- Extreme pricing outliers

These issues required systematic data cleaning before analysis.

## Data Cleaning Approach
- Missing values were handled using mode (categorical) and median (numerical) imputation
- Duplicate records were removed to prevent skewed analysis
- Category labels were standardized for consistency
- Outliers were treated using the IQR method to reduce noise

## Exploratory Data Analysis
Key analyses performed:
- Distribution analysis of transaction amounts
- Category-wise revenue aggregation
- Customer-level spending analysis
- Monthly revenue trend analysis

## Key Insights
- Customer spending is highly right-skewed, indicating a small group of high-value customers
- Certain product categories contribute disproportionately to total revenue
- Monthly trends reveal seasonal variations in purchasing behavior
- Aggregated customer-level metrics enable segmentation into high, medium, and low spenders

## Conclusion
This project demonstrates a complete raw-to-clean data pipeline and Python-based EDA workflow. The resulting insights can support customer segmentation, retention strategies, and data-driven business decisions.
