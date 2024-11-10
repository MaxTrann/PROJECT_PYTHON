import csv
import pandas as pd 

class dataProcessing:
    def __init__(self, filePath):
        self.filePath = filePath
        self.data = self.getData() # Lấy dữ liệu từ file csv
        
    def getData(self):
        # Các bước để tải dữ liệu từ file csv
        data = [] # tạo một danh sách để chứa các dòng dữ liệu 
        try:
            with open(self.filePath, mode = 'r', newline='', encoding='utf-8') as filecsv:
                readData = csv.reader(filecsv)
                for row in readData:
                    data.append(row)
        except FileNotFoundError:
            print(f"File {self.filePath} lỗi không tồn tại!")
        return data
    
    def outputData(self):
        print(pd.DataFrame(self.data)) # in dưới dạng data frame của pandas
        
    def getSampleData(self): # trả về bản ghi đầu tiên của dữ liệu để lấy đó làm mẫu
        if self.data:
            return self.data[0]
        return []
    
    def addData(self, newData):
        self.data.append(newData)
        print("Dữ liệu đã được thêm!")
        
    def updateData(self, index, newData):
        if index >= 0 and index < len(self.data):
            self.data[index] = newData
            print("Dữ liệu đã được cập nhật!")
        else:
            print("Vị trí thêm không hợp lệ!")
            
    def deleteData(self, index):
        if index >= 0 and index < len(self.data):
            self.data.pop(index)
            print("Dữ liệu đã được xóa!")
        else:
            print("Vị trí xóa không hợp lệ!")
        
    def saveData(self):
        # Lưu dữ liệu vào file csv
        with open(self.filePath, mode='w', newline='', encoding='utf-8') as filecsv:
            write = csv.writer(filecsv)
            write.writerows(self.data)
        print("Dữ liệu đã được lưu thành công!")

    