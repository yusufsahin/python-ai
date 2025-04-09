import pickle

with open("data.pkl", "rb") as file:
    load_data = pickle.load(file)
    print(type(load_data))
    print(load_data)