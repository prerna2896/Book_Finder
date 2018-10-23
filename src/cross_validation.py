import numpy as np
import pandas as pd
from sklearn import preprocessing

def leave_k_out_cross_validation(k, model, features, labels):
  enc = preprocessing.OneHotEncoder(handle_unknown='ignore')
  accuracy = 0.0
  features_len = len(features)
  for i in range(features_len - k):
      features_train = np.concatenate([features[0 : i], features[i + k : features_len]])
      labels_train = np.concatenate([labels[0 : i], labels[i + k : features_len]])
      features_test = features[i : i + k]
      labels_test = labels[i : i + k]
      enc.fit(features_train)
      model.fit(enc.transform(features_train), labels_train)
      accuracy += model.score(enc.transform(features_test), labels_test)
  accuracy /= (features_len - k)
  return accuracy
