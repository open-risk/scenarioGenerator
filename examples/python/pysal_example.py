import numpy as np
import pysal.lib
from pysal.model.spreg import OLS

db = pysal.lib.io.open(pysal.lib.examples.get_path('columbus.dbf'), 'r')

hoval = db.by_col("HOVAL")
y = np.array(hoval)
y.shape = (len(hoval), 1)

X = []
X.append(db.by_col("INC"))
X.append(db.by_col("CRIME"))
X = np.array(X).T

ols = OLS(y, X, name_y='home value', name_x=['income', 'crime'], name_ds='columbus', white_test=True)

print(ols.summary)
