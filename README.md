# Convenience Store Market Basket Pattern Explorer

## Group 22

**Members:** Sison, Sablan, Satimbre

## Project Overview

The **Convenience Store Market Basket Pattern Explorer** analyzes convenience-store transaction records to discover products that are frequently purchased together.

The project uses **association-rule mining** and the **Apriori algorithm** to identify frequent itemsets and purchasing patterns. The same market basket analysis is implemented using **KNIME, Python, and Streamlit**.

The Streamlit application allows users to upload a transaction dataset, adjust the minimum support and confidence thresholds, view frequent itemsets and association rules, and download the generated results.

---

## Project Scenario

A convenience store wants to analyze customer transaction records to discover products that are frequently purchased together.

The system answers questions such as:

- Which products frequently occur together?
- Which product combinations satisfy the selected minimum support?
- Which association rules satisfy the selected confidence threshold?
- How strong are the relationships between products based on lift?
- How do the KNIME and Python implementations compare?

---

## Dataset

The project uses a synthetic convenience-store transaction dataset containing:

- **50 transactions**
- Transaction IDs from **T001 to T050**
- **15 unique products**
- Approximately **2-5 products per transaction**

### Dataset Fields

| Field | Type | Description |
|---|---|---|
| `Transaction_ID` | String | Unique identifier assigned to each transaction |
| `Purchased_Items` | String/List | Comma-separated products purchased within the transaction |

Example:

```csv
Transaction_ID,Purchased_Items
T001,"Soft Drink, Chips"
T002,"Coffee, Bread, Biscuits"
T003,"Instant Noodles, Eggs"
```

The main dataset is located at:

```text
data/CS_Transactions.csv
```

---

## Primary Algorithm

### Apriori

The project uses the **Apriori algorithm** to discover frequent itemsets.

Apriori identifies products or product combinations that occur frequently enough to satisfy a selected **minimum support threshold**.

The Python implementation uses:

```python
from mlxtend.frequent_patterns import apriori, association_rules
```

### Association Rules

Association rules are evaluated using the following measurements:

- **Support** - how frequently an item or item combination occurs across all transactions.
- **Confidence** - how often the consequent occurs when the antecedent occurs.
- **Lift** - measures how strongly two items are associated compared with their expected independent occurrence.
- **Support Count** - the actual number of transactions containing the item or item combination.

### Default Settings

```text
Minimum Support:    0.10
Minimum Confidence: 0.80
Maximum Itemset Length: 3
```

### Comparison Method

Frequent itemsets are also compared using their **support count**.

---

## Technologies Used

- **KNIME Analytics Platform** - visual workflow implementation
- **Python** - programmatic implementation
- **Google Colab / Jupyter Notebook** - Python development environment
- **pandas** - dataset loading and processing
- **mlxtend** - Apriori and association-rule mining
- **Streamlit** - interactive web interface
- **Git / GitHub** - version control and project repository

---

## Project Structure

```text
Group22-Convenience_Store_Market_Basket_Pattern_Explorer/
│
├── data/
│   └── CS_Transactions.csv
│
├── documentation/
│   └── Group22_MarketBasket_Documentation.pdf
│
├── knime/
│   └── KNIME_CS_Market_Basket.knwf
│
├── python/
│   └── CS_Market_Basket.ipynb
│
├── results/
│   ├── association_rules_results.csv
│   └── frequent_itemsets_results.csv
│
├── streamlit/
│   ├── app.py
│   └── CS_Market_Basket_Streamlit.ipynb
│
├── README.md
└── requirements.txt
```

---

# Requirements

## Software Requirements

To use the complete project, the following software is recommended:

### Python Implementation and Streamlit

- Python 3
- pip
- A modern web browser
- Visual Studio Code, Google Colab, Jupyter Notebook, or another Python environment

### KNIME Implementation

- KNIME Analytics Platform

### Optional Development Tools

- Git
- GitHub account
- Visual Studio Code

---

## Python Package Requirements

The required Python packages are listed in:

```text
requirements.txt
```

The primary packages are:

```text
pandas
mlxtend
streamlit
```

Additional dependencies may automatically be installed by pip.

---

# Installation

## 1. Download the Repository

You can download the repository through GitHub:

**Code → Download ZIP**

Extract the ZIP file to a folder on your computer.

Alternatively, if Git is installed, clone the repository:

```bash
git clone https://github.com/dmsison-ph/Group22-Convenience_Store_Market_Basket_Pattern_Explorer.git
```

Enter the project directory:

```bash
cd Group22-Convenience_Store_Market_Basket_Pattern_Explorer
```

---

## 2. Install Python Dependencies

From the project root, run:

```bash
pip install -r requirements.txt
```

This installs the packages required by the Python and Streamlit implementations.

If `pip` is not recognized, try:

```bash
python -m pip install -r requirements.txt
```

---

# How to Use

## Option 1 - Run the Streamlit Application

From the project root, run:

```bash
streamlit run streamlit/app.py
```

If the `streamlit` command is not recognized, use:

```bash
python -m streamlit run streamlit/app.py
```

Streamlit should display a local address similar to:

```text
http://localhost:8501
```

Open the address in a web browser if it does not open automatically.

### Using the Application

1. Locate the **Upload Transaction CSV** section.
2. Upload:

```text
data/CS_Transactions.csv
```

3. Set the desired **Minimum Support**.
4. Set the desired **Minimum Confidence**.
5. Review the dataset preview.
6. Review the generated frequent itemsets.
7. Review the generated association rules.
8. Examine support, confidence, lift, and support count.
9. Use the download buttons to export the result tables if needed.

For reproducing the project's primary results, use:

```text
Minimum Support: 0.10
Minimum Confidence: 0.80
```

---

## Option 2 - Run the Python Analysis

Open:

```text
python/CS_Market_Basket.ipynb
```

The notebook can be opened using:

- Google Colab
- Jupyter Notebook
- Visual Studio Code with Jupyter support

The notebook performs the following process:

```text
Load Dataset
      ↓
Validate Dataset
      ↓
Prepare Transactions
      ↓
Transaction Encoding
      ↓
Apriori
      ↓
Frequent Itemsets
      ↓
Association Rules
      ↓
Calculate Support Count
      ↓
Sort and Compare Results
      ↓
Export CSV Results
```

The generated result files are stored in:

```text
results/
```

---

## Option 3 - Open the KNIME Workflow

Open KNIME Analytics Platform and import/open:

```text
knime/KNIME_CS_Market_Basket.knwf
```

The KNIME workflow visually performs the market basket analysis through connected nodes for transaction preparation, association-rule generation, sorting, and support-count calculation.

### Important KNIME Note

If the **CSV Reader** cannot locate the dataset because the workflow was created on another computer, manually select:

```text
data/CS_Transactions.csv
```

in the CSV Reader configuration.

File paths can differ between computers.

---

# Key Results

Using:

```text
Minimum Support = 0.10
Minimum Confidence = 0.80
```

the analysis identified five qualifying association rules:

| Antecedent | Consequent | Support | Confidence | Lift | Support Count |
|---|---|---:|---:|---:|---:|
| Instant Noodles | Eggs | 0.16 | 1.00 | 3.571 | 8 |
| Corned Beef | Eggs | 0.10 | 1.00 | 3.571 | 5 |
| Hotdog | Bread | 0.10 | 1.00 | 2.381 | 5 |
| Peanut Butter | Bread | 0.10 | 1.00 | 2.381 | 5 |
| Milk | Bread | 0.10 | 1.00 | 2.381 | 5 |

The KNIME and Python implementations produced consistent association-rule results when equivalent thresholds were used.

---

# Testing

The application was tested using several conditions.

### Normal Input

The original 50-transaction dataset was processed using:

```text
Minimum Support = 0.10
Minimum Confidence = 0.80
```

The application successfully generated frequent itemsets and association rules.

### Invalid CSV Structure

A CSV without the required:

```text
Transaction_ID
Purchased_Items
```

columns was rejected.

The Streamlit application displayed a user-friendly validation message instead of processing the invalid file.

### Threshold Sensitivity

Lowering the minimum confidence from:

```text
0.80 → 0.60
```

allowed additional association rules to qualify.

This demonstrates how the selected threshold affects the number of generated rules.

### High Support Boundary Test

The minimum support was increased to:

```text
0.50
```

No frequent itemsets were produced because no item appeared in at least 50% of the transactions.

The application correctly displayed:

```text
No frequent itemsets were found using the selected minimum support.
Try lowering the support threshold.
```

---

# Important Notes

### Required CSV Format

Uploaded transaction files must contain exactly the required fields:

```text
Transaction_ID
Purchased_Items
```

`Purchased_Items` should contain comma-separated product names.

Example:

```csv
T001,"Soft Drink, Chips"
```

### Do Not Upload Result CSVs as Input

The following files are **outputs**, not transaction input files:

```text
results/association_rules_results.csv
results/frequent_itemsets_results.csv
```

Uploading these files into the Streamlit transaction uploader will cause validation to fail because they do not contain the required transaction columns.

Use:

```text
data/CS_Transactions.csv
```

instead.

### Jupyter Notebook Files

Files ending in:

```text
.ipynb
```

are Jupyter Notebook files containing Python code.

The Python implementation was developed using Google Colab, which uses the `.ipynb` notebook format.

---

# Troubleshooting

## Streamlit Command Is Not Recognized

Try:

```bash
python -m streamlit run streamlit/app.py
```

If Streamlit is not installed:

```bash
python -m pip install streamlit
```

---

## `ModuleNotFoundError: mlxtend`

Install mlxtend:

```bash
python -m pip install mlxtend
```

Or reinstall all project requirements:

```bash
python -m pip install -r requirements.txt
```

---

## CSV Required-Columns Error

If Streamlit displays:

```text
The CSV must contain the columns 'Transaction_ID' and 'Purchased_Items'.
```

verify that you uploaded:

```text
data/CS_Transactions.csv
```

and not one of the generated result CSV files.

The first row of the correct dataset should contain:

```csv
Transaction_ID,Purchased_Items
```

---

## No Frequent Itemsets Found

If the application displays:

```text
No frequent itemsets were found using the selected minimum support.
```

the support threshold may be too high.

Lower **Minimum Support**.

For the supplied dataset, the recommended starting value is:

```text
0.10
```

---

## No Association Rules Found

If frequent itemsets are available but no association rules are displayed, the confidence requirement may be too restrictive for the available patterns.

Try lowering **Minimum Confidence**.

The project's default value is:

```text
0.80
```

---

## KNIME Cannot Find the CSV

The KNIME CSV Reader may contain a path from the computer on which the workflow was originally created.

Open the **CSV Reader** configuration and manually select:

```text
data/CS_Transactions.csv
```

Then execute the workflow again.

---

## Port 8501 Is Already in Use

If Streamlit reports that port `8501` is unavailable, another Streamlit process may already be running.

Stop the existing process using:

```text
Ctrl + C
```

in the terminal where it is running.

Alternatively, start Streamlit on another port:

```bash
streamlit run streamlit/app.py --server.port 8502
```

---

## Google Colab and `localhost`

When Streamlit runs inside Google Colab, `localhost` refers to the remote Colab runtime rather than the user's computer.

For local use, running:

```bash
streamlit run streamlit/app.py
```

directly on a computer is simpler.

The included Streamlit notebook documents the Colab-based development process.

---

## Dependency Warning During Installation

pip may display warnings involving packages already installed on a computer.

If the required project packages install successfully and the Streamlit application runs correctly, unrelated package conflicts may not affect this project.

Using a dedicated Python virtual environment is recommended for a cleaner installation.

---

# Project Limitations

This project has several important limitations.

### Synthetic Dataset

The dataset contains only **50 synthetic transactions**. The transactions were created for academic demonstration and do not represent actual customer purchasing behavior.

### Small Sample Size

Fifty transactions are sufficient to demonstrate Apriori and association-rule mining but are too few for drawing reliable conclusions about real-world consumer behavior.

### Limited Product Selection

The dataset contains only **15 product categories**. Real convenience stores may contain hundreds or thousands of different products.

### Threshold Dependence

The generated patterns depend strongly on the selected minimum support and minimum confidence values.

Changing these thresholds may:

- remove existing rules,
- generate additional rules,
- or result in no qualifying patterns.

### Association Does Not Mean Causation

An association rule indicates that products occurred together frequently in the dataset.

It does **not** prove that purchasing one product causes a customer to purchase another.

### Synthetic Patterns May Be Stronger Than Real Patterns

Because the dataset was deliberately constructed for demonstration, some relationships have very high confidence values. Real transaction data would likely contain more variation and noise.

### No Real-Time Transaction Integration

The application analyzes uploaded CSV files. It is not connected to an actual point-of-sale or convenience-store transaction system.

### Academic Prototype

The system should be treated as an educational market basket analysis prototype rather than a production-ready retail analytics platform.

---

# Documentation

The complete project documentation is available at:

```text
documentation/Group22_MarketBasket_Documentation.pdf
```

It contains:

- Dataset information
- Data dictionary
- KNIME workflow
- Python implementation process
- Streamlit interface
- Testing evidence
- Comparison results
- Interpretation and limitations

---

## Group Responsibilities

| Member | Primary Responsibility | Secondary Responsibility |
|---|---|---|
| Sison | Python + Streamlit | Project leadership and integration |
| Sablan | KNIME + Algorithm Evaluation | Results comparison |
| Satimbre | Dataset + Documentation | Testing and KNIME assistance |

---

## Repository

**Group 22 - Convenience Store Market Basket Pattern Explorer**

Developed as an academic project using **KNIME, Python, Apriori, association-rule mining, and Streamlit**.

## Presentation Video

The Group 22 Audio-Visual Presentation (AVP) is available in:

`video/Group_22_AVP.mp4`
