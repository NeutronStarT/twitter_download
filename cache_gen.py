import os
import pickle

class cache_gen():

    def __init__(self, save_path) -> None:
        self.cache_path = save_path + os.sep + "cache_data_v2.log"

        if os.path.exists(self.cache_path):
            with open(self.cache_path, 'r') as f:
                self.cache_data = set(line.strip() for line in f.readlines())
        else:
            self.cache_data = set()

    def add(self, element):
        if element not in self.cache_data:
            self.cache_data.add(element)

    def is_present(self, element):
        if element in self.cache_data:
            return False
        else:
            self.add(element)
            return True
    
    def save_cache(self, element):
        if element not in self.cache_data:
            self.cache_data.add(element)
        with open(self.cache_path, 'a') as f:
            f.write(element + '\n')

