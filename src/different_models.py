import data_extractor as de
import cross_validation as cv
from sklearn.tree import DecisionTreeClassifier as DTC

data = de.read_data("../data/book_data.xlsx")

features = data[:, ["author", "genre"]]
labels = data["user_rating"]

print features
print labels

print features.shape
print labels.shape

# Decision Tree Classifier
# decisionTree = DTC()
# cv.leave_k_out_cross_validation(1, decisionTree, features, labels)

