#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import matplotlib.pyplot as plt

# Load data from the current month's CSV file
current_month_csv = 'flight1fbaug.csv'
df = pd.read_csv(current_month_csv)

# Ask the user for the number of followers this month
user_followers_current = int(input("Enter the number of followers for the current month: "))

# Ask the user for the number of followers from the previous month
user_followers_previous = int(input("Enter the number of followers from the previous month: "))

# Calculate monthly growth in followers
followers_growth = user_followers_current - user_followers_previous

# Calculate followers' growth rate in percentage
followers_growth_rate = (followers_growth / user_followers_previous) * 100 if user_followers_previous > 0 else 0

# Calculate the average engagement rate for the previous and current month
previous_month_csv = 'flight1fbjuly23.csv'
previous_df = pd.read_csv(previous_month_csv)
previous_month_engagement_rate = (previous_df['Engagements'].mean() / user_followers_previous) * 100 if user_followers_previous > 0 else 0
current_month_engagement_rate = (df['Engagements'].mean() / user_followers_current) * 100

# Create a bar chart for followers growth rate
plt.figure(figsize=(2, 4))
plt.bar('Current Month', followers_growth_rate)
plt.xlabel('Month')
plt.ylabel('Followers Growth Rate (%)')
plt.title('Monthly Followers Growth Rate')
plt.show()

# Create a bar chart for average engagement rate
plt.figure(figsize=(6, 4))
plt.bar(['Previous Month', 'Current Month'], [previous_month_engagement_rate, current_month_engagement_rate])
plt.xlabel('Month')
plt.ylabel('Average Engagement Rate (%)')
plt.title('Average Monthly Engagement Rate')
plt.show()

# Print statistical analysis results
print(f"Followers Growth Rate: {followers_growth_rate:.2f}%")
print(f"Average Engagement Rate (Previous Month): {previous_month_engagement_rate:.2f}%")
print(f"Average Engagement Rate (Current Month): {current_month_engagement_rate:.2f}%")


# In[ ]:




