import chartify

df = chartify.examples.example_data()
print(df.head())

ch = chartify.Chart()
ch.plot.scatter(
    data_frame=df,
    x_column='unit_price',
    y_column='total_price'
)
ch.show()