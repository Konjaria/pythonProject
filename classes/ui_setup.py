"""

Final Project -  Object-Oriented Programming 2 (Python)
Author: Saba Konjaria
created at: 29 Dec, 2022
Description of the Dataset  Below
***********************************************************************
This is a comprehensive list of all shooting incidents that have taken place in New York City
since 2006  up until the end of the previous year. The data is collected and reviewed by the Office of
Management Analysis and Planning on a quarterly basis before being made available on the NYPD website. Each record
includes details about the incident, such as the location and time it occurred, as well as information about the
suspects and victims involved.

Data source: https://catalog.data.gov/dataset/nypd-shooting-incident-data-historic

"""
import sqlite3
import tkinter as tk
from tkinter import Tk, ttk, messagebox
import matplotlib.pyplot as plt
import pandas as pd
try:
    # ------------------------ Constants --------------------------------
    BACKGROUND_COLOR = "#6B011F"
    TEXT_COLOR = "#FEC260"
    DATABASE_PATH = "./data_input/data.db"
    FILE_NAME = './data_input/NYPD_Shooting_Incident_Data__Historic_.csv'
    RUN_TIME = 0
    df = pd.read_csv(filepath_or_buffer=FILE_NAME)

    # ------------------------ Class Definition --------------------------
    class main_window(Tk):
        # ------------------------ Constructor UI/UX ---------------------
        def __init__(self):
            super().__init__()
            self.df = df  # Getting the data from the dataframe
            # ------------------------ UI --------------------------------
            self.title("NYPD History")
            self.geometry("640x470+0+0")
            self.resizable(False, False)
            self.iconbitmap("data_input/detective.ico")
            self.config(bg=BACKGROUND_COLOR, padx=50, pady=70)

            # Title Label
            tk.Label(self, text="NYPD\nData History", bg=BACKGROUND_COLOR, fg=TEXT_COLOR,
                     font=("Sylfaen", 36, 'bold')).grid(row=0, column=1)
            tk.Label(self, text="Filter by: ", fg=TEXT_COLOR, bg=BACKGROUND_COLOR,
                     font=("Sylfaen", 12, 'bold')).grid(row=1, column=0, pady=40)

            # ----------------- Variables Declaration ----------------------

            self.combobox_var = tk.StringVar()  # 1.1 Combobox Variable
            self.area_var = tk.BooleanVar(self, False)  # 1.2  Area chart type
            self.bar_var = tk.BooleanVar(self, False)  # 1.3  Bar chart type
            self.plot_var = tk.BooleanVar(self, False)  # 1.4  Plot chart type
            self.pie_var = tk.BooleanVar(self, False)  # 1.5  Pie chart type


            # fixed: create a drop-down list for better UX
            self.drop_down = ttk.Combobox(self, width=37, textvariable=self.combobox_var,
                                          values=[element for element in list(self.df.keys()) if element not in ['incident_key','OCCUR_DATE','OCCUR_TIME']])

            # Buttons for Data processing in two different ways
            tk.Button(self, text="Get Info", bg="#0A2647", fg="#F1F7B5", command=self.get_info, width=12).grid(row=1, column=2, padx=10)
            tk.Button(self, text="Build Chart", bg="#0A2647", fg="#F1F7B5", command=self.plot_chart, width=12).grid(row=5, column=1, padx=10, pady=20, ipadx=20)


            # Check Buttons for several types of Chart types
            tk.Checkbutton(self, width=15, text="Area chart", activeforeground="white", fg="white", bg="#0A2647",
                           activebackground="#0A2647", selectcolor="#0A2647", variable=self.area_var).grid(row=2, column=0)
            tk.Checkbutton(self, width=15, text="Bar chart", activeforeground="white", fg="white", bg="#0A2647",
                           activebackground="#0A2647", selectcolor="#0A2647", variable=self.bar_var,).grid(row=2, column=1)
            tk.Checkbutton(self, width=15, text="Plot chart", activeforeground="white", fg="white", bg="#0A2647",
                           activebackground="#0A2647", selectcolor="#0A2647", variable=self.plot_var).grid(row=2, column=2)
            tk.Checkbutton(self, width=15, text="Pie chart", activeforeground="white", fg="white", bg="#0A2647",
                           activebackground="#0A2647", selectcolor="#0A2647", variable=self.pie_var).grid(row=3, column=1, pady=10)
            # Put the Drop-down list somewhere onto the screen, I prefer using grid manager instead of pack or place
            self.drop_down.grid(row=1, column=1)
            self.mainloop()

        # ------------------------ Functionality -------------------------

        def plot_chart(self):
            """
            this function is responsible for plotting the charts, according to several check buttons matches.
            plot_chart() checks whether user chose already some chart type and filter_key already or not
            :return:
            """
            p1 = self.combobox_var.get().upper()
            CHARTS = [self.area_var.get(), self.bar_var.get(), self.pie_var.get(), self.plot_var.get()]
            try:
                global RUN_TIME
                if p1 == '' or p1 not in self.drop_down['values'] or not any(CHARTS):
                    raise ValueError
            except ValueError:
                messagebox.showinfo(parent=self, title="Error",
                                    message="Verify that Chart type  and filter key are selected. "
                                            "Notice that, filter key must be chosen from the drop-down list")
            else:
                if CHARTS[0]:
                    fig1, ax1 = plt.subplots()
                    diagram_0 = self.df[p1].value_counts()
                    diagram_0 = diagram_0.sort_index()
                    diagram_0.plot(kind='area', x=diagram_0.index, y=diagram_0.values, ax=ax1)
                    plt.title(f"Number of Incidences according to {p1}")
                    plt.xlabel(f'{p1}')
                    plt.ylabel(f'Incidence numbers ')
                    plt.grid()

                if CHARTS[1]:
                    fig1, ax2 = plt.subplots()
                    diagram_1 = self.df[p1].value_counts()
                    diagram_1 = diagram_1.sort_index()
                    if RUN_TIME % 2 == 0:
                        diagram_1.plot(kind='bar', x=diagram_1.index, y=diagram_1.values, ax=ax2, hatch='+',
                                       color="#227C70")
                    else:
                        diagram_1.plot(kind='bar', x=diagram_1.index, y=diagram_1.values, ax=ax2, color="#3C2317")

                    plt.title(f"Number of Incidences according to {p1}")
                    plt.xlabel(f'{p1}')
                    plt.ylabel(f'Incidence numbers ')
                    plt.grid()

                if CHARTS[2]:
                    fig1, ax3 = plt.subplots()
                    diagram_2 = self.df[p1].value_counts()
                    diagram_2 = diagram_2.sort_index()
                    explode = []
                    MAX_ELEM_INDEX = 0
                    MAX_ELEM = list(diagram_2)[MAX_ELEM_INDEX]
                    for i in range(len(diagram_2.values)):
                        curr_elem = list(diagram_2.values)[i]
                        if MAX_ELEM < curr_elem:
                            MAX_ELEM = curr_elem
                            MAX_ELEM_INDEX = i
                        explode.append(0)
                    explode[MAX_ELEM_INDEX] = 0.1
                    print(len(explode), len(diagram_2.keys()))

                    diagram_2.plot(kind='pie', x=diagram_2.index, y=diagram_2.values, ax=ax3, explode=explode, shadow=True,
                                   startangle=90, autopct='%1.1f%%',
                                   wedgeprops={'edgecolor': '#85586F'}, figsize=(11, 5))
                    plt.title(f"Number of Incidences according to {p1}")
                    plt.grid()

                if CHARTS[3]:
                    fig1, ax4 = plt.subplots()
                    diagram_3 = self.df[p1].value_counts()
                    diagram_3 = diagram_3.sort_index()
                    if RUN_TIME % 2 == 0:
                        diagram_3.plot(kind='line', x=diagram_3.index, y=diagram_3.values, ax=ax4,
                                       color='#444444', linestyle='dashed', lw=3)
                    else:
                        diagram_3.plot(kind='line', x=diagram_3.index, y=diagram_3.values, ax=ax4,
                                       color='#88A47C', linestyle='dashdot', lw=3)
                    plt.title(f"Number of Incidences according to {p1}")
                    plt.xlabel(f'{p1}')
                    plt.ylabel(f'Incidence numbers ')
                    plt.grid()

                RUN_TIME += 1
                plt.show()
                plt.close()

        def add(self):
            """
            After the information has been received from the user, they will use this function to
            insert it  into the database and  csv file, only if they  wish to do so
            :return: None
            """
            try:
                if not any([self.INCIDENT_KEY_entry.get(),  self.OCCUR_DATE_entry.get(),  self.OCCUR_TIME_entry.get(), self.BOROUGH_entry.get(), self.PRECINCT_entry.get(), self.JURISDICTION_CODE_entry.get(),
                            self.STATISTICAL_MURDER_FLAG_entry.get(), self.VIC_AGE_GROUP_entry.get(), self.VIC_SEX_entry.get(), self.VIC_RACE_entry.get()]):
                    raise ValueError
            except ValueError:
                messagebox.showerror(parent=self.new_window, title="Error", message="Please enter a value for at least "
                                                                                "one field.")
            else:
                # todo: connect SQLite3 database
                conn = sqlite3.connect(database=DATABASE_PATH)
                c = conn.cursor()
                c.execute('INSERT INTO crimes VALUES(:incident_key, :date, :time, :borough, :precinct, '
                          ':jurisdiction_code, '
                          ':statistical_murder_flag, :vic_age_grp, :vic_sex, :vic_race)', {
                              'incident_key': self.INCIDENT_KEY_entry.get(),
                              'date': self.OCCUR_DATE_entry.get(),
                              'time': self.OCCUR_TIME_entry.get(),
                              'borough': self.BOROUGH_entry.get(),
                              'precinct': self.PRECINCT_entry.get(),
                              'jurisdiction_code': self.JURISDICTION_CODE_entry.get(),
                              'statistical_murder_flag': self.STATISTICAL_MURDER_FLAG_entry.get(),
                              'vic_age_grp': self.VIC_AGE_GROUP_entry.get(),
                              'vic_sex': self.VIC_SEX_entry.get(),
                              'vic_race': self.VIC_RACE_entry.get(),
                          })

                conn.commit()
                conn.close()


                self.clear_GUI()
                answer = messagebox.askyesno(parent=self.new_window,
                                             title="Congrats",
                                             message="Data has been updated succesfully, Do you want to "
                                                     "write them into the data_file? ")
                if answer:
                    self.__write_into_csv__()



        def clear_GUI(self):
            """
            clears everything inside the database new_window
            :return: None
            """
            self.INCIDENT_KEY_entry.delete(0, 'end')
            self.OCCUR_DATE_entry.delete(0, 'end')
            self.OCCUR_TIME_entry.delete(0, 'end')
            self.BOROUGH_entry.delete(0, 'end')
            self.PRECINCT_entry.delete(0, 'end')
            self.JURISDICTION_CODE_entry.delete(0, 'end')
            self.STATISTICAL_MURDER_FLAG_entry.delete(0, 'end')
            self.VIC_AGE_GROUP_entry.delete(0, 'end')
            self.VIC_SEX_entry.delete(0, 'end')
            self.VIC_RACE_entry.delete(0, 'end')
            self.result_label.config(text='')

        def find_record(self):
            """
            this function si responsible for searching the data that the user  provide and prints appropriate messages
            :return: None
            """
            # todo: connect the database
            conn = sqlite3.connect(database=DATABASE_PATH)

            # todo: code-optimization, not to write all the time i.e. self.INCIDENT_KEY_entry.get()
            incident_key = self.INCIDENT_KEY_entry.get()
            occur_date = self.OCCUR_DATE_entry.get()
            occur_time = self.OCCUR_TIME_entry.get()
            borough = self.BOROUGH_entry.get()
            precinct = self.PRECINCT_entry.get()
            jurisdiction_code = self.JURISDICTION_CODE_entry.get()
            statistical_murder_flag = self.STATISTICAL_MURDER_FLAG_entry.get()
            vic_age_group = self.VIC_AGE_GROUP_entry.get()
            vic_sex = self.VIC_SEX_entry.get()
            vic_race = self.VIC_RACE_entry.get()


            try:
                # todo : check whether if at least one field is filled in
                if not any([incident_key, occur_date, occur_time, borough, precinct, jurisdiction_code, statistical_murder_flag, vic_age_group, vic_sex, vic_race]):
                    raise ValueError
                # todo: check if this line thows TypeError or not, if yes, that means that user provide invalid data that can not be found in out database
                record = list(main_window.search_database(incident_key=incident_key, occur_date=occur_date, occur_time=occur_time, borough=borough, precinct=precinct, jurisdiction_code=jurisdiction_code,
                                                          statistical_murder_flag=statistical_murder_flag, vic_age_group=vic_age_group, vic_sex=vic_sex, vic_race=vic_race))
            except TypeError:
                messagebox.showinfo(parent=self.new_window, title="Please check provided data", message="No record was found with the given information.")
            except ValueError:
                messagebox.showinfo(parent=self.new_window, title="Please check provided data", message="Please enter a value for at least one field.")
            else:
                # todo: as soon as the user will put the information into the entries, program clears the screen,
                # todo: as the hint that the data has been successfully updated
                self.result_label.config(text="")
                self.clear_GUI()
                self.INCIDENT_KEY_entry.insert(0, record[0][0])
                self.OCCUR_DATE_entry.insert(0, record[0][1])
                self.OCCUR_TIME_entry.insert(0, record[0][2])
                self.BOROUGH_entry.insert(0, record[0][3])
                self.PRECINCT_entry.insert(0, record[0][4])
                self.JURISDICTION_CODE_entry.insert(0, record[0][5])
                self.STATISTICAL_MURDER_FLAG_entry.insert(0, record[0][6])
                self.VIC_AGE_GROUP_entry.insert(0, record[0][7])
                self.VIC_SEX_entry.insert(0, record[0][8])
                self.VIC_RACE_entry.insert(0, record[0][9])

                self.result_label.config(text=f"{len(record)} search resultant has been found")
            conn.commit()
            conn.close()


        def get_info(self):
            """
            This function basically is the general function for the processing data in terms of relation with databases.
            Here I am just going to create a new window, whereas will be placed several input entries for the user and
            some buttons as well for simple database working
            :return:
            """
            # todo: ---------------------------------  UI/UX for database window --------------------------------------
            self.new_window = tk.Toplevel()
            self.new_window.geometry("750x500+0+0")
            self.new_window.resizable(False, False)
            self.new_window.config(padx=10, pady=10)
            self.title_Label = tk.Label(self.new_window, text="Database", font=("Sylfaen", 36, 'bold'))
            self.title_Label.grid(row=0, column=1, columnspan=2, pady=10, ipadx=10)



            self.result_label = tk.Label(self.new_window, text="", font=('Sylfaen', 12, 'normal'))
            self.result_label.grid(row=12, column=0, columnspan=2)


            self.INCIDENT_KEY_entry = tk.Entry(self.new_window, width=30)
            self.OCCUR_DATE_entry = tk.Entry(self.new_window, width=30)
            self.OCCUR_TIME_entry = tk.Entry(self.new_window, width=30)
            self.BOROUGH_entry = tk.Entry(self.new_window, width=30)
            self.PRECINCT_entry = tk.Entry(self.new_window, width=30)
            self.JURISDICTION_CODE_entry = tk.Entry(self.new_window, width=30)
            self.STATISTICAL_MURDER_FLAG_entry = tk.Entry(self.new_window, width=30)
            self.VIC_AGE_GROUP_entry = tk.Entry(self.new_window, width=30)
            self.VIC_SEX_entry = tk.Entry(self.new_window, width=30)
            self.VIC_RACE_entry = tk.Entry(self.new_window, width=30)

            self.INCIDENT_KEY_entry.grid(row=1, column=2, padx=10, ipadx=40, columnspan=2)
            self.OCCUR_DATE_entry.grid(row=2, column=2, padx=10, ipadx=40, columnspan=2)
            self.OCCUR_TIME_entry.grid(row=3, column=2, padx=10, ipadx=40, columnspan=2)
            self.BOROUGH_entry.grid(row=4, column=2, padx=10, ipadx=40, columnspan=2)
            self.PRECINCT_entry.grid(row=5, column=2, padx=10, ipadx=40, columnspan=2)
            self.JURISDICTION_CODE_entry.grid(row=6, column=2, padx=10, ipadx=40, columnspan=2)
            self.STATISTICAL_MURDER_FLAG_entry.grid(row=7, column=2, padx=10, ipadx=40, columnspan=2)
            self.VIC_AGE_GROUP_entry.grid(row=8, column=2, padx=10, ipadx=40, columnspan=2)
            self.VIC_SEX_entry.grid(row=9, column=2, padx=10, ipadx=40, columnspan=2)
            self.VIC_RACE_entry.grid(row=10, column=2, padx=10, ipadx=40, columnspan=2)

            VIC_RACE_label = tk.Label(self.new_window, text="VIC_RACE: ")
            VIC_SEX_label = tk.Label(self.new_window, text="VIC_SEX: ")
            VIC_AGE_GROUP_label = tk.Label(self.new_window, text="VIC_AGE_GROUP: ")
            STATISTICAL_MURDER_FLAG_label = tk.Label(self.new_window, text="STATISTICAL_MURDER_FLAG: ")
            JURISDICTION_CODE_label = tk.Label(self.new_window, text="JURISDICTION_CODE: ")
            PRECINCT_label = tk.Label(self.new_window, text="PRECINCT: ")
            BOROUGH_label = tk.Label(self.new_window, text="BOROUGH: ")
            OCCUR_TIME_label = tk.Label(self.new_window, text="OCCUR_TIME: ")
            OCCUR_DATE_label = tk.Label(self.new_window, text="OCCUR_DATE: ")
            INCIDENT_KEY_label = tk.Label(self.new_window, text="INCIDENT_KEY: ")

            INCIDENT_KEY_label.grid(row=1, column=0, padx=10, ipadx=40)
            OCCUR_DATE_label.grid(row=2, column=0, padx=10, ipadx=40)
            OCCUR_TIME_label.grid(row=3, column=0, padx=10, ipadx=40)
            BOROUGH_label.grid(row=4, column=0, padx=10, ipadx=40)
            PRECINCT_label.grid(row=5, column=0, padx=10, ipadx=40)
            JURISDICTION_CODE_label.grid(row=6, column=0, padx=10, ipadx=40)
            STATISTICAL_MURDER_FLAG_label.grid(row=7, column=0, padx=10, ipadx=40)
            VIC_AGE_GROUP_label.grid(row=8, column=0, padx=10, ipadx=40)
            VIC_SEX_label.grid(row=9, column=0, padx=10, ipadx=40)
            VIC_RACE_label.grid(row=10, column=0, padx=10, ipadx=40)

            ADD_btn = tk.Button(self.new_window, width=22, text='Add Record to the database', command=self.add)
            ADD_btn.grid(row=11, column=1, columnspan=2, pady=10, padx=10, ipadx=40)

            SHOW_btn = tk.Button(self.new_window, width=22, text='Find Record', command=self.find_record)
            SHOW_btn.grid(row=12, column=1, columnspan=2, pady=10, padx=10, ipadx=40)

            SHOW_btn = tk.Button(self.new_window, width=22, text='Clear Record', command=self.clear_GUI)
            SHOW_btn.grid(row=13, column=1, columnspan=2, pady=10,  padx=10, ipadx=40)


        @staticmethod
        def search_database(incident_key=None, occur_date=None, occur_time=None, borough=None, precinct=None,
                            jurisdiction_code=None, statistical_murder_flag=None, vic_age_group=None,
                            vic_sex=None, vic_race=None):
            """
            Function is responsible for searching the data into the SQLite3 database and returning list of
            founded ones if they actually exist
             -----------------------------------------------------------------------------------------
            :param incident_key: INCIDENT KEY column value to look for into the database
            :param occur_date: OCCUR_DATE column value to look for into the database
            :param occur_time: OCCUR_TIME column value to look for into the database
            :param borough: BOROUGH column value to look for into the database
            :param precinct: PRECINCT column value to look for into the database
            :param jurisdiction_code: JURISDICTION_CODE column value to look for into the database
            :param statistical_murder_flag: STATISTICAL_MURDER_FLAG column value to look for into the database
            :param vic_age_group: VIC_AGE_GRP column value to look for into the database
            :param vic_sex: VIC_SEX column value to look for into the database
            :param vic_race: VIC_RACE column value to look for into the database
            :return: list of found occurences if actually data according to those parameters has been found. else function
            returns Nonetype object
            """
            # Connect to the database
            conn = sqlite3.connect(database=DATABASE_PATH)
            c = conn.cursor()

            sql = "SELECT * FROM crimes"
            params = []
            conditions = []

            if incident_key:
                conditions.append("INCIDENT_KEY=?")
                params.append(incident_key)
            if occur_date:
                conditions.append("OCCUR_DATE=?")
                params.append(occur_date)
            if occur_time:
                conditions.append("OCCUR_TIME=?")
                params.append(occur_time)
            if borough:
                conditions.append("BOROUGH=?")
                params.append(borough)
            if precinct:
                conditions.append("PRECINCT=?")
                params.append(precinct)
            if jurisdiction_code:
                conditions.append("JURISDICTION_CODE=?")
                params.append(jurisdiction_code)
            if statistical_murder_flag:
                conditions.append("STATISTICAL_MURDER_FLAG=?")
                params.append(statistical_murder_flag)
            if vic_age_group:
                conditions.append("VIC_AGE_GROUP=?")
                params.append(vic_age_group)
            if vic_sex:
                conditions.append("VIC_SEX=?")
                params.append(vic_sex)
            if vic_race:
                conditions.append("VIC_RACE=?")
                params.append(vic_race)
            if conditions:
                sql += " WHERE " + " AND ".join(conditions)
            c.execute(sql, params)
            record = c.fetchall()

            conn.close()
            return record if record else None


        def __write_into_csv__(self):
            """
            whether if the user decides to write the updated data from the database into the data file (.csv file)
            this function is responsible to write them out inside
            :return: None
            """
            conn = sqlite3.connect(database=DATABASE_PATH)
            self.df = pd.read_sql_query("SELECT * FROM crimes", conn)
            self.df.to_csv(FILE_NAME, index=False)
            df_csv = pd.read_csv(FILE_NAME)
            df_new = pd.read_sql_query("SELECT * FROM crimes WHERE INCIDENT_KEY NOT IN (SELECT INCIDENT_KEY FROM crimes)", conn)
            df_combined = pd.concat([df_csv, df_new]).drop_duplicates()
            df_combined.to_csv(FILE_NAME, index=False)
            conn.close()
            return
except FileNotFoundError:
    messagebox.showinfo(title="File Not Found", message="Please check out the data file")
    exit(1)
except sqlite3.OperationalError:
    messagebox.showinfo(title="Database Issue", message="Please make sure that database file exist or it is not damaged")
    exit(1)


