import chartify

df = chartify.examples.example_data()
print(df.head())

ch = chartify.Chart(blank_labels=True) #blank_labels可以控制圖表label的預設是否隱藏
ch.plot.scatter(
    data_frame=df,
    x_column='unit_price',
    y_column='total_price'
)
ch.set_title('水果單價與總價格關係')
# ch.set_subtitle('Chartify 內建數據')
# ch.set_source_label('Chartify')
ch.axes.set_xaxis_label('單價')
ch.axes.set_yaxis_label('總價格')

ch.show()