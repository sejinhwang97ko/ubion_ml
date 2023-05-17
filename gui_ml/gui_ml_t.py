from PyQt5.QtWidgets import * 
import sys , pickle

from PyQt5 import uic, QtWidgets , QtCore, QtGui
import data_visualize

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("./mainwindow.ui", self)
        
        global data
        data  = data_visualize.data_()
        self.show()
        
        self.Browse = self.findChild( QPushButton, "Browse" )
        self.column_list = self.findChild( QListWidget, "column_list" )
        self.Submit_btn = self.findChild( QPushButton, "Submit" )
        
        self.Browse.clicked.connect(self.getCSV)
        self.Submit_btn.clicked.connect(self.set_target)
        self.column_list.clicked.connect(self.target)
    
    def target(self):
        self.item = self.column_list.currentItem().text()
        print(self.item)
        
    def getCSV(self):
        self.filepath , _ = QFileDialog.getOpenFileName(self,"Open File", "C:/apps/ml_7/datasets","csv(*.csv)" )
        # print(self.filepath)
        # self.column_list.addItems(["브라우져", '브라우승', "브라질"])
        self.filldetails(0)
    
    
    
    def filldetails(self , flag=1):
        if (flag==0):
            self.df = data.read_file(self.filepath)
            print(self.df)
        self.column_list.clear()
        
        if len(self.df)==0:
            pass
            
        else:
            
            self.column_arr = data.get_column_list(self.df)
            # print(self.column_arr)
            for i , j in enumerate(self.column_arr):
                stri = f'{j} ------- {str(self.df[j].dtype)}'
                self.column_list.insertItem(i, stri)
        
        
        
        

if __name__ == '__main__':       
    app = QApplication(sys.argv)
    window = UI()
    app.exec_()