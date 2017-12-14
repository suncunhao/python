
import pandas as pd
import re

data = pd.read_clipboard()
columns = data.columns
base_columns = ['是否属于白名单', '经销商名称']

result = []
for year in ['14', '15', '16', '17']:
    select_data = data[base_columns + [col for col in columns if year in col]]
    select_data.columns =[re.sub(r'\d+', '', col) for col in select_data.columns]
    select_data.insert(0, 'year', '20'+year)
    result.append(select_data)

result_df = pd.concat(result, ignore_index=True)
result_df = result_df[[
    'year', '是否属于白名单', '经销商名称', '销售总指标', '财务总指标',
    '授信比例', '年初信用额', '信用额', '备注', '信用等级'
]]
# result_df.to_clipboard()
result_df.to_csv('data_output/20171123/shouxinzhibiao.csv')


def f(x):
    try:
        return float(re.sub(',', '', x))
    except Exception:
        print(x)
        raise

# client_balance
client_balance = pd.read_clipboard()
client_balance['receivable'] = client_balance['receivable'].fillna('0')
client_balance['receivable'] = client_balance['receivable'].apply(
    lambda x: float(re.sub(',', '', x))
)


df = client_balance[client_balance.receivable > 0 & (client_balance.document_type == '发货单')][['year', 'month', 'client_name', 'receivable']]
df2 = df.groupby(['year', 'month', 'client_name']).sum().reset_index()
df2.to_clipboard()