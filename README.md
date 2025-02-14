# E-commerce Data Pipeline (PySpark)  
**Author:** Etsubdink Tadesse  
**ID:** DBUR/3971/13  

📌 **Overview**  
This project implements an **end-to-end data pipeline** using **PySpark** and **DuckDB** for processing e-commerce transactions. The pipeline efficiently extracts, transforms, and loads (ETL) data.

---

## 🚀 Project Workflow

1️⃣ **Data Extraction**  
   - Loads raw e-commerce data from a **CSV file** using **PySpark**.

2️⃣ **Data Transformation**  
   - Cleans and preprocesses data, handling missing values and filtering invalid records.  
   - Categorizes transactions based on price into **High, Medium, and Low Value**.

3️⃣ **Data Loading**  
   - Stores transformed data into **DuckDB**, a lightweight OLAP database.

---

## 📂 Directory Structure


---

## ⚙️ How to Run

### 🔹 **Setup Environment**
Ensure Python 3.x is installed, then install dependencies:

```sh
pip install pyspark duckdb

python3 scripts/extract.py
python3 scripts/transform.py
python3 scripts/load.py

### 📂 Large Files
Due to size limitations, large files are stored externally. You can download them from this link:

🔗 [Download Data File](https://drive.google.com/drive/folders/1gJD_VtexnS7mv01XG65GyL3rR3DP8Lpu?usp=sharing)


