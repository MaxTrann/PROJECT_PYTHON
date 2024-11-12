from dataCLEANING import *
from dataCRUD import dataProcessing
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
import seaborn as sns

def ShowMenu():
    print ("+---------------------DATA EXECUTION---------------------+")
    print ("|                    0. Exit Program                     |")
    print ("| 1. Display Data Sheet            4. Delete Data Record |")
    print ("| 2. Add New Data Record           5. Save Data Record   |")
    print ("| 3. Update Data Record            6. Clean Data         |")
    print ("|________________________________________________________|")

def main():
    Data_File = 'student_sleep_patterns.csv'
    # Data_Frame = pd.read_csv(Data_File)
    outfileDataCleaned = "cleaned_student_sleep_patterns.csv"
    Data_Frame = dataProcessing(Data_File)

    while True:
        # Menu
        ShowMenu()

        try:
            Choice = int(input("\nChoose option: "))
            if Choice >= 0 and Choice <= 6:
                # Thoát Chương Trình
                if Choice == 0:
                    print ("Exit Program")
                    break
                
                # Hiện thị Data Frame
                elif Choice == 1:
                    print ("\nData Information")
                    Data_Frame.outputData()

                # Thêm bản ghi dữ liệu
                elif Choice == 2:
                    print ("\nAdd new data record")
                    while True:
                        new_data = input("Enter new comma-separated values' record: ").split(',')
                        if len(new_data) == len(Data_Frame.getSampleData()):
                            Data_Frame.addData(new_data)
                            break
                        else:
                            print ("Invalid field count. Enter data with correct field count.")

                # Cập nhật bản ghi
                elif Choice == 3:
                    print ("\nUpdate data record")
                    while True:
                        Updated_Index = input("Input updated data's index: ")
                        if Updated_Index.isdigit():
                            Updated_Index = int(Updated_Index)
                            if Updated_Index >= 0 and Updated_Index < len(Data_Frame.getData()):
                                break
                            else:
                                print ("\nInvalid input. Please try again")
                        else:
                            print ("\nInvalid input. Please enter a number.")
                    while True:
                        Updated_Data = input("Enter new comma-separated values' record: ").split(',')
                        if len(Updated_Data) == len(Data_Frame.getSampleData()):
                            Data_Frame.updateData(Updated_Index, Updated_Data)
                            break
                        else:
                            print ("Invalid field count. Please enter data with correct field count.")

                # Xóa bản ghi
                elif Choice == 4:
                    print ("\nDelete data record")
                    while True:
                        Deleted_Index = input("Input deleted data's index: ")
                        if Deleted_Index.isdigit():
                            Deleted_Index = int(Deleted_Index)
                            if Deleted_Index >= 0 and Deleted_Index < len(Data_Frame.getData()):
                                break
                            else:
                                print ("Invalid input. Please choose again")
                        else:
                            print ("Invalid input. Please enter a number.")
                    Data_Frame.deleteData(Deleted_Index)

                # Lưu bản ghi
                elif Choice == 5:
                    print ("\nSave data record")
                    Data_Frame.saveData()

                # Làm sạch dữ liệu
                elif Choice == 6:
                    print ("\nClean data")
                    print ("Data Cleaning Options:")
                    print ("1. Statistics of data")
                    print ("2. Sort Data Columns")
                    print ("3. Delete Rows with Missing Data")
                    print ("4. Delete Outliers")

                    while True:
                        try:
                            Clean_Choosing = int(input("Choose your option: "))
                            if Clean_Choosing > 0 and Clean_Choosing < 5:
                                # Đọc dữ liệu từ file
                                Cleaning_Data = loadData(Data_File)

                                if Clean_Choosing == 1:
                                    aggregateData(Cleaning_Data)

                                elif Clean_Choosing == 2:
                                    # Sắp xếp cột dữ liệu
                                    cols = input("Input the column that you want to sort: ")
                                    order = input("Sort in ascending order? (y/n): ").strip().lower() == 'y'
                                    Cleaning_Data = sortDataCol(Cleaning_Data, cols, greater=order)
                                    print("\nData after sorting:")
                                    print(Cleaning_Data)

                                elif Clean_Choosing == 3:
                                    # Xóa các dòng có dữ liệu trống
                                    Cleaning_Data = deleteMissData(Cleaning_Data)
                                    print("\nAfter Deleting Rows with Missing Data:")
                                    print(Cleaning_Data)

                                elif Clean_Choosing == 4:
                                    # Xóa các giá trị ngoại lai
                                    Cleaning_Data = deleteOutliers(Cleaning_Data)
                                    print("\nAfter Removing Outliers:")
                                    print(Cleaning_Data)

                                # Lưu dữ liệu đã xử lý vào file
                                Cleaning_Data.to_csv(outfileDataCleaned, index=False)
                                print("Data is saved in 'cleaned_student_sleep_patterns.csv'.")
                                break
                            else:
                                print ("\nInvalid input. Please choose again")
                                continue
                        except ValueError:
                            print ("\nInvalid input. Please enter a number")
            else:
                print ("\nInvalid input. Please choose again")
                continue
        except ValueError:
            print ("\nInvalid input. Please enter a number")

if __name__ == "__main__":
    main()
