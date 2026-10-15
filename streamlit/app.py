
import streamlit as st
import pandas as pd

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Convenience Store Market Basket Pattern Explorer",
    layout="wide"
)

st.title("Convenience Store Market Basket Pattern Explorer")

st.write(
    """
    Upload a convenience-store transaction dataset to discover
    frequently purchased product combinations and association rules
    using the Apriori algorithm.
    """
)


# --------------------------------------------------
# SIDEBAR SETTINGS
# --------------------------------------------------

st.sidebar.header("Analysis Settings")

min_support = st.sidebar.slider(
    "Minimum Support",
    min_value=0.05,
    max_value=0.50,
    value=0.10,
    step=0.05
)

min_confidence = st.sidebar.slider(
    "Minimum Confidence",
    min_value=0.10,
    max_value=1.00,
    value=0.80,
    step=0.05
)

st.sidebar.write(
    f"Minimum Support: {min_support:.2f}"
)

st.sidebar.write(
    f"Minimum Confidence: {min_confidence:.2f}"
)


# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Transaction CSV",
    type=["csv"]
)


# --------------------------------------------------
# RUN ANALYSIS
# --------------------------------------------------

if uploaded_file is not None:

    try:

        # ------------------------------------------
        # LOAD DATASET
        # ------------------------------------------

        df = pd.read_csv(uploaded_file)

        required_columns = [
            "Transaction_ID",
            "Purchased_Items"
        ]


        # ------------------------------------------
        # VALIDATE COLUMNS
        # ------------------------------------------

        if not all(
            column in df.columns
            for column in required_columns
        ):
            st.error(
                "The CSV must contain the columns "
                "'Transaction_ID' and 'Purchased_Items'."
            )
            st.stop()


        # ------------------------------------------
        # VALIDATE EMPTY DATA
        # ------------------------------------------

        if df.empty:
            st.error(
                "The uploaded CSV contains no transactions."
            )
            st.stop()


        if df[required_columns].isnull().any().any():
            st.error(
                "The dataset contains missing Transaction IDs "
                "or Purchased Items."
            )
            st.stop()


        # ------------------------------------------
        # DATASET INFORMATION
        # ------------------------------------------

        st.success("Dataset loaded successfully.")

        st.subheader("Dataset Information")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Transactions",
                len(df)
            )

        with col2:
            st.metric(
                "Dataset Columns",
                len(df.columns)
            )


        st.subheader("Dataset Preview")

        st.dataframe(
            df,
            use_container_width=True
        )


        # ------------------------------------------
        # PREPARE TRANSACTIONS
        # ------------------------------------------

        transactions = (
            df["Purchased_Items"]
            .str.split(",")
            .apply(
                lambda items: [
                    item.strip()
                    for item in items
                    if item.strip()
                ]
            )
            .tolist()
        )


        # ------------------------------------------
        # TRANSACTION ENCODING
        # ------------------------------------------

        encoder = TransactionEncoder()

        encoded_array = (
            encoder
            .fit(transactions)
            .transform(transactions)
        )

        basket_df = pd.DataFrame(
            encoded_array,
            columns=encoder.columns_
        )


        # ------------------------------------------
        # APRIORI
        # ------------------------------------------

        frequent_itemsets = apriori(
            basket_df,
            min_support=min_support,
            use_colnames=True,
            max_len=3
        )


        # ------------------------------------------
        # CHECK ITEMSET RESULTS
        # ------------------------------------------

        if frequent_itemsets.empty:

            st.warning(
                "No frequent itemsets were found using the "
                "selected minimum support. Try lowering "
                "the support threshold."
            )

            st.stop()


        # ------------------------------------------
        # SUPPORT COUNT
        # ------------------------------------------

        frequent_itemsets["support_count"] = (
            frequent_itemsets["support"]
            * len(df)
        ).round().astype(int)


        # ------------------------------------------
        # FORMAT ITEMSETS
        # ------------------------------------------

        def format_itemset(itemset):
            return ", ".join(
                sorted(itemset)
            )


        itemset_results = frequent_itemsets.copy()

        itemset_results["itemsets"] = (
            itemset_results["itemsets"]
            .apply(format_itemset)
        )

        itemset_results = itemset_results[
            [
                "itemsets",
                "support",
                "support_count"
            ]
        ]

        itemset_results = (
            itemset_results
            .sort_values(
                by="support_count",
                ascending=False
            )
            .reset_index(drop=True)
        )


        # ------------------------------------------
        # DISPLAY FREQUENT ITEMSETS
        # ------------------------------------------

        st.subheader("Frequent Itemsets")

        st.write(
            """
            Frequent itemsets show products or product
            combinations that appear often enough to meet
            the selected minimum support.
            """
        )

        st.dataframe(
            itemset_results,
            use_container_width=True
        )


        # ------------------------------------------
        # ASSOCIATION RULES
        # ------------------------------------------

        rules = association_rules(
            frequent_itemsets,
            metric="confidence",
            min_threshold=min_confidence
        )


        if rules.empty:

            st.warning(
                "Frequent itemsets were found, but no "
                "association rules meet the selected "
                "minimum confidence. Try lowering the "
                "confidence threshold."
            )

        else:

            rule_results = rules[
                [
                    "antecedents",
                    "consequents",
                    "support",
                    "confidence",
                    "lift"
                ]
            ].copy()

            rule_results["support_count"] = (
                rule_results["support"] * len(df)
            ).round().astype(int)

            rule_results["antecedents"] = (
                rule_results["antecedents"]
                .apply(format_itemset)
            )

            rule_results["consequents"] = (
                rule_results["consequents"]
                .apply(format_itemset)
            )

            rule_results = (
                rule_results
                .sort_values(
                    by="lift",
                    ascending=False
                )
                .reset_index(drop=True)
            )

            st.subheader("Association Rules")

            st.write(
                """
                Association rules show relationships between
                products using support, confidence, and lift.
                """
            )

            st.dataframe(
                rule_results,
                use_container_width=True
            )

            st.subheader("How to Read the Results")

            st.write(
                """
                *Support* — how frequently the product
                combination appears in all transactions.

                *Confidence* — how often the consequent
                appears when the antecedent is purchased.

                *Lift* — how strongly the products are
                associated compared with random occurrence.

                *Support Count* — the actual number of
                transactions containing the combination.
                """
            )

            rules_csv = (
                rule_results
                .to_csv(index=False)
                .encode("utf-8")
            )

            st.download_button(
                label="Download Association Rules",
                data=rules_csv,
                file_name="association_rules_results.csv",
                mime="text/csv"
            )

        itemsets_csv = (
            itemset_results
            .to_csv(index=False)
            .encode("utf-8")
        )

        st.download_button(
            label="Download Frequent Itemsets",
            data=itemsets_csv,
            file_name="frequent_itemsets_results.csv",
            mime="text/csv"
        )

    except Exception as error:

        st.error(
            f"Unable to process the dataset: {error}"
        )

else:

    st.info(
        "Upload CS_Transactions.csv to begin "
        "the market basket analysis."
    )
