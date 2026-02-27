import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="Customer Behavior Dashboard", layout="wide")

st.title("📊 Customer Behavior Analysis Dashboard")


# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("customer_transactions_processed.csv")
    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])
    df["TotalAmount"] = pd.to_numeric(df["TotalAmount"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df.dropna(inplace=True)
    return df


df = load_data()

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

country = st.sidebar.multiselect("Select Country", df["Country"].unique())
category = st.sidebar.multiselect(
    "Select Product Category", df["ProductCategory"].unique()
)

if country:
    df = df[df["Country"].isin(country)]

if category:
    df = df[df["ProductCategory"].isin(category)]

# -----------------------------
# 1️⃣ KPI Row
# -----------------------------
total_revenue = df["TotalAmount"].sum()
total_transactions = df["TransactionID"].nunique()
total_customers = df["CustomerID"].nunique()
avg_order_value = total_revenue / total_transactions if total_transactions > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Revenue", f"${total_revenue:,.0f}")
col2.metric("🧾 Total Transactions", total_transactions)
col3.metric("👥 Total Customers", total_customers)
col4.metric("📊 Avg Order Value", f"${avg_order_value:,.2f}")

st.divider()

# 2️⃣ Monthly Revenue Trend
monthly = (
    df.groupby(pd.Grouper(key="TransactionDate", freq="M"))["TotalAmount"]
    .sum()
    .reset_index()
)
fig = px.line(
    monthly,
    x="TransactionDate",
    y="TotalAmount",
    title="Monthly Revenue Trend",
    markers=True,
)
st.plotly_chart(fig, use_container_width=True)

# 3️⃣ Revenue by Category
category_rev = df.groupby("ProductCategory")["TotalAmount"].sum().reset_index()
fig = px.bar(
    category_rev,
    x="ProductCategory",
    y="TotalAmount",
    title="Revenue by Product Category",
)
st.plotly_chart(fig, use_container_width=True)

# 4️⃣ Revenue by Country
country_rev = df.groupby("Country")["TotalAmount"].sum().reset_index()
fig = px.bar(country_rev, x="Country", y="TotalAmount", title="Revenue by Country")
st.plotly_chart(fig, use_container_width=True)

# 5️⃣ Top 10 Customers

top_customers = (
    df.groupby("CustomerID")["TotalAmount"].sum().sort_values(ascending=False).head(10)
)

# Convert index to string
top_customers.index = top_customers.index.astype(str)

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(top_customers.index, top_customers.values, width=0.6)

ax.set_title("Top 10 Customers by Revenue")
ax.set_xlabel("Customer ID")
ax.set_ylabel("Revenue")

plt.xticks(rotation=45)

# Add revenue labels above bars
for i, v in enumerate(top_customers.values):
    ax.text(i, v, f"{v:,.0f}", ha="center")

plt.tight_layout()

st.pyplot(fig)

# 6️⃣ Purchase Frequency Histogram
customer_freq = df.groupby("CustomerID")["TransactionID"].count()
fig = px.histogram(
    customer_freq, nbins=20, title="Customer Purchase Frequency Distribution"
)
st.plotly_chart(fig, use_container_width=True)

# 7️⃣ Payment Method Pie
payment_dist = df["PaymentMethod"].value_counts().reset_index()
payment_dist.columns = ["PaymentMethod", "Count"]
fig = px.pie(
    payment_dist,
    names="PaymentMethod",
    values="Count",
    title="Payment Method Distribution",
)
st.plotly_chart(fig, use_container_width=True)

# 8️⃣ Average Revenue per Customer
avg_rev_customer = df.groupby("CustomerID")["TotalAmount"].sum().mean()
st.metric("Avg Revenue per Customer", f"${avg_rev_customer:,.2f}")

# 9️⃣ Average Quantity per Transaction
avg_qty = df["Quantity"].mean()
st.metric("Avg Quantity per Transaction", round(avg_qty, 2))

# 🔟 Monthly Transaction Count
monthly_tx = (
    df.groupby(pd.Grouper(key="TransactionDate", freq="M"))["TransactionID"]
    .count()
    .reset_index()
)
fig = px.line(
    monthly_tx,
    x="TransactionDate",
    y="TransactionID",
    title="Monthly Transaction Count",
    markers=True,
)
st.plotly_chart(fig, use_container_width=True)

# 11️⃣ Revenue Distribution
fig = px.histogram(df, x="TotalAmount", nbins=30, title="Revenue Distribution")
st.plotly_chart(fig, use_container_width=True)

# 12️⃣ Quantity Distribution
fig = px.histogram(df, x="Quantity", nbins=30, title="Quantity Distribution")
st.plotly_chart(fig, use_container_width=True)

# 13️⃣ Revenue by Payment Method (Bar)
payment_rev = df.groupby("PaymentMethod")["TotalAmount"].sum().reset_index()
fig = px.bar(
    payment_rev, x="PaymentMethod", y="TotalAmount", title="Revenue by Payment Method"
)
st.plotly_chart(fig, use_container_width=True)

# 14️⃣ Top 10 Countries by Transactions
country_tx = (
    df.groupby("Country")["TransactionID"]
    .count()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
fig = px.bar(
    country_tx, x="Country", y="TransactionID", title="Top 10 Countries by Transactions"
)
st.plotly_chart(fig, use_container_width=True)

# 15️⃣ Customer Revenue Boxplot
customer_rev = df.groupby("CustomerID")["TotalAmount"].sum().reset_index()
fig = px.box(customer_rev, y="TotalAmount", title="Customer Revenue Distribution")
st.plotly_chart(fig, use_container_width=True)
