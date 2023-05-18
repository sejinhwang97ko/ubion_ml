import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler, PowerTransformer
import matplotlib.pyplot as plt

class data_:
    def read_file(self, filepath):
        if str(filepath) == '':
            return ''
        else:
            return pd.read_csv(str(filepath), index_col=False)

    def get_column_list(self, df):
        return list(df.columns)

    def get_cat(self, df):
        cat_col=[x for x in df.columns if df[x].dtype=='object']
        return cat_col

    def convert_category(self, df, column_name):
        le = LabelEncoder()
        df[column_name] = le.fit_transform(df[column_name])
        return df[column_name]

    def drop_columns(self, df, column_name):
        return df.drop(column_name, axis=1)

    def get_empty_list(self, df):
        empty_list=[x for x in df.columns if df[x].isnull().values.any()]
        return empty_list

    def fillmean(self, df, column_name):
        df[column_name] = df[column_name].fillna(df[column_name].mean())
        return df[column_name]

    def fillnan(self, df, column_name):
        df[column_name] = df[column_name].fillna("Unknown")
        return df[column_name]

    def StandardScaler(self, df, target_name):
        sc = StandardScaler()
        X = df.drop(target_name, axis=1)
        scaled_features = sc.fit_transform(X)
        scaled_features_df = pd.DataFrame(scaled_features, index=X.index, columns=X.columns)
        scaled_features_df[target_name] = df[target_name]
        return scaled_features_df
    def MinMaxScaler(self, df, target_name):
        mc = MinMaxScaler()
        X = df.drop(target_name, axis=1)
        scaled_features = mc.fit_transform(X)
        scaled_features_df = pd.DataFrame(scaled_features, index=X.index, columns=X.columns)
        scaled_features_df[target_name] = df[target_name]
        return scaled_features_df
    def PowerTransformer(self, df, target_name):
        pc = PowerTransformer()
        X = df.drop(target_name, axis=1)
        scaled_features = pc.fit_transform(X)
        scaled_features_df = pd.DataFrame(scaled_features, index=X.index, columns=X.columns)
        scaled_features_df[target_name] = df[target_name]
        return scaled_features_df

    def scatter_graph(self, df, x, y, c, marker):
        plt.figure()
        plt.scatter(df[x], df[y], c=c, marker=marker)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f'{y} vs {x}')
        plt.show()

    def line_graph(self, df, x, y, c, marker):
        plt.figure()
        df = df.sort_values(by=[x])
        plt.plot(df[x], df[y], c=c, marker=marker)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f'{y} vs {x}')
        plt.show()

