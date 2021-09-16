# 분석파일 추가해야 하는 곳
import pickle
import numpy as np


class Analysis:
    def sizeRecomm(self, age, height, weight):   # age: INT, height: FLOAT, weight: INT
        '''
        Best model is Random Forest
        '''

        # Load pickle
        with open('best_model.pickle', 'rb') as f:
            rf_clf = pickle.load(f)

        # Test data
        X_test = np.array([[weight, age, height]])

        # Predict
        size = rf_clf.predict(X_test)

        return size    # 문자열로 반환해야 함
