from PyQt5.QtWidgets import *
import sys, pickle

from PyQt5 import uic, QtWidgets, QtCore, QtGui
import data_visualize, table_display

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("./mainwindow.ui", self)
        global data #초기 지정 data를 어디서나 쓸 수 있음
        data = data_visualize.data_()
        self.show()

        self.Browse = self.findChild(QPushButton, "Browse")
        self.column_list = self.findChild(QListWidget, "column_list")
        self.Submit_btn = self.findChild(QPushButton, "Submit")
        self.target_col = self.findChild(QLabel, "target_col")
        self.table = self.findChild(QTableView, "tableView")
        self.data_shape = self.findChild(QLabel, "shape")
        self.cat_column = self.findChild(QComboBox, "cat_column")
        self.scaler = self.findChild(QComboBox, "scaler")
        self.drop_column = self.findChild(QComboBox, "drop_column")
        self.empty_column = self.findChild(QComboBox, "empty_column")
        self.scale_btn = self.findChild(QPushButton, "scale_btn")
        self.drop_btn = self.findChild(QPushButton, "drop_btn")
        self.fillmean_btn = self.findChild(QPushButton, "fillmean_btn")
        self.fillna_btn = self.findChild(QPushButton, "fillna_btn")
        self.convert_btn = self.findChild(QPushButton, "convert_btn")
        # 버튼 클릭
        self.Browse.clicked.connect(self.getCSV)
        self.Submit_btn.clicked.connect(self.set_target)
        self.column_list.clicked.connect(self.target)
    def target(self):
        self.item = self.column_list.currentItem().text() # 클릭한 상태의 데이터가 저장
        print(self.item)

    def set_target(self):
        self.target_value = str(self.item).split()[0]
        print(self.target_value)
        self.target_col.setText(self.target_value)
    def getCSV(self):
        self.filepath , _ = QFileDialog.getOpenFileName(self, "Open File", "C:/Users/Sejin/Documents/GitHub/ubion_ml/datasets", "CSV(*.CSV)")
        # 주소 적은 뒤 \가 아닌 /로 변경
        # "CSV(*.CSV)" : CSV파일만 보이기
        # 파일 경로 가져오는 것
        # print(self.filepath)
        # self.column_list.clear() # 계속 버튼 눌렀을 때 그 전꺼 지우는 코드
        # self.column_list.addItems(["브라우져", "브라우승", "브라질"])
        self.filldetails(0)
    def fill_combo_box(self):
        x = table_display.DataFrameModel(self.df)
        self.table.setModel(x)

    def filldetails(self, flag=1):
        
        if (flag==0):
            self.df = data.read_file(self.filepath)
        self.column_list.clear()

        if len(self.df) == 0:
            pass
        else:
            self.column_arr = data.get_column_list(self.df)
            for i , j in enumerate(self.column_arr):
                stri = f'{j} ------- {str(self.df[j].dtype)}'
                self.column_list.insertItem(i, stri)
        df_shape = f'Shape-rows : {self.df.shape[0]}, columns:{self.df.shape[1]}'
        self.data_shape.setText(df_shape)
        self.fill_combo_box()

if __name__ == '__main__': # 가장 먼저 실행
    app = QApplication(sys.argv)
    window = UI()
    app.exec_()