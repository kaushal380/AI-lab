from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd


data = pd.DataFrame(data={
    'Rain': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No'],
    'TrafficJam': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No'],
    'ArriveLate': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No']
})

model = BayesianModel([('Rain', 'TrafficJam'), ('TrafficJam', 'ArriveLate')])
model.fit(data, estimator=MaximumLikelihoodEstimator)

# Print conditional probability distributions
for cpd in model.get_cpds():
    print(cpd)

inference = VariableElimination(model)
query_result = inference.query(variables=['ArriveLate'], evidence={'Rain': 'Yes'})
print(query_result)
