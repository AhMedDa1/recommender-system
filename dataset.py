import pandas as pd
import numpy as np


class data:
    def __init__(self, path):
        self.path = path
        self.data = pd.read_csv(path, 
                                ).drop(columns='timestamp')
        self.data = self.data.to_numpy()
    
    def data_structure(self, data, test_size):
        np.random.shuffle(data)

        user_map, movie_map = {}, {}
        user_rating, movie_rating = [], []

        data_by_user_train, data_by_user_test = [], []
        data_by_movie_train, data_by_movie_test = [], []

        user_ids = data[:, 0].tolist()
        movie_ids = data[:, 1].tolist()
        ratings = data[:, 2].tolist()
         
        for i in range(len(data)):
            user = user_ids[i]
            movie = movie_ids[i]
            rating = ratings[i]

            if user not in user_map:
                user_map[user] = len(user_rating)
                user_rating.append([])
                data_by_user_train.append([])
                data_by_user_test.append([])

            if movie not in movie_map:
                movie_map[movie] = len(movie_rating)
                movie_rating.append([])
                data_by_movie_train.append([])
                data_by_movie_test.append([])

            user_idx = user_map[user]
            movie_idx = movie_map[movie]

            user_rating[user_idx].append((movie, rating))
            movie_rating[movie_idx].append((user_idx, rating))

            if np.random.rand() > test_size:
                data_by_user_train[user_idx].append((movie, rating))
                data_by_movie_train[movie_idx].append((user_idx, rating))
            else:
                data_by_user_test[user_idx].append((movie, rating))
                data_by_movie_test[movie_idx].append((user_idx, rating))

        return (
            data_by_user_train, data_by_movie_train,
            data_by_user_test, data_by_movie_test,
            user_map, movie_map,
        )
    

# if __name__ =="__main__":
#     csv = "Data/ratings_small.csv"

#     data_set = data(csv)

#     train_test_split_results = data_set.data_structure(
#         data_set.data, test_size=0.2
#     )

#     (
#         data_by_user_train,
#         data_by_movie_train,
#         data_by_user_test,
#         data_by_movie_test,
#         user_map,
#         movie_map,
#     ) = train_test_split_results

#     print("Shape of data_by_user_train:", len(data_by_user_train))
#     print("Shape of data_by_movie_train:", len(data_by_movie_train))
#     print("Shape of data_by_user_test:", len(data_by_user_test))
#     print("Shape of data_by_movie_test:", len(data_by_movie_test))
#     print("Number of users in user_map:", len(user_map))
#     print("Number of movies in movie_map:", len(movie_map))



