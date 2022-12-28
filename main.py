from classes.ui_setup import main_window
import pandas as pd


def main():
    df = pd.read_csv(filepath_or_buffer="data_input/NYPD_Shooting_Incident_Data__Historic_.csv")
    my_ui = main_window(database=df)


if __name__ == "__main__":
    main()
