from PyQt5.QtWidgets import * 
import sys , pickle

from PyQt5 import uic, QtWidgets , QtCore, QtGui
import data_visualize , table_display

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("./mainwindow.ui", self)
        
        global data
        data  = data_visualize.data_()
        self.show()
        self.target_value =''
        
        self.Browse = self.findChild( QPushButton, "Browse" )
        self.column_list = self.findChild( QListWidget, "column_list" )
        self.Submit_btn = self.findChild( QPushButton, "Submit" )
        self.target_col = self.findChild( QLabel, "target_col" )
        self.table = self.findChild( QTableView, "tableView" )
        self.data_shape = self.findChild( QLabel, "shape" )
        
        
        self.scaler = self.findChild( QComboBox, "scaler" )
        self.scale_btn = self.findChild( QPushButton, "scale_btn" )
        
        self.cat_column = self.findChild( QComboBox, "cat_column" )
        self.convert_btn = self.findChild( QPushButton, "convert_btn" )
        
        self.drop_column = self.findChild( QComboBox, "drop_column" )
        self.drop_btn = self.findChild( QPushButton, "drop_btn" )
        
        self.empty_column = self.findChild( QComboBox, "empty_column" )
        self.fillmean_btn = self.findChild( QPushButton, "fillmean_btn" )
        self.fillna_btn = self.findChild( QPushButton, "fillna_btn" )
        
        
        
        self.Browse.clicked.connect(self.getCSV)
        self.Submit_btn.clicked.connect(self.set_target)
        self.column_list.clicked.connect(self.target)
        self.convert_btn.clicked.connect(self.convert_cat)
        self.drop_btn.clicked.connect(self.dropc)
        
    def dropc(self):
        name = self.drop_column.currentText()
        if self.target_value == '':
            pass
        else:
            if ( name == self.target_value):
                pass
            
            else:
                self.df = data.drop_columns(self.df,name)
                self.filldetails()
    
    def convert_cat(self):
        name = self.cat_column.currentText()
        self.df[name] = data.convert_category(self.df, name)
        self.filldetails()
    
    def set_target(self):
        self.target_value = str(self.item).split()[0]
        print(self.target_value)
        self.target_col.setText(self.target_value)
        
        
        
        
    def target(self):
        self.item = self.column_list.currentItem().text()
        print(self.item)
        
    def getCSV(self):
        self.filepath , _ = QFileDialog.getOpenFileName(self,"Open File", "C:/apps/ml_7/datasets","csv(*.csv)" )
        # print(self.filepath)
        # self.column_list.addItems(["브라우져", '브라우승', "브라질"])
        self.filldetails(0)
    
    
    def fill_combo_box(self):
        
        self.cat_column.clear()
        self.cat_column.addItems(self.cat_col_list)
        
        self.drop_column.clear()
        self.drop_column.addItems(self.column_arr)
        
        self.empty_column.clear()
        self.empty_column.addItems(self.empty_column_name)
        x = table_display.DataFrameModel(self.df)
        self.table.setModel(x)
        
    def filldetails(self , flag=1):
        if (flag==0):
            self.df = data.read_file(self.filepath)
            # print(self.df)
            
        self.column_list.clear()    
        self.cat_col_list = data.get_cat(self.df)
        self.empty_column_name=data.get_empty_list(self.df)
        
        if len(self.df)==0:
            pass
            
        else:
            
            self.column_arr = data.get_column_list(self.df)
            # print(self.column_arr)
            for i , j in enumerate(self.column_arr):
                stri = f'{j} ------- {str(self.df[j].dtype)}'
                self.column_list.insertItem(i, stri)
        
        df_shape = f'Shape-rows :{self.df.shape[0]} , columns:{self.df.shape[1]}'
        self.data_shape.setText(df_shape)
        
        
        self.fill_combo_box()
        
        
        

if __name__ == '__main__':       
    app = QApplication(sys.argv)
    window = UI()
    app.exec_()