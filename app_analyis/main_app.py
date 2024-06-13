import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the dataset
file_path = '/workspaces/analysis/app_analyis/df.csv'
df = pd.read_csv(file_path)

# Streamlit App
def main():
    # Set page config
    st.set_page_config(
        page_title="Laptop Analysis Dashboard",
        page_icon="💻",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    pages = {
        "Home": home,
        "Data Overview": data_overview,
        "Brand Analysis": brand_analysis,
        "Price Analysis": price_analysis,
        "Performance Analysis": performance_analysis,
        "Display and Design Analysis": display_design_analysis,
        "Additional Insights": additional_insights,
        "Conclusion and Recommendations": conclusion_recommendations,
    }
    
    choice = st.sidebar.selectbox("Select a page", list(pages.keys()))
    page = pages[choice]
    page()

def home():
    st.title("Laptop Analysis Dashboard")
    st.write("Welcome to the Laptop Analysis Dashboard. Use the navigation bar to explore different insights.")
    
    # Overview of the dataset
    st.subheader("Dataset Overview")
    st.write("Here's a quick look at the first few rows of the dataset:")
    st.write(df.head())

    # Plotly Chart
    st.subheader("Price Distribution by Brand")
    fig = px.box(df, x="Brand", y="Price", title="Price Distribution by Brand",
                 labels={"Price": "Price in Rupees", "Brand": "Laptop Brand"})
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig, use_container_width=True)

    # Top 5 Laptops by Highest Price
    st.subheader("Top 5 Laptops by Highest Price")
    top_5_df = df[['Brand', 'Spec_Score', 'Series', 'Price']].sort_values(by='Price', ascending=False).head()
    fig_table = go.Figure(data=[go.Table(
        columnwidth=[80, 80, 80, 80],
        header=dict(values=list(top_5_df.columns),
                    fill_color='gray',
                    font=dict(color='white', size=12),
                    align='center'),
        cells=dict(values=[top_5_df.Brand, top_5_df.Spec_Score, top_5_df.Series, top_5_df.Price],
                fill_color='lightgray',
                font=dict(color='black', size=11),
                align='center'))
    ])
    fig_table.update_layout(
        width=800,  # Adjust width as needed
        height=200,  # Adjust height as needed
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="#1E1E1E",  # Background color to match the main background
        plot_bgcolor="#1E1E1E"
    )
    st.plotly_chart(fig_table, use_container_width=True)

    # Average Price by Brand
    avg_price_by_brand = df.groupby('Brand')['Price'].mean().reset_index()
    fig_avg_price = px.bar(avg_price_by_brand, x='Brand', y='Price', color='Brand',
                        title="Average Price by Brand",
                        labels={"Price": "Average Price in Rupees", "Brand": "Laptop Brand"})
    fig_avg_price.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_avg_price, use_container_width=True)



    # Background color styling
    st.markdown(
        """
        <style>
        .main {
            background-color: #1E1E1E;
            color: white;
        }
        .css-18e3th9 {
            color: white;
        }
        .css-1d391kg {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def data_overview():
    st.title("Data Overview")
    
    # Dataset Summary
    st.subheader("Dataset Summary")
    st.write(df.describe())

    # Brand Distribution
    st.subheader("Brand Distribution")
    brand_counts = df['Brand'].value_counts().reset_index()
    brand_counts.columns = ['Brand', 'Count']
    fig_bar_brand = px.bar(brand_counts, x='Brand', y='Count', 
                           title="Number of Laptops per Brand", 
                           labels={"Brand": "Brand", "Count": "Count"})
    fig_bar_brand.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_bar_brand, use_container_width=True)

    # Side-by-Side Pie Charts

    st.subheader("Brand Market Share")
    top_5_brands = brand_counts.nlargest(5, 'Count')
    Other_Brands = brand_counts.iloc[5:]

    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                        subplot_titles=('Top 5 Brands', 'Other Brands'))

    # Top 5 brands pie chart
    fig.add_trace(go.Pie(labels=top_5_brands['Brand'], values=top_5_brands['Count'], name="Top 5 Brands"),
                  row=1, col=1)

    # Remaining brands pie chart
    fig.add_trace(go.Pie(labels=Other_Brands['Brand'], values=Other_Brands['Count'], name="Other Brands"),
                  row=1, col=2)

    fig.update_layout(
        title_text="Market Share of Laptop Brands",
        annotations=[dict(text='Top 5 Brands', x=0.18, y=0.5, font_size=15, showarrow=False),
                     dict(text='Other Brands', x=0.82, y=0.5, font_size=15, showarrow=False)],
        paper_bgcolor="rgba(0, 0, 0, 0)",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )

    st.plotly_chart(fig, use_container_width=True)


# Brand Analysis
def brand_analysis():
    st.title("Brand Analysis")
    
    # Dropdown for selecting brand
    brand_list = df['Brand'].unique().tolist()
    selected_brand = st.selectbox("Select a Brand", brand_list)
    
    # Dropdown for selecting sort order
    sort_order = st.radio("Select Price Order", ('Ascending', 'Descending'))
    ascending_order = True if sort_order == 'Ascending' else False
    
    # Filter the dataframe based on the selected brand
    brand_data = df[df['Brand'] == selected_brand]
    
    # Sort the dataframe based on the selected order
    brand_data = brand_data.sort_values(by='Price', ascending=ascending_order)
    
    # Display Brand Details
    st.subheader(f"Details for {selected_brand}")

    # Table with Spec Score, Series, Price Range, Utility, and Price
    # Table with Spec Score, Series, Price Range, Utility, and Price
    st.subheader(f"{selected_brand} Laptop Details")
    st.dataframe(brand_data[['Spec_Score', 'Series', 'Price_Range', 'Utility', 'Price']])
    
    # Average Price for the selected brand
    avg_price = brand_data['Price'].mean()
    st.write(f"Average Price: Rs.{avg_price:.2f}")
    
    # Average Spec Score for the selected brand
    avg_spec_score = brand_data['Spec_Score'].mean()
    st.write(f"Average Spec Score: {avg_spec_score:.2f}")

    # Spec Score Distribution for the selected brand
    st.subheader("Spec Score Distribution")
    fig_spec_score = px.box(brand_data, y='Spec_Score', color='Brand',
                            title=f"Spec Score Distribution for {selected_brand}",
                            labels={"Spec_Score": "Specification Score", "Brand": "Laptop Brand"})
    fig_spec_score.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_spec_score, use_container_width=True)
    
    # Price vs. Spec Score for the selected brand
    st.subheader("Price vs. Spec Score")
    fig_price_spec = px.scatter(brand_data, x='Spec_Score', y='Price', color='Series',
                                title=f"Price vs. Spec Score for {selected_brand}",
                                labels={"Spec_Score": "Specification Score", "Price": "Price in USD", "Series": "Laptop Series"})
    fig_price_spec.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_price_spec, use_container_width=True)
    
    




def price_analysis():
    st.title("Price Analysis")
    st.write("This page will display a price analysis of laptops.")
    # Add more code for price analysis here

def performance_analysis():
    st.title("Performance Analysis")
    st.write("This page will display a performance analysis of laptops.")
    # Add more code for performance analysis here

def display_design_analysis():
    st.title("Display and Design Analysis")
    st.write("This page will display an analysis of display and design features.")
    # Add more code for display and design analysis here

def additional_insights():
    st.title("Additional Insights")
    st.write("This page will display additional insights from the data.")
    # Add more code for additional insights here

def conclusion_recommendations():
    st.title("Conclusion and Recommendations")
    st.write("This page will display conclusions and recommendations based on the analysis.")
    # Add more code for conclusions and recommendations here

if __name__ == "__main__":
    main()
