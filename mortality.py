import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Load your mortality data into a pandas DataFrame
# Assuming your DataFrame is named 'mortality_data'
mortality_data = pd.read_csv(r"C:\Users\kaush\Documents\college assignments\AI lab\deathrate.csv")
# Fit the model

model = sm.GLM.from_formula("Total + Age + Year + Female + Male", family=sm.families.Poisson(), data=mortality_data)
fit = model.fit()

# Print summary of the fitted model
print(fit.summary())

# Assess goodness-of-fit
# Plot observed vs. fitted values
plt.figure(figsize=(10, 6))
plt.scatter(mortality_data['Total'], fit.fittedvalues)
plt.xlabel('Observed Mortality')
plt.ylabel('Fitted Mortality')
plt.title('Observed vs. Fitted Mortality')
plt.show()

# Plot residuals
plt.figure(figsize=(10, 6))
plt.scatter(mortality_data['Age'], fit.resid_pearson)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Age')
plt.ylabel('Pearson Residuals')
plt.title('Pearson Residuals vs. Age')
plt.show()
