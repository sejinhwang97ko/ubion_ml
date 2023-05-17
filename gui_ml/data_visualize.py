import pandas as pd


class data_:
    def read_file(self, filepath):
        if str(filepath) == '':
            return ''
        else:
            return pd.read_csv(str(filepath), index_col=0)

    def get_column_list(self, df):
        return list(df.columns)