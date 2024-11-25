import pandas as pd
import numpy as np
import pickle




class data:
    def __init__(self, path):
        self.path = path
        self.data = pd.read_csv(path).drop(columns='timestamp')

        self.data = self.data.to_numpy()
        

    def split(self):
        splitr = 0.2
        data = self.process(self.data, splitr)
        user_train, item_train, user_test = data[4], data[5], data[6]

        return user_train, item_train, user_test

    def process(self, data, split):
        splitp = int((1-split) * len(data))
        user_dict = {}
        idx_to_user = []
        item_dict = {}
        idx_to_item = []

        for idx in range(len(data)):

            user_id = data[idx][0]
            item_id = data[idx][1]

            if user_id not in user_dict:
                idx_to_user.append((user_id))
                user_dict[(user_id)] = len(user_dict)
            
            if item_id not in item_dict:
                idx_to_item.append((item_id))
                item_dict[(item_id)]=len(item_dict)
        
        user_train = [[] for i in range(len(idx_to_user))]
        item_train = [[] for i in range(len(idx_to_item))]

        user_test = [[] for i in range(len(idx_to_user))]
        item_test = [[] for i in range(len(idx_to_item))]

        for idx in range(len(data)):
            
            user_id = data[idx][0]
            item_id = data[idx][1]
            rating  = data[idx][2]
            user_idx = user_dict[user_id]
            item_idx = item_dict[item_id]

            if idx < splitp:
                user_train[user_idx].append((item_idx, float(rating)))
                item_train[item_idx].append((user_idx, float(rating)))

            else:
                user_test[user_idx].append((item_idx, float(rating)))
                item_test[item_idx].append((user_idx,float(rating)))

        return (user_dict,
                idx_to_user,
                item_dict,
                idx_to_item,
                user_train,
                item_train,
                user_test,
                item_test
               )
