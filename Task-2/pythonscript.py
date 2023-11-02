import requests
import psycopg2
# Define your API URL
api_url = "https://health-products.canada.ca/api/clinical-trial/sponsor/?lang=en&type=json"
# Define your PostgreSQL database connection parameters
db_host = "192.168.2.69"
db_name = "clinical_trails"
db_user = "postgres"
db_password = "postpwd"
# Function to fetch data from the API
def fetch_data_from_api(url):
response = requests.get(url)
data = response.json()
return data
# Function to sanitize text to be compatible with WIN1252
def sanitize_text(text):
# Replace problematic characters with '?'
sanitized_text = ''.join(char if ord(char) < 128 else '?' for char in text)
return sanitized_text
# Function to create the database table
def create_database_table():
conn = psycopg2.connect(
host=db_host,
database=db_name,
user=db_user,
password=db_password
)
cursor = conn.cursor()
create_table_query = """
CREATE TABLE IF NOT EXISTS Sponsor (
manufacturer_id INT PRIMARY KEY,
manufacturer_name VARCHAR(255)
)
"""
cursor.execute(create_table_query)
conn.commit()
cursor.close()
conn.close()
# Function to insert data into the database
def insert_data_into_database(data):
conn = psycopg2.connect(
host=db_host,
database=db_name,
user=db_user,
password=db_password
)
cursor = conn.cursor()
for item in data:
# Sanitize manufacturer_name before inserting
manufacturer_name = sanitize_text(item['manufacturer_name'])
cursor.execute("INSERT INTO Sponsor (manufacturer_id, manufacturer_name) VALUES (%s, %s)",
(item['manufacturer_id'], manufacturer_name))
conn.commit()
cursor.close()
conn.close()
# Main function to orchestrate the process
def main():
# Create the database table if it doesn't exist
create_database_table()
# Fetch data from the API
api_data = fetch_data_from_api(api_url)
# Insert data into the database
insert_data_into_database(api_data)
print("Data loaded into the database successfully.")
if __name__ == "__main__":
main()
