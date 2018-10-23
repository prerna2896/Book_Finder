import data_extractor as data_ext
import cross_validation as cross_val
import numpy as np

data = data_ext.read_data("../data/book_data.xlsx")

author_data = data["author"]
genre_data = data["genre"]
features = np.column_stack((author_data, genre_data))
rating_data = data["user_rating"]
labels = np.array(rating_data)

# Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier as DTC
print "Decision Tree Classifier accuracy: \t", cross_val.leave_k_out_cross_validation(1, DTC(), features, labels)

# KNeighbors Classifier
from sklearn.neighbors import KNeighborsClassifier as KNC
print "KNeighbors Classifier accuracy: \t", cross_val.leave_k_out_cross_validation(1, KNC(), features, labels)


