# Import required libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Set up custom styles for a colorful app
st.markdown(
    """
    <style>
    .main-title {
        color: #1f77b4;
        font-size: 36px;
        font-weight: bold;
    }
    .sub-title {
        color: #ff7f0e;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }
    .info-text {
        color: #2ca02c;
        font-size: 18px;
    }
    .footer-text {
        color: #9467bd;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 1.0 Title and Introduction
st.markdown("<h1 class='main-title'>Business Dashboard</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='info-text'>This dashboard provides insights into sales, customer demographics, and product performance. Upload your data to get started!</p>",
    unsafe_allow_html=True,
)

# 2.0 Data Input
st.markdown("<h2 class='sub-title'>Upload Business Data</h2>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose a CSV File", type="csv", accept_multiple_files=False)

# 3.0 App Body: Processing Data
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("### Preview of the Uploaded Data:")
    st.dataframe(data.head())

    # Sales insights
    st.markdown("<h2 class='sub-title'>Sales Insights</h2>", unsafe_allow_html=True)
    if 'sales_date' in data.columns and 'sales_amount' in data.columns:
        st.write("**Sales Over Time**")
        fig = px.line(
            data,
            x='sales_date',
            y='sales_amount',
            title='Sales Over Time',
            line_shape='spline',
            markers=True,
            color_discrete_sequence=['#1f77b4'],
        )
        st.plotly_chart(fig)
    else:
        st.warning("Please ensure your data has 'sales_date' and 'sales_amount' columns for sales visualization.")

    # Customer Segmentation by Region
    st.markdown("<h2 class='sub-title'>Customer Segmentation</h2>", unsafe_allow_html=True)
    if 'region' in data.columns and 'sales_amount' in data.columns:
        st.write("**Customer Segmentation by Region**")
        fig = px.pie(
            data,
            names="region",
            values='sales_amount',
            title='Sales by Region',
            color_discrete_sequence=px.colors.sequential.Plasma,
        )
        st.plotly_chart(fig)
    else:
        st.warning("Please ensure your data has a 'region' column for customer segmentation.")

    # Product Analysis
    st.markdown("<h2 class='sub-title'>Product Analysis</h2>", unsafe_allow_html=True)
    if 'product' in data.columns and 'sales_amount' in data.columns:
        st.write("**Top Products by Sales**")
        top_products_df = data.groupby('product').sum(numeric_only=True).nlargest(10, 'sales_amount')
        fig = px.bar(
            top_products_df,
            x=top_products_df.index,
            y='sales_amount',
            title="Top Products By Sales",
            text_auto=True,
            color_discrete_sequence=['#ff7f0e'],
        )
        st.plotly_chart(fig)
    else:
        st.warning("Please ensure your data has 'product' and 'sales_amount' columns for product analysis.")

    # Feedback Form
    st.markdown("<h2 class='sub-title'>Feedback (Your Opinion Counts)</h2>", unsafe_allow_html=True)
    feedback = st.text_area("Please provide any feedback or suggestions.")
    if st.button("Submit Feedback"):
        st.success('Thank you for your feedback!')

# 4.0 Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p class='footer-text'>This business dashboard template is flexible. Expand upon it based on your specific business needs.</p>",
    unsafe_allow_html=True,
)

if __name__ == "__main__":
    pass
