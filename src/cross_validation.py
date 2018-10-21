def leave_k_out_cross_validation(k, model, features, labels):
    accuracy = 0.0
    features_len = len(features)
    for i in range(features_len - k):
        features_train = features[0 : i] + features[i + k : data_len]
        labels_train = labels[0 : i] + labels[i + k : data_len] 
        features_test = features[i : i + k]
        labels_test = labels[i : i + k]
        model.fit(features_train, labels_train)
        accuracy += model.score(features_test, labels_test)
    accuracy /= (data_len - k)
    return accuracy
