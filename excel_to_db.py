import psycopg2
import pandas as pd
from sqlalchemy import create_engine

def input_data_to_DB(filepath):
    try:
        pgconnect = psycopg2.connect(user= "postgres",
                                    password = "admin",
                                    host = "::1",
                                    port = "5432",
                                    database = "etf_transactions"
                                    )
        
        pgcursor = pgconnect.cursor()
        
        pgcursor.execute("SELECT current_database();")
        print("You are connected to Database: ", pgcursor.fetchone(), "\n")

        excel = pd.ExcelFile(filepath)
        print("Established Excel Object")


        sheet_names = excel.sheet_names
        print("the sheets that will be inputted is: ", sheet_names)

        print("Reading Excel Document...")
        df = pd.read_excel(filepath, sheet_name = None)

        engine = create_engine('postgresql+psycopg2://postgres:admin@localhost/etf_transactions')

        print("Moving data onto the PostgreSQL database.... \n")

        for currentSheet in sheet_names:
            print("Currently importing sheet:", currentSheet, "\n")
            curr_df = df[currentSheet]
            curr_df.to_sql('trial', engine, if_exists='append', index = False)


    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if pgconnect:
            pgcursor.close()
            pgconnect.close()
            print("PostgreSQL connection is closed")



        