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

# Price_Analysis

def price_analysis():
    st.title("Price Analysis")

    # Price Distribution
    st.subheader("Price Distribution")
    fig_price_dist = px.histogram(df, x='Price', nbins=30, color='Brand',
                                  title="Distribution of Laptop Prices",
                                  labels={"Price": "Price in USD", "Brand": "Laptop Brand"})
    fig_price_dist.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_price_dist, use_container_width=True)

    # Price vs. Spec Score
    st.subheader("Price vs. Spec Score")
    fig_price_spec = px.scatter(df, x="Spec_Score", y="Price", color="Brand",
                                title="Price vs. Spec Score",
                                labels={"Spec_Score": "Specification Score", "Price": "Price in USD", "Brand": "Laptop Brand"})
    fig_price_spec.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_price_spec, use_container_width=True)

    # Price Range Distribution
    st.subheader("Price Range Distribution")
    price_range_counts = df['Price_Range'].value_counts().reset_index()
    price_range_counts.columns = ['Price_Range', 'Count']
    fig_price_range = px.bar(price_range_counts, x='Price_Range', y='Count', 
                             title="Number of Laptops per Price Range", 
                             labels={"Price_Range": "Price Range", "Count": "Count"})
    fig_price_range.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_price_range, use_container_width=True)

    # Top 10 Most Expensive Laptops
    st.subheader("Top 10 Most Expensive Laptops")
    top_10_expensive = df.nlargest(10, 'Price')
    fig_top_10 = px.bar(top_10_expensive, x='Series', y='Price', color='Brand',
                        title="Top 10 Most Expensive Laptops",
                        labels={"Series": "Laptop Series", "Price": "Price in Rupees", "Brand": "Laptop Brand"})
    fig_top_10.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_top_10, use_container_width=True)

    # Price Distribution by Utility
    st.subheader("Price Distribution by Utility")
    fig_price_utility = px.box(df, x='Utility', y='Price', color='Utility',
                               title="Price Distribution by Utility",
                               labels={"Utility": "Utility", "Price": "Price in Rupees"})
    fig_price_utility.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_price_utility, use_container_width=True)

    # Price vs. RAM Capacity
    st.subheader("Price vs. RAM Capacity")
    fig_price_ram = px.scatter(df, x='Ram_Capacity(GB)', y='Price', color='Brand',
                               title="Price vs. RAM Capacity",
                               labels={"Ram_Capacity(GB)": "RAM Capacity (GB)", "Price": "Price in Rupees", "Brand": "Laptop Brand"})
    fig_price_ram.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_price_ram, use_container_width=True)

# Performane Analysis

def performance_analysis():
    st.title("Performance Analysis")

    # Spec Score Distribution
    st.subheader("Spec Score Distribution")
    fig_spec_dist = px.histogram(df, x='Spec_Score', nbins=30, color='Brand',
                                 title="Distribution of Specification Scores",
                                 labels={"Spec_Score": "Specification Score", "Brand": "Laptop Brand"})
    fig_spec_dist.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_spec_dist, use_container_width=True)

    # Top 10 Laptops by Spec Score
    st.subheader("Top 10 Laptops by Spec Score")
    top_10_spec = df.nlargest(10, 'Spec_Score')
    fig_top_10_spec = px.bar(top_10_spec, x='Series', y='Spec_Score', color='Brand',
                             title="Top 10 Laptops by Specification Score",
                             labels={"Series": "Laptop Series", "Spec_Score": "Specification Score", "Brand": "Laptop Brand"})
    fig_top_10_spec.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_top_10_spec, use_container_width=True)

    # Spec Score vs. RAM Capacity
    st.subheader("Spec Score vs. RAM Capacity")
    fig_spec_ram = px.scatter(df, x='Ram_Capacity(GB)', y='Spec_Score', color='Brand',
                              title="Specification Score vs. RAM Capacity",
                              labels={"Ram_Capacity(GB)": "RAM Capacity (GB)", "Spec_Score": "Specification Score", "Brand": "Laptop Brand"})
    fig_spec_ram.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_spec_ram, use_container_width=True)

# display design analysis

def display_design_analysis():
    st.title("Display and Design Analysis")

    # Screen Size Distribution
    st.subheader("Screen Size Distribution")
    fig_screen_size_dist = px.histogram(df, x='Display Size (Inches)', nbins=20, color='Brand',
                                        title="Distribution of Screen Sizes",
                                        labels={"Display Size (Inches)": "Screen Size (inches)", "Brand": "Laptop Brand"})
    fig_screen_size_dist.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_screen_size_dist, use_container_width=True)

    # Resolution Distribution
    st.subheader("Resolution Distribution")
    df['Resolution'] = df['Resolution Width'].astype(str) + 'x' + df['Resolution Height'].astype(str)
    resolution_counts = df['Resolution'].value_counts().reset_index()
    resolution_counts.columns = ['Resolution', 'Count']
    fig_resolution_dist = px.bar(resolution_counts, x='Resolution', y='Count', color='Resolution',
                                 title="Distribution of Screen Resolutions",
                                 labels={"Resolution": "Screen Resolution", "Count": "Count"})
    fig_resolution_dist.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_resolution_dist, use_container_width=True)

    # PPI vs. Price
    st.subheader("PPI vs. Price")
    fig_ppi_price = px.scatter(df, x='PPI', y='Price', color='Brand',
                               title="PPI vs. Price",
                               labels={"PPI": "Pixels Per Inch (PPI)", "Price": "Price in Rupees", "Brand": "Laptop Brand"})
    fig_ppi_price.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_ppi_price, use_container_width=True)



def additional_insights():
    st.title("Additional Insights")

    # Operating System Distribution
    st.subheader("Operating System Distribution")
    os_counts = df['OS Type'].value_counts().reset_index()
    os_counts.columns = ['OS Type', 'Count']
    fig_os_dist = px.pie(os_counts, values='Count', names='OS Type',
                         title="Operating System Distribution")
    fig_os_dist.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_os_dist, use_container_width=True)

    # Graphics Brand Distribution
    st.subheader("Graphics Brand Distribution")
    graphics_counts = df['Graphics_Brand'].value_counts().reset_index()
    graphics_counts.columns = ['Graphics_Brand', 'Count']
    fig_graphics_dist = px.bar(graphics_counts, x='Graphics_Brand', y='Count', color='Graphics_Brand',
                               title="Graphics Brand Distribution",
                               labels={"Graphics_Brand": "Graphics Brand", "Count": "Count"})
    fig_graphics_dist.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_graphics_dist, use_container_width=True)

    # Weight vs. Price
    st.subheader("Weight vs. Price")
    fig_weight_price = px.scatter(df, x='Weight(kg)', y='Price', color='Brand',
                                  title="Weight vs. Price",
                                  labels={"Weight(kg)": "Weight (kg)", "Price": "Price in USD", "Brand": "Laptop Brand"})
    fig_weight_price.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig_weight_price, use_container_width=True)


def conclusion_recommendations():
    st.title("Conclusion and Recommendations")

    st.subheader("Key Findings")
    st.write("""
    Based on the analyses conducted in the previous sections, here are some key findings:
    
    1. **Price Analysis**:
       - The average price of laptops varies significantly across different brands.
       - High-end laptops tend to have higher specification scores and better performance metrics.
       - The top 10 most expensive laptops are dominated by a few brands, indicating brand influence on pricing.

    2. **Performance Analysis**:
       - Specification scores vary widely across brands and models.
       - There is a positive correlation between RAM capacity and specification scores.
       - The top 10 laptops by specification scores provide high performance and are generally more expensive.

    3. **Display and Design Analysis**:
       - Screen sizes and resolutions vary across different brands and models.
       - Higher PPI (Pixels Per Inch) tends to correlate with higher prices.
       - The distribution of screen sizes and resolutions indicates preferences for certain standards among brands.

    4. **Additional Insights**:
       - The distribution of operating systems shows a preference for certain OS types among laptop users.
       - Graphics brand distribution highlights the dominance of a few key players in the market.
       - Weight is an important factor influencing the price of laptops, with lighter laptops generally being more expensive.
    """)

    st.subheader("Recommendations")
    st.write("""
    Based on the key findings, here are some actionable recommendations for stakeholders:

    1. **Pricing Strategy**:
       - Focus on optimizing the pricing of high-specification models to target high-end consumers.
       - Consider introducing mid-range models with balanced specifications and competitive pricing to capture a larger market share.

    2. **Product Development**:
       - Invest in improving RAM capacity and overall performance metrics to meet the demand for high-performance laptops.
       - Develop models with diverse screen sizes and high PPI to cater to various consumer preferences.

    3. **Marketing and Sales**:
       - Highlight the unique features and specifications of high-end models in marketing campaigns to justify the premium pricing.
       - Promote laptops with popular operating systems and graphics brands to align with consumer preferences.

    4. **Supply Chain and Inventory Management**:
       - Monitor the demand for different specifications and adjust production volumes accordingly to avoid overstocking or stockouts.
       - Ensure a steady supply of components from key graphics and operating system vendors to maintain product availability.
    """)

    st.subheader("Next Steps")
    st.write("""
    Moving forward, consider the following steps to further enhance the laptop portfolio and business strategy:

    1. **Customer Feedback**:
       - Gather and analyze customer feedback to identify areas for improvement in existing models and develop new features that meet consumer needs.

    2. **Market Research**:
       - Conduct ongoing market research to stay updated on industry trends and competitor strategies.

    3. **Innovation**:
       - Invest in research and development to introduce innovative features and technologies that differentiate your products from competitors.
    """)


if __name__ == "__main__":
    main()
