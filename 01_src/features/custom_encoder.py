class CustomLabelEncoder:
    def __init__(self, label_map):
        self.label_map = label_map
        self.inverse_label_map = {v: k for k, v in label_map.items()}

    def fit_transform(self, labels):
        encoded_labels = list(map(lambda x: self.label_map[x], labels))
        return encoded_labels

    def inverse_transform(self, encoded_labels):
        decoded_labels = list(map(lambda x: self.inverse_label_map[x], encoded_labels))
        return decoded_labels