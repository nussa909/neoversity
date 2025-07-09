import pickle


class FileSerializer:
    def __init__(self, filename):
        self.__filename = filename

    def save_data(self, data):
        with open(self.__filename, "wb") as f:
            pickle.dump(data, f)

    def load_data(self):
        try:
            with open(self.__filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("File not found")
            return None
