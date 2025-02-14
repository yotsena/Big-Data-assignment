E-commerce Data Pipeline (PySpark)
Name:Etsubdink Tadesse
ID:DBUR/3971/13

Overview
This project implements an end-to-end data pipeline using PySpark and DuckDB for processing e-commerce transactions. The pipeline extracts, transforms, and loads (ETL) data efficiently.

🚀 Project Workflow
1️⃣ Data Extraction
Loads raw e-commerce data from a CSV file using PySpark.
2️⃣ Data Transformation
Cleans and preprocesses data, handling missing values and filtering invalid records.
Categorizes transactions based on price into High, Medium, and Low Value.
3️⃣ Data Loading
Stores transformed data into DuckDB, a lightweight OLAP database.
📂 Directory Structure
├── data/                    # Raw and processed datasets
├── scripts/                 # Python scripts for ETL pipeline
│   ├── extract.py           # Extracts data from CSV
│   ├── transform.py         # Cleans and transforms data
│   ├── load.py              # Loads data into DuckDB
│
├── notebooks/               # Jupyter notebooks for analysis
├── visualizations/          # Tableau dashboards & insights
├── README.md                # Project documentation


⚙️ How to Run
🔹 Setup Environment
Ensure Python 3.x is installed, then install dependencies:

pip install pyspark duckdb
🔹 Run the Pipeline
Execute the ETL pipeline step-by-step:

python3 scripts/extract.py
python3 scripts/transform.py
python3 scripts/load.py
🛠️ Data Processing Steps
1️⃣ Handling Missing Values
CustAccountBalance → Filled missing values with 0.
CustGender & brand → Replaced missing values with "Unknown".
2️⃣ Transaction Type Categorization
A new column transaction_type was added:

Price Range	Category
price > 10000	High Value
1000 < price ≤ 10000	Medium Value
price ≤ 1000	Low Value
3️⃣ Filtering Data
Removed rows where price ≤ 0 (invalid transactions).
📊 Tableau Visualizations
The processed data is visualized using Tableau to derive meaningful insights.

🔗 Key Dashboards:
✅ Sales Trends Over Time ✅ Sales by Location ✅ Transaction Types ✅ Customer Segmentation

🔹 Insights from the Data
📌 Sales peaked in December, likely due to holiday shopping. 📌 Customers in Mumbai contributed the highest revenue. 📌 High-value transactions accounted for 30% of total revenue.

🤝 Contributing
Feel free to fork, create issues, or submit pull requests to improve this pipeline!

📜 License
This project is open-source under the MIT License.

🏷️ Keywords
PySpark, ETL, Data Pipeline, E-commerce, Big Data, DuckDB, Tableau

