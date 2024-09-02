# %%
import joblib
import pandas as pd

# %%
baseline_model = joblib.load('baseline.pkl')

# %%
df = pd.read_csv('../Archive/train.csv')

# %%
df.drop(columns='Id', inplace=True)

# %%
importances = baseline_model.feature_importances_
feature_names = [col for col in df.columns if col != 'SalePrice']
feature_importances = list(zip(feature_names, importances))

# %%
feature_importances_sorted = sorted(feature_importances, key=lambda x: x[1], reverse=True)

# %%
for feature, importance in feature_importances_sorted:
    print(f"{feature}: {importance:.4f}")
# %%
