from multiprocessing import Process, Queue
from classes.ui_setup import main_window
import pymongo
import pandas as pd
import matplotlib.pyplot as plt

try:

    def main():
        client = pymongo.MongoClient('localhost', 27017)
        database = client["Project"]["NYPD_shoot"]
        df = pd.read_csv(filepath_or_buffer="data_input/NYPD_Shooting_Incident_Data__Historic_.csv")
        my_app = main_window(df)



    if __name__ == "__main__":
        queue = Queue()
        p = Process(target=main)
        p.start()
        p.join()
        result = queue.get()
except RecursionError as an_Exception:
    pass
else:
    pass
finally:
    pass
