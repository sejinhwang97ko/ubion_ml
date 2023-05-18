import pandas as pd
from sklearn.preprocessing import LabelEncoder


class data_:
    
    def read_file(self , filepath):
        if str(filepath)=='':
            return ""
        else:
            return pd.read_csv(str(filepath) , index_col=False )
            

    def get_column_list(self , df):
        # print(list(df.columns))
        # columnname_list=[]
        # for i in df.columns:
        #     columnname_list.append(i)
        return list(df.columns)
    
    def get_cat(self, df):
        cat_col=[x for x in df.columns if df[x].dtype=='object']
        # cat_col=[]
        # for i in df.columns:
        #     if (df[i].dtype=='object'):
        #         cat_col.append(i)
        return cat_col

    def convert_category(self, df ,column_name):
        le = LabelEncoder()
        df[column_name]= le.fit_transform(df[column_name])
        return df[column_name]
    
    def drop_columns(self , df , column_name):
        return df.drop(column_name, axis=1)
    
    def get_empty_list(self , df):
        empty_list=[x for x in df.columns if df[x].isnull().values.any()]    
        return empty_list