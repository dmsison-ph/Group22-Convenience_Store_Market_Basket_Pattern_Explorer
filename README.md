# Convenience Store Market Basket Pattern Explorer

## Group 22

**Members:** Sison, Sablan, Satimbre

## Project Overview

The Convenience Store Market Basket Pattern Explorer analyzes convenience-store transaction records to discover products that are frequently purchased together.

The project uses association-rule mining to identify frequent itemsets and purchasing patterns. The same analysis is implemented using KNIME, Python, and Streamlit.

## Dataset

- 50 synthetic convenience-store transactions
- Transaction IDs: T001-T050
- 15 unique products
- 2-5 products per transaction
- Fields:
  - `Transaction_ID`
  - `Purchased_Items`

The dataset is located in:

`data/CS_Transactions.csv`

## Algorithm

### Primary Algorithm: Apriori

Apriori is used to identify frequent product combinations based on a minimum support threshold.

### Association Rules

Association rules are evaluated using:

- Support
- Confidence
- Lift
- Support Count

Default analysis settings:

- Minimum Support: 0.10
- Minimum Confidence: 0.80
- Maximum Itemset Length: 3

### Comparison Method

Frequent itemsets are compared using support count.

## Technologies

- KNIME Analytics Platform
- Python
- pandas
- mlxtend
- Streamlit
- Google Colab

## Project Structure

```text
data/
    CS_Transactions.csv

documentation/
    Group22_MarketBasket_Documentation.pdf

knime/
    KNIME_CS_Market_Basket.knwf

python/
    CS_Market_Basket.ipynb

results/
    association_rules_results.csv
    frequent_itemsets_results.csv

streamlit/
    app.py
    CS_Market_Basket_Streamlit.ipynb
    