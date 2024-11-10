import pandas as pd

# Hàm 0: Đọc dữ liệu từ file csv và trả về một DataFrame
def loadData(filePath):
    return pd.read_csv(filePath)

# Hàm 1: Thống kê dữ liệu của file
def aggregateData(data):
    print("Thống kê các giá trị có trong file:")
    for col in data.columns:
        print(f"\nThông tin về cột {col}': ")
        print(data[col].value_counts())
        
# Hàm 2: Sắp xếp dữ liệu theo cột
# data: dữ liệu cần xử lí, cols: những cột cần sort, greater=True(default): True là sắp xếp tăng dần, False là sắp xếp giảm dần
def sortDataCol(data, cols, greater=True):
    sortedData = data.sort_values(by=cols, ascending=greater)
    return sortedData

# Hàm 3: Hàm để loại bỏ những dòng bị thiếu dữ liệu NULL (NaN)
def deleteMissData(data):
    dataCleaned = data.dropna(axis=0)
    return dataCleaned
    
# Hàm 4: Xử lí các số liệu ngoại lai 
def deleteOutliers(data):
    validGenders = ['Male', 'Female', 'Other']
    data = data[data['Gender'].isin(validGenders)] # Những cú pháp hợp lệ của gender
    data = data[data['Student_ID'] >= 0] # ID phải lớn hơn 0
    data = data[data['Age'] >= 18] # tuổi của sinh viên đại học phải >= 18
    return data


def main():
    fileData = "student_sleep_patterns.csv"
    outfileDataCleaned = "cleaned_student_sleep_patterns.csv"
    
    # Step1: Đọc dữ liệu từ fileData
    data = loadData(fileData)
    
    # Step2: Thống kê dữ liệu
    aggregateData(data)
    
    # Step3: Loại bỏ những dòng bị thiếu dữ liệu 
    dataCleaned = deleteMissData(data)
    
    # Step4: Xử lí những giá trị ngoại loại
    dataCleaned = deleteOutliers(dataCleaned)
    
    
    # Step6: Sắp xếp dữ liệu của cột Age và Sleep_Quality
    cols = ['Age']
    sortedData = sortDataCol(dataCleaned, cols)
    print("Dữ liệu sau khi sắp xếp: ")
    print(sortedData)
    
    # Lưu dữ liệu đã được xử lí vào csv mới
    sortedData.to_csv(outfileDataCleaned, index=False) # xuất ra file mới ko có chỉ số cột
    print(f"Dữ liệu đã được cập nhật vào file {outfileDataCleaned} thành công!")
    
    
main()
    