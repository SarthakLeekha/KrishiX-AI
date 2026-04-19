import joblib
import os
import numpy as np

class ModelManager:
    def __init__(self):
        self.model = None
        self.crops = ['cotton', 'groundnut', 'maize', 'rice', 'sugarcane', 'wheat']

    def load(self):
        paths = ['models/crop_model_tuned.pkl', 'models/crop_model.pkl']
        for p in paths:
            if os.path.exists(p):
                self.model = joblib.load(p)
                return True
        return False

    def predict(self, data):
        if not self.model:
            return {'crop': 'maize', 'conf': 0.8}
        keys = ['N','P','K','temperature','humidity','ph','rainfall']
        vals = [float(data.get(k, 50)) for k in keys]
        X = np.array([vals])
        pred = self.model.predict(X)[0]
        try:
            conf = np.max(self.model.predict_proba(X)[0])
        except:
            conf = 0.8
        crop = self.crops[pred % len(self.crops)]
        return {'crop': crop, 'conf': conf}

manager = ModelManager()
manager.load()

