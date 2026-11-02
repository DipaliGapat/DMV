DMV Practical 07
================================================================================

# --- Code cell 1 ---
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# --- Code cell 2 ---
df = pd.read_csv(r"C:\Users\dipal\OneDrive\Desktop\DMV Practicals\sales_data_sample.csv",encoding="latin-1")
df1 = pd.read_excel(r"C:\Users\dipal\OneDrive\Desktop\DMV Practicals\Sales.xlsx")
df2 = pd.read_json(r"C:\Users\dipal\OneDrive\Desktop\DMV Practicals\sales.json")

# --- Code cell 3 ---
df

# --- Code cell 4 ---
df1

# --- Code cell 5 ---
df2

# --- Code cell 6 ---
df.head()

# --- Code cell 7 ---
df1.head()

# --- Code cell 8 ---
df2.head()

# --- Code cell 9 ---
df.shape

# --- Code cell 10 ---
df1.shape

# --- Code cell 11 ---
df2.shape

# --- Code cell 12 ---
df.describe()

# --- Code cell 13 ---
df1.describe()

# --- Code cell 14 ---
df2.describe()

# --- Code cell 15 ---
df.info()

# --- Code cell 16 ---
df1.info

# --- Code cell 17 ---
df2.info

# --- Code cell 18 ---
df.isna()

# --- Code cell 19 ---
df.isna().sum()

# --- Code cell 20 ---
df.describe()

# --- Code cell 21 ---
print("Duplicate Rows:", df.duplicated().sum())

# --- Code cell 22 ---
df.duplicated().sum()

# --- Code cell 23 ---
df[df.duplicated()]

# --- Code cell 24 ---
df.drop_duplicates(inplace=True)

# --- Code cell 25 ---
df.nunique()

# --- Code cell 26 ---
df['ORDERNUMBER'].unique()

# --- Code cell 27 ---
df['ORDERNUMBER'].value_counts()

# --- Code cell 28 ---
df[df.isnull().any(axis=1)]

# --- Code cell 29 ---
df.dtypes

# --- Code cell 30 ---
df.fillna(df.mean(numeric_only=True), inplace=True)

# --- Code cell 31 ---

df.fillna("5", inplace=True)

# --- Code cell 32 ---
df

# --- Code cell 33 ---
df.isna().sum()

# --- Code cell 34 ---
df.dropna(inplace=True)

# --- Code cell 35 ---
df.isna().sum()

# --- Code cell 36 ---
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# --- Code cell 37 ---
df.columns = df.columns.str.lower()

# --- Code cell 38 ---
df.columns

# --- Code cell 39 ---
df['state'] = df['state'].str.upper()

# --- Code cell 40 ---
df

# --- Code cell 41 ---
df.drop_duplicates(inplace=True)

# --- Code cell 42 ---
print(df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())
print(df.info())

# --- Code cell 43 ---
unified_df = pd.concat(
    [df,df1,df2],
    ignore_index=True
)

print(unified_df.head())

# --- Code cell 44 ---
print(unified_df.shape)
print(unified_df.info())

# --- Code cell 45 ---
unified_df.to_csv("unified_sales_data.csv", index=False)

# --- Code cell 46 ---
unified_df['sales'].sum()  

# --- Code cell 47 ---
unified_df['sales'].mean()    

# --- Code cell 48 ---
df.head()

# --- Code cell 49 ---
df.describe()

# --- Code cell 50 ---

print(unified_df.columns.tolist())

# --- Code cell 51 ---
df['Total_Sales'] = df['quantityordered'] * df['priceeach']

# --- Code cell 52 ---
total_sales = df['Total_Sales'].sum()
print("\nTotal Sales:", total_sales)

# --- Code cell 53 ---
average_order_value = df['Total_Sales'].mean()
print("Average Order Value:", average_order_value)

# --- Code cell 54 ---
category_sales = df.groupby('ordernumber')['Total_Sales'].sum()

# --- Code cell 55 ---
print("\nSales by ORDERNUMBER:")
print(category_sales)

# --- Code cell 56 ---
category_distribution = df['ordernumber'].value_counts()

print("\nProduct Category Distribution:")
print(category_distribution)

# --- Code cell 57 ---
average_category_sales = df.groupby('ordernumber')['Total_Sales'].mean()

print("\nAverage Sales by Category:")
print(average_category_sales)

# --- Code cell 58 ---
orders_per_category = df.groupby('ordernumber').size()

print("\nOrders per Category:")
print(orders_per_category)

# --- Code cell 59 ---
product_sales = df.groupby("ordernumber")["sales"].sum()

product_sales = product_sales.head(10)

plt.figure(figsize=(10,6))
product_sales.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title("Sales of First 10 Order Numbers")
plt.xlabel("Order Number")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# --- Code cell 60 ---
df

# --- Code cell 61 ---
product_sales = df.groupby("ordernumber")["sales"].sum()

# Top 10 products
product_sales = product_sales.sort_values(ascending=False).head(10)

plt.figure(figsize=(8,8))
plt.pie(product_sales,
        labels=product_sales.index,
        autopct='%1.1f%%',
        startangle=90)

plt.title("Top 10 Products by Sales")
plt.axis('equal')
plt.show()

# --- Code cell 62 ---
sales_data = df["sales"].head(80)

plt.figure(figsize=(8,6))
plt.boxplot(sales_data)

plt.title("Box Plot of First 80 Sales Records")
plt.ylabel("Sales")

plt.show()

# --- Code cell 63 ---
country_sales = df.groupby("city")["sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
country_sales.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title("Top 10 CITIES by Sales")
plt.xlabel("CITY")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# --- Code cell 64 ---
customer_orders = df["contactlastname"].value_counts().head(10)

plt.figure(figsize=(10,5))
customer_orders.plot(kind="bar")

plt.title("Top 10 Customers by Number of Orders")
plt.xlabel("Customer")
plt.ylabel("Orders")

plt.show()

# --- Code cell 65 ---
quantity = df.groupby("ordernumber")["quantityordered"].sum()

top10_quantity = quantity.sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top10_quantity.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title("Top 10 Order Numbers by Quantity Sold")
plt.xlabel("Order Number")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# --- Code cell 66 ---
sales_data = df["sales"].head(10)

plt.figure(figsize=(8,5))
plt.hist(sales_data, bins=5, color='skyblue', edgecolor='black')

plt.title("Sales Distribution (First 10 Records)")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# --- Code cell 67 ---
plt.figure(figsize=(8,6))

plt.scatter(df["quantityordered"], df["sales"])

plt.title("Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")

plt.show()

# --- Code cell 68 ---
quantity = df["quantityordered"].head(10)
sales = df["sales"].head(10)

# Create scatter plot
plt.figure(figsize=(8,6))
plt.scatter(quantity, sales, color='blue')

plt.title("Sales vs Quantity (First 10 Records)")
plt.xlabel("Quantity Ordered")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

# --- Code cell 69 ---
df

# --- Code cell 70 ---
df["orderdate"] = pd.to_datetime(df["orderdate"])

df["Month"] = df["orderdate"].dt.month_name()

monthly_sales = df.groupby("orderdate")["sales"].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)
plt.show()

# --- Code cell 71 ---
df4=pd.read_csv("Sales_April_2019.csv")
df5=pd.read_csv("Sales_August_2019.csv")

# --- Code cell 72 ---
df4

# --- Code cell 73 ---
df5

# --- Code cell 74 ---
merged_df = pd.concat([df4, df5], ignore_index=True)

print(merged_df.head())
print(merged_df.shape)

# --- Code cell 75 ---
merged_df[['Street', 'City', 'State_Zip']] = merged_df['Purchase Address'].str.split(',', expand=True)

merged_df[['State', 'Zip Code']] = merged_df['State_Zip'].str.strip().str.split(' ', n=1, expand=True)

merged_df[['Purchase Address', 'Street', 'City', 'State', 'Zip Code']].head()

# --- Code cell 76 ---
merged_df['Quantity Ordered'] = pd.to_numeric(merged_df['Quantity Ordered'], errors='coerce')
merged_df['Price Each'] = pd.to_numeric(merged_df['Price Each'], errors='coerce')

merged_df = merged_df.dropna(subset=['Quantity Ordered', 'Price Each'])

# --- Code cell 77 ---
merged_df['Total Sales'] = merged_df['Quantity Ordered'] * merged_df['Price Each']

print(merged_df[['Product', 'Quantity Ordered', 'Price Each', 'Total Sales']].head())

# --- Code cell 78 ---
merged_df['Order Date'] = pd.to_datetime(
    merged_df['Order Date'],
    format='mixed'
)

merged_df['Month'] = merged_df['Order Date'].dt.month_name()

print(merged_df[['Order Date', 'Month']].head())

# --- Code cell 79 ---
merged_df['Sales Category'] = merged_df['Total Sales'].apply(
    lambda x: 'High' if x >= 500 else 'Low'
)

merged_df[['Total Sales','Sales Category']].head()

# --- Code cell 80 ---
merged_df['Discounted Sales'] = merged_df['Total Sales'] * 0.90

merged_df[['Total Sales','Discounted Sales']].head()

# --- Code cell 81 ---
merged_df

# --- Code cell 82 ---
print(merged_df.head())
================================================================================
DMV Practical 08
================================================================================

# --- Code cell 1 ---
pip install folium

# --- Code cell 2 ---
import requests
import pandas as pd
import matplotlib.pyplot as plt
import folium

# --- Code cell 3 ---
api_key = "[REDACTED_API_KEY]"

# --- Code cell 4 ---
base_url = "http://api.openweathermap.org/data/2.5/forecast"
city_name = "New York"
params = {
"q": city_name,
"appid": api_key,
"units": "metric"
}
response = requests.get(base_url, params=params)
data = response.json()

# --- Code cell 5 ---
response

# --- Code cell 6 ---
data

# --- Code cell 7 ---
weather_data = data["list"]
timestamps = [entry["dt"] for entry in weather_data]
temperatures = [entry["main"]["temp"] for entry in weather_data]
humidity = [entry["main"]["humidity"] for entry in weather_data]
wind_speed = [entry["wind"]["speed"] for entry in weather_data]
weather_description = [item['weather'][0]['description'] for item in weather_data]

# --- Code cell 8 ---
weather_data

# --- Code cell 9 ---
datetime_objects = [pd.to_datetime(timestamp, unit="s") for timestamp in timestamps]

# --- Code cell 10 ---
weather_df = pd.DataFrame({
'Timestamp': timestamps,
"Datetime": datetime_objects,
'Temperature': temperatures,
'humidity': humidity,
'wind_speed': wind_speed,
'weather_description': weather_description,
})

# --- Code cell 11 ---
weather_df.set_index("Datetime", inplace=True)

# --- Code cell 12 ---
weather_df

# --- Code cell 13 ---
precipitation = []

for entry in weather_data:
    rain = entry.get("rain", {}).get("3h", 0)
    snow = entry.get("snow", {}).get("3h", 0)
    total_precipitation = rain + snow
    precipitation.append(total_precipitation)

# Display the precipitation values
print(precipitation)

# --- Code cell 14 ---
avg_temp = sum(temperatures) / len(temperatures)
avg_temp

# --- Code cell 15 ---
max_temp = max(temperatures)
max_temp

# --- Code cell 16 ---
min_temp = min(temperatures)
min_temp

# --- Code cell 17 ---
import matplotlib.pyplot as plt
daily_mean_temp = weather_df['Temperature'].resample('D').mean()
daily_mean_humidity = weather_df['humidity'].resample('D').mean()
daily_mean_wind_speed = weather_df['wind_speed'].resample('D').mean()

# --- Code cell 18 ---
plt.figure(figsize=(10, 6))
daily_mean_temp.plot(color='red', linestyle='-', marker='o')
plt.title('Mean Daily Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# --- Code cell 19 ---
plt.figure(figsize=(10, 6))
daily_mean_humidity.plot(kind='bar', color='blue')
plt.title('Mean Daily Humidity')
plt.xlabel('Date')

plt.ylabel('Humidity (%)')
plt.grid(True)
plt.show()

# --- Code cell 20 ---
plt.figure(figsize=(10, 6))
plt.scatter(weather_df['Temperature'], weather_df['wind_speed'], color='green')
plt.title('Temperature vs. Wind Speed')
plt.xlabel('Temperature (°C)')
plt.ylabel('Wind Speed (m/s)')
plt.grid(True)
plt.show()

# --- Code cell 21 ---
plt.figure(figsize=(10, 6))
plt.plot(timestamps, temperatures, label="Temperature (°C)")
plt.plot(timestamps, precipitation, label="Precipitation")
plt.xlabel("Timestamp")
plt.ylabel("Value")
plt.title("Weather Data for {}".format(city_name))
plt.legend()
plt.show()

# --- Code cell 22 ---
import seaborn as sns

# --- Code cell 23 ---
heatmap_data = weather_df[['Temperature', 'humidity']]
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm')
plt.title('Temperature vs Humidity Heatmap')
plt.show()
plt.scatter(weather_df['Temperature'], weather_df['humidity'])
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.title('Temperature vs Humidity Scatter Plot')
plt.show()

# --- Code cell 24 ---
import requests
import pandas as pd

API_KEY = "[REDACTED_API_KEY]"
locations = ['London', 'Paris', 'New York']
weather_list = []
for location in locations:
    api_url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(api_url)
    data = response.json()
    if response.status_code == 200:
        forecast = data["list"][0]
        temperature = forecast["main"]["temp"]
        humidity = forecast["main"]["humidity"]
        wind_speed = forecast["wind"]["speed"]
        latitude = data["city"]["coord"]["lat"]
        longitude = data["city"]["coord"]["lon"]
        weather_list.append({
            "Location": location,
            "Temperature (°C)": temperature,
            "Humidity (%)": humidity,
            "Wind Speed (m/s)": wind_speed,
            "Latitude": latitude,
            "Longitude": longitude
        })
    else:
        print(f"Error for {location}: {data.get('message')}")
weather_df = pd.DataFrame(weather_list)
print(weather_df)

# --- Code cell 25 ---
latitude = data.get("coord", {}).get("lat", 0)
longitude = data.get("coord", {}).get("lon", 0)

weather_map = folium.Map(location=[latitude, longitude], zoom_start=10)

for index, row in weather_df.iterrows():
  location_name = row['Location']
  latitude = row['Latitude']
  longitude = row['Longitude']
  folium.Marker([latitude, longitude], popup=location_name).add_to(weather_map)

# --- Code cell 26 ---
weather_map

# --- Code cell 27 ---
folium.Marker([latitude, longitude], popup=city_name).add_to(weather_map)
weather_map.save("weather_map.html")
================================================================================
DMV Practical 09
================================================================================

# --- Code cell 1 ---
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn import metrics
import matplotlib.pyplot as plt

# --- Code cell 2 ---
df= pd.read_csv("Telecom.csv")

# --- Code cell 3 ---
df.head()

# --- Code cell 4 ---
df

# --- Code cell 5 ---
df.info()

# --- Code cell 6 ---
df.shape

# --- Code cell 7 ---
df.columns

# --- Code cell 8 ---
df.describe()

# --- Code cell 9 ---
df.isnull().sum()

# --- Code cell 10 ---
num_cols = df.select_dtypes(include=['int64','float64']).columns

for col in num_cols:
    df[col] = df[col].fillna(df[col].mean())

# --- Code cell 11 ---
cat_cols = df.select_dtypes(include='object').columns

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# --- Code cell 12 ---
df.isnull().sum()

# --- Code cell 13 ---
df.duplicated().sum()

# --- Code cell 14 ---
df = df.drop_duplicates()

# --- Code cell 15 ---
for col in cat_cols:
    df[col] = df[col].str.strip()

# --- Code cell 16 ---
for col in cat_cols:
    df[col] = df[col].str.lower()

# --- Code cell 17 ---
df

# --- Code cell 18 ---
for col in cat_cols:
    df[col] = df[col].str.upper()

# --- Code cell 19 ---
df

# --- Code cell 20 ---
df.dtypes 

# --- Code cell 21 ---
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# --- Code cell 22 ---
df["Churn"] = df["Churn"].map({"YES":1,"NO":0})

# --- Code cell 23 ---
df.dtypes

# --- Code cell 24 ---
df

# --- Code cell 25 ---
num_cols = df.select_dtypes(include=np.number).columns 

# --- Code cell 26 ---
for col in num_cols:
    plt.figure(figsize=(5,3))
    plt.boxplot(df[col].dropna())
    plt.title(col)
    plt.show()

# --- Code cell 27 ---
for col in num_cols:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[(df[col] >= lower) & (df[col] <= upper)]

# --- Code cell 28 ---
for col in num_cols:
    plt.figure(figsize=(5,3))
    plt.boxplot(df[col].dropna())
    plt.title(col)
    plt.show()

# --- Code cell 29 ---
df["Charge_per_Tenure"] = df["MonthlyCharges"] / (df["tenure"] + 1)

# --- Code cell 30 ---
services = [
    "PhoneService",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies"
]

df["TotalServices"] = df[services].apply(lambda x: (x=="yes").sum(), axis=1)

# --- Code cell 31 ---
df

# --- Code cell 32 ---
df = pd.get_dummies(df, drop_first=True)

# --- Code cell 33 ---
df

# --- Code cell 34 ---
from sklearn.preprocessing import MinMaxScaler

# --- Code cell 35 ---
scaler = MinMaxScaler() 

# --- Code cell 36 ---
num_cols = df.select_dtypes(include=np.number).columns

df[num_cols] = scaler.fit_transform(df[num_cols])

# --- Code cell 37 ---
from sklearn.model_selection import train_test_split

# --- Code cell 38 ---
X = df.drop("Churn", axis=1)
y = df["Churn"]

# --- Code cell 39 ---
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42           
)

# --- Code cell 40 ---
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)    

# --- Code cell 41 ---
df.to_csv("Telecom_Customer_Churn_Cleaned.csv", index=False)

# --- Code cell 42 ---
df
================================================================================
DMV Practical 10
================================================================================

# --- Code cell 1 ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Code cell 2 ---
df = pd.read_csv("Bengaluru_House_Data.csv")

# --- Code cell 3 ---
df

# --- Code cell 4 ---
df.head()

# --- Code cell 5 ---
df.info()

# --- Code cell 6 ---
df.shape

# --- Code cell 7 ---
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(" ", "_")
df.columns = df.columns.str.replace("[^A-Za-z0-9_]", "", regex=True)

print(df.columns)

# --- Code cell 8 ---
df.isnull().sum()

# --- Code cell 9 ---
num_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in num_cols:
    df[col] = df[col].fillna(df[col].mean())

# --- Code cell 10 ---
cat_cols = df.select_dtypes(include=["object"]).columns

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# --- Code cell 11 ---
df = df.dropna()

# --- Code cell 12 ---
neighborhood = pd.read_csv("mumbai-house-price-data-cleaned-selected-columns.csv")

# --- Code cell 13 ---
merged_df = pd.merge(df, neighborhood, on="price", how="left")

merged_df.head()

# --- Code cell 14 ---
houses = neighborhood[neighborhood["property_type"] == "House"]

houses.head()

# --- Code cell 15 ---
pune = df[df["location"] == "Pune"]

pune.head()

# --- Code cell 16 ---
print(df.columns)

# --- Code cell 17 ---
print(neighborhood.columns)

# --- Code cell 18 ---
expensive = df[df["price"] > 5000000]

expensive.head()

# --- Code cell 19 ---
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

neighborhood["property_type"] = le.fit_transform(neighborhood["property_type"])

# --- Code cell 20 ---
df = pd.get_dummies(df, columns=["location"], drop_first=True)

df.head()
================================================================================
DMV Practical 11
================================================================================

# --- Code cell 1 ---
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("City_Air_Quality.csv")

df

# --- Code cell 2 ---
df.head()

# --- Code cell 3 ---
df.tail()

# --- Code cell 4 ---
df.shape

# --- Code cell 5 ---
df.columns

# --- Code cell 6 ---
df.info()

# --- Code cell 7 ---
df.describe()

# --- Code cell 8 ---
print(df.columns)

# --- Code cell 9 ---
df['Date'] = pd.to_datetime(df['Date'])

# --- Code cell 10 ---
df = df.sort_values('Date')

# --- Code cell 11 ---
plt.figure(figsize=(10,5))

plt.plot(df['Date'], df['AQI'], marker='o')

plt.xlabel('Date')
plt.ylabel('AQI')
plt.title('AQI Trend Over Time')

plt.xticks(rotation=45)
plt.grid(True)

plt.show()

# --- Code cell 12 ---
plt.plot(df['Date'], df['AQI'])

# --- Code cell 13 ---
plt.figure(figsize=(10,5))

plt.plot(df['Date'], df['PM2.5'], marker='o')

plt.xlabel('Date')
plt.ylabel('PM2.5')
plt.title('PM2.5 Trend Over Time')

plt.xticks(rotation=45)
plt.grid(True)

plt.show()

# --- Code cell 14 ---
plt.figure(figsize=(10,5))

plt.plot(df['Date'], df['PM10'], marker='o')

plt.xlabel('Date')
plt.ylabel('PM10')
plt.title('PM10 Trend Over Time')

plt.xticks(rotation=45)
plt.grid(True)

plt.show()

# --- Code cell 15 ---
plt.figure(figsize=(10,5))

plt.plot(df['Date'], df['CO'], marker='o')

plt.xlabel('Date')
plt.ylabel('CO')
plt.title('CO Trend Over Time')

plt.xticks(rotation=45)
plt.grid(True)

plt.show()

# --- Code cell 16 ---
plt.figure(figsize=(10,5))

plt.bar(df['Date'], df['AQI'])

plt.xlabel('Date')
plt.ylabel('AQI')
plt.title('AQI Comparison by Date')

plt.xticks(rotation=45)

plt.show()

# --- Code cell 17 ---
plt.figure(figsize=(6,5))

plt.boxplot(df['AQI'])

plt.ylabel('AQI')
plt.title('AQI Distribution')

plt.show()

# --- Code cell 18 ---
plt.figure(figsize=(8,5))

plt.scatter(df['PM2.5'], df['AQI'])

plt.xlabel('PM2.5')
plt.ylabel('AQI')
plt.title('AQI vs PM2.5')

plt.grid(True)

plt.show()

# --- Code cell 19 ---
plt.figure(figsize=(8,5))

plt.scatter(df['PM10'], df['AQI'])

plt.xlabel('PM10')
plt.ylabel('AQI')
plt.title('AQI vs PM10')

plt.grid(True)

plt.show()

# --- Code cell 20 ---
plt.figure(figsize=(8,5))

plt.scatter(df['CO'], df['AQI'])

plt.xlabel('CO')
plt.ylabel('AQI')
plt.title('AQI vs CO')

plt.grid(True)

plt.show()

# --- Code cell 21 ---
plt.figure(figsize=(10,5))

plt.plot(df['Date'], df['AQI'],
         marker='o',
         color='red',
         label='AQI')

plt.xlabel('Date')
plt.ylabel('AQI')
plt.title('Air Quality Index Trend')

plt.legend()
plt.grid(True)

plt.xticks(rotation=45)

plt.show()
================================================================================
DMV Practical 12
================================================================================

# --- Code cell 1 ---
import pandas as pd
import matplotlib.pyplot as plt

# --- Code cell 2 ---
df = pd.read_csv("Retail_Sales_Data.csv")

# --- Code cell 3 ---
df

# --- Code cell 4 ---
df.head()

# --- Code cell 5 ---
df.tail()

# --- Code cell 6 ---
df.shape

# --- Code cell 7 ---
df.columns

# --- Code cell 8 ---
df.dtypes

# --- Code cell 9 ---
df.describe()

# --- Code cell 10 ---
df.isnull().sum()

# --- Code cell 11 ---
df[["Region", "Product_Category", "Sales_Amount"]].head()

# --- Code cell 12 ---
region_sales = df.groupby("Region", as_index=False)["Sales_Amount"].sum()

region_sales

# --- Code cell 13 ---
plt.figure(figsize=(8,5))

plt.bar(region_sales["Region"], region_sales["Sales_Amount"])

plt.xlabel("Region")
plt.ylabel("Total Sales Amount")
plt.title("Total Sales by Region")

plt.show()

# --- Code cell 14 ---
plt.figure(figsize=(7,7))

plt.pie(
    region_sales["Sales_Amount"],
    labels=region_sales["Region"],
    autopct="%1.1f%%"
)

plt.title("Sales Distribution by Region")

plt.show()

# --- Code cell 15 ---
top_regions = region_sales.sort_values(
    by="Sales_Amount",
    ascending=False
)

print(top_regions)

# --- Code cell 16 ---
top_region = top_regions.iloc[0]

print("Top Performing Region:", top_region["Region"])
print("Sales Amount:", top_region["Sales_Amount"])

# --- Code cell 17 ---
print(top_regions.head(3))

# --- Code cell 18 ---
region_category_sales = df.groupby(
    ["Region", "Product_Category"],
    as_index=False
)["Sales_Amount"].sum()

region_category_sales

# --- Code cell 19 ---
pivot_data = df.pivot_table(
    index="Region",
    columns="Product_Category",
    values="Sales_Amount",
    aggfunc="sum"
)

pivot_data

# --- Code cell 20 ---
pivot_data.plot(
    kind="bar",
    stacked=True,
    figsize=(10,6)
)

plt.xlabel("Region")
plt.ylabel("Total Sales Amount")
plt.title("Sales by Region and Product Category")

plt.legend(title="Product Category")

plt.show()

# --- Code cell 21 ---
pivot_data.plot(
    kind="bar",
    figsize=(10,6)
)

plt.xlabel("Region")
plt.ylabel("Total Sales Amount")
plt.title("Sales Comparison by Region and Product Category")

plt.legend(title="Product Category")

plt.show()
