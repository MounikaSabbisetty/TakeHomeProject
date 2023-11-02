import json
import urllib.request
import psycopg2
def lambda_handler(event, context):
try:
# External API URL
api_url = "https://health-products.canada.ca/api/clinical-trial/medicalcondition/?lang=en&type=json"
# Fetch data from the external API
with urllib.request.urlopen(api_url) as response:
data = json.load(response)
# PostgreSQL database connection details
host = "192.168.2.69"
database = "clinical_trials"
user = "postgres"
password = "postpwd"
# Connect to the PostgreSQL database
conn = psycopg2.connect(
host=host,
database=database,
user=user,
password=password
)
cursor = conn.cursor()
# Create a table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS MedicalCondition (
id SERIAL PRIMARY KEY,
name VARCHAR(255),
description TEXT
)
""")
conn.commit()
# Insert data into the database
for item in data:
cursor.execute("INSERT INTO MedicalCondition (name, description) VALUES (%s, %s)", (item['name'], item['description']))
conn.commit()
cursor.close()
conn.close()
return {
'statusCode': 200,
'body': json.dumps('Data loaded successfully!')
}
except Exception as e:
return {
'statusCode': 500,
'body': json.dumps(f'Error: {str(e)}')
}
