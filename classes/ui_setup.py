import json
from tkinter import Tk, ttk, messagebox, Canvas
import tkinter as tk
import pymongo
import pandas as pd
import matplotlib.pyplot as plt

BACKGROUND_COLOR = "#6B011F"
TEXT_COLOR = "#FEC260"


# db_dict = db.to_dict(orient="records")
# db_dict.append({"saba_konjaria": "12"})
# database.insert_many(db_dict)


class main_window(Tk):
    def __init__(self, database):
        super().__init__()
        self.__canvas__ = None
        self.db = database
        self.title("My Window")
        self.geometry("570x500")
        self.resizable(False, False)
        self.iconbitmap("data_input/detective.ico")
        self.config(bg=BACKGROUND_COLOR, padx=50, pady=70)

        self.purpose_label = tk.Label(text="NYPD\nData History", bg=BACKGROUND_COLOR, fg=TEXT_COLOR,
                                      font=("Sylfaen", 36, 'bold'))
        self.purpose_label.grid(row=0, column=1)

        # Variables
        self.combobox_variables1 = tk.StringVar()
        self.combobox_variables2 = tk.StringVar()

        self.data_processing_lbl = tk.Label(text="Filter by: ", fg=TEXT_COLOR, bg=BACKGROUND_COLOR,
                                            font=("Sylfaen", 12, 'bold'))
        self.data_processing_usr1 = ttk.Combobox(self, width=15, textvariable=self.combobox_variables1,
                                                 values=['Incident key', 'Borough', 'Victim age-group', 'Victim Sex',
                                                         'Victim Race', 'Jurisdiction code', 'Murder flag', 'Precinct',
                                                         'Date/time'])
        self.data_processing_usr2 = ttk.Combobox(self, width=15, textvariable=self.combobox_variables2,
                                                 values=['Incident key', 'Borough', 'Victim age-group', 'Victim Sex',
                                                         'Victim Race', 'Jurisdiction code', 'Murder flag', 'Precinct',
                                                         'Date/time'])
        self.data_processing_lbl.grid(row=1, column=0, pady=40)
        self.data_processing_usr1.grid(row=1, column=1)
        self.data_processing_usr2.grid(row=1, column=2)

        tk.Button(text="Build chart", bg="#0A2647", fg="#F1F7B5", command=self.filter_clicked, width=12).grid(row=5,
                                                                                                              column=1,
                                                                                                              pady=40)

        # Chart types Variables
        self.area_var = tk.BooleanVar(self, False)
        self.bar_var = tk.BooleanVar(self, False)
        self.plot_var = tk.BooleanVar(self, False)
        self.pie_var = tk.BooleanVar(self, False)

        # area
        self.area_button = tk.Checkbutton(self, text="Area chart", activeforeground="white", activebackground="#0A2647",
                                          selectcolor="#0A2647", variable=self.area_var, fg="white", bg="#0A2647")
        self.area_button.grid(row=2, column=0)
        # bar
        self.bar_button = tk.Checkbutton(self, text="Bar chart", activeforeground="white", activebackground="#0A2647",
                                         selectcolor="#0A2647", variable=self.bar_var, fg="white", bg="#0A2647")
        self.bar_button.grid(row=2, column=1)
        # plot
        self.plot_button = tk.Checkbutton(self, text="Plot chart", activeforeground="white", activebackground="#0A2647",
                                          selectcolor="#0A2647", variable=self.plot_var, fg="white", bg="#0A2647")
        self.plot_button.grid(row=2, column=2)
        # pie
        self.pie_button = tk.Checkbutton(self, text="Pie chart", activeforeground="white", activebackground="#0A2647",
                                         selectcolor="#0A2647", variable=self.pie_var, fg="white", bg="#0A2647")
        self.pie_button.grid(row=3, column=1, pady=10)

        self.mainloop()

    def filter_clicked(self):
        try:
            IS_EMPTY = ""
            CHARTS = [self.area_var.get(), self.bar_var.get(), self.pie_var.get(), self.plot_var.get()]
            if (self.combobox_variables1.get() == IS_EMPTY or self.combobox_variables1.get()
                not in self.data_processing_usr1['values'] or not any(CHARTS)) or \
                    (self.combobox_variables2.get() == IS_EMPTY or self.combobox_variables2.get()
                     not in self.data_processing_usr2['values'] or not any(CHARTS)):
                raise ValueError

            clues = list(self.db.keys())

            i = self.data_processing_usr1['values'].index(self.data_processing_usr1.get())
            if CHARTS[0]:
                pass
            if CHARTS[1]:
                pass
            if CHARTS[2]:
                pass
            if CHARTS[3]:
                pass

            plt.grid()
            plt.show()
            plt.close()
        except ValueError:
            messagebox.showinfo(title="Oops....", message="Verify that Chart type is selected and filter key is "
                                                          "selected in the drop-down list")
