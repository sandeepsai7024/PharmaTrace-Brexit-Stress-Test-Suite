import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# 1. Create a larger, more complex dataset
n_rows = 2000
data = {
    'Lead_Time': np.random.normal(7, 2, n_rows), # Normal distribution
    'Border_Congestion': np.random.poisson(3, n_rows), # Poisson distribution
    'Storage_Type': np.random.choice([0, 1], n_rows), # 0=Ambient, 1=Cold Chain
    'Route_ID': np.random.choice([1, 2, 3], n_rows) # 1=Dover, 2=Air, 3=Tunnel
}
df = pd.DataFrame(data)

# 2. Logic: Create a 'Stock_Out' target (1 if stock-out happens, 0 if not)
# If Lead time + Congestion > 12 days and it's Cold Chain, it's a Stock-Out
df['Stock_Out'] = ((df['Lead_Time'] + df['Border_Congestion'] > 12) & (df['Storage_Type'] == 1)).astype(int)

# 3. Train a quick Random Forest to get 'Importance'
X = df[['Lead_Time', 'Border_Congestion', 'Storage_Type', 'Route_ID']]
y = df['Stock_Out']
model = RandomForestClassifier().fit(X, y)

# 4. Save this for Power BI
df.to_csv('PharmaTrace_ML_Data.csv', index=False)
print("Tech-Forward Dataset Created!")
