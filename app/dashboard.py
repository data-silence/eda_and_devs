import pandas as pd
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from explainerdashboard import *

df = pd.read_pickle("df_eda.pickle")

X = df.drop(columns=['y', 'Administrative', 'Informational', 'ProductRelated'])
y = df['y']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

modelCB = CatBoostClassifier(verbose=0, cat_features=[7, 8, 9, 10, 11, 12, 13])
modelCB.fit(X_train, y_train)

explainer = ClassifierExplainer(modelCB, X_test, y_test,
                                model_output='logodds', labels=['Buy', 'Not Buy'])

db = ExplainerDashboard(explainer)
db.to_yaml("dashboard.yaml", explainerfile="explainer.joblib", dump_explainer=True)
