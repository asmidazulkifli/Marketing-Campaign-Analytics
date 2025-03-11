#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import random
import numpy as np

# Define constants
num_rows = 189000  # Adjust dataset size
start_date = "2022-01-01"
end_date = "2025-07-30"

# Generate date range
full_date_range = pd.date_range(start=start_date, end=end_date, freq='D')

def weighted_random_dates(dates, weights, size):
    return np.random.choice(dates, size=size, p=weights)

# Create seasonal patterns for different years
year_weights = {2022: 0.08, 2023: 0.20, 2024: 0.35, 2025: 0.37}
month_weights = {
    1: 0.05, 2: 0.06, 3: 0.07,  # Q1: Low activity
    4: 0.08, 5: 0.08, 6: 0.09,  # Q2: Slight increase
    7: 0.1, 8: 0.1, 9: 0.08,    # Q3: Mid-year stability
    10: 0.12, 11: 0.14, 12: 0.11  # Q4: Peaks in Nov (Black Friday), Dec (Holidays)
}

date_weights = np.array([month_weights[d.month] for d in full_date_range])
date_weights /= date_weights.sum()  # Normalize weights

# Re-weighted dates to ensure seasonality
dates = weighted_random_dates(full_date_range, date_weights, num_rows)

# Normalize month weights
monthly_date_weights = np.array([month_weights[pd.Timestamp(d).month] for d in pd.to_datetime(dates)])
monthly_date_weights /= monthly_date_weights.sum()

# Campaign details
campaign_names = [
    "Spring Sale", "Black Friday", "Webinar Series", 
    "Product Launch", "Customer Loyalty", "Clearance Sale", 
    "Exclusive Offers", "Holiday Special", "Flash Deals"
]

campaignnames_probs = [
    0.16,  # Spring Sale
    0.14,  # Black Friday
    0.12,  # Webinar Series
    0.12,  # Product Launch
    0.10,  # Customer Loyalty
    0.10,  # Clearance Sale
    0.09,  # Exclusive Offers
    0.09,  # Holiday Special
    0.08   # Flash Deals
]
campaign_types = ["Newsletter", "Events & Webinars", "Promotional", "Lead Nurturing"]
campaigntypes_probs = [0.12, 0.24, 0.46, 0.18] 
conversion_targets = ["Download", "Purchase", "Sign Up", "Enroll", "Web Visit"]
conversiontargets_probs = [0.12, 0.32, 0.16, 0.18, 0.22] 

# Customer segments with realistic distribution
client_segments = ["lead", "existing customer"]
client_segment_probs = [0.35, 0.65]  # 35% leads, 65% existing customers

devices = ["mobile", "desktop", "tablet"]
devices_probs = [0.3, 0.5, 0.2] 

countries = ["Qatar", "China", "Germany", "Canada", "Australia", "France", "India", "Malaysia", "Singapore", "Japan", "New Zealand", "Nigeria", "Kenya", "South Africa", "Cuba", "Jamaica", "United States", "Brazil", "Chile", "Colombia", "Argentina"]
continent_map = {
    "Qatar": "Asia", "China": "Asia", "India": "Asia", "Malaysia": "Asia", "Singapore": "Asia", "Japan": "Asia",
    "Germany": "Europe", "France": "Europe",
    "Canada": "North America", "Cuba": "North America", "Jamaica": "North America", "United States": "North America",
    "Brazil": "South America", "Chile": "South America", "Colombia": "South America", "Argentina": "South America",
    "Australia": "Oceania", "New Zealand": "Oceania",
    "Nigeria": "Africa", "Kenya": "Africa", "South Africa": "Africa"
}
email_domains = ["gmail.com", "hotmail.com", "aol.com", "outlook.com", "yahoo.com"]

# Function to generate varied emails
def generate_email():
    user_id = random.randint(1000, 99999)
    domain = random.choice(email_domains)
    return f"user{user_id}@{domain}"

# Generate random data
data = {
    "Campaign Name": np.random.choice(campaign_names, size=num_rows, p=campaignnames_probs),
    "Campaign Type": np.random.choice(campaign_types, size=num_rows, p=campaigntypes_probs),
    "Conversion Target": np.random.choice(conversion_targets, size=num_rows, p=conversiontargets_probs),
    "Date Sent": dates,
    "Client Email": [generate_email() for _ in range(num_rows)],
    "Client Segment": np.random.choice(client_segments, size=num_rows, p=client_segment_probs),
    "Country": np.random.choice(countries, size=num_rows),
    "Continent": [continent_map[country] for country in np.random.choice(countries, size=num_rows)],
    "Device": np.random.choice(devices, size=num_rows, p=devices_probs),
}

# Generate logical email interactions
opened = np.random.choice([0, 1], size=num_rows, p=[0.3, 0.7])  # 70% open rate
clicked = [1 if o and random.random() < 0.6 else 0 for o in opened]  # 60% of opened emails clicked
bounced = [1 if not o and random.random() < 0.4 else 0 for o in opened]  # 40% of non-opened emails bounced
unsubscribed = [1 if c and random.random() < 0.2 else 0 for c in clicked]  # 20% of clicked unsubscribed
converted = [1 if c and random.random() < 0.4 else 0 for c in clicked]  # 40% of clicked converted

# Add interactions to data
data.update({
    "Opened": opened,
    "Clicked": clicked,
    "Bounced": bounced,
    "Unsubscribed": unsubscribed,
    "Conversion": converted
})

# Create DataFrame
df = pd.DataFrame(data)
df.head()


# In[2]:


df.to_csv(r"C:\Users\60177\Desktop\Mine\Project24\Marketing Analytics\campaign_data.csv")


# In[ ]:





# In[ ]:




