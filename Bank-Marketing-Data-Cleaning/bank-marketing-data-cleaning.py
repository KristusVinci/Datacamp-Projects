import pandas as pd
import numpy as np

df = pd.read_csv("bank_marketing.csv")

df['year'] = 2022

df['last_contact_date'] = pd.to_datetime(df[['year','month','day']].astype(str).agg('-'.join, axis=1),format='%Y-%b-%d',errors='coerce').dt.date

df['job'] = df['job'].replace('.','_', regex=False)
df['education'] = df['education'].str.replace('.','_',regex=False)
df['education'] = df['education'].replace('unknown',np.nan)
df['credit_default'] = df['credit_default'].eq('yes')
df['mortgage'] = df['mortgage'].eq('yes')
df['previous_outcome'] = df['previous_outcome'].eq('success')
df['campaign_outcome'] = df['campaign_outcome'].eq('yes')

client_df = df[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']]

campaign_df = df[['client_id', 'number_contacts', 'contact_duration', 'previous_outcome','campaign_outcome','last_contact_date']]

economics_df = df[['client_id','cons_price_idx','euribor_three_months']]

client_df.to_csv("client.csv", index=False)
campaign_df.to_csv("campaign.csv", index = False)
economics_df.to_csv("economics.csv", index = False)