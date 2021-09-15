# 분석파일 추가해야 하는 곳
import pickle
import numpy as np


class Analysis:
    def sizeRecomm(self, age, height, weight):   # age: INT, height: FLOAT, weight: INT
        '''
        Best model is XGboost
        '''

        # Load pickle
        with open('best_model.pickle', 'rb') as f:
            xgb = pickle.load(f)

        # Test data
        X_test = np.array([[weight, age, height]])

        # Predict
        size = xgb.predict(X_test)

        return size    # 문자열로 반환해야 함
