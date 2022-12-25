import panel as pn

pn.extension()

window = pn.widgets.IntSlider(name='window', value=30, start=1, end=60)
sigma = pn.widgets.FloatSlider(name='sigma', value=10, start=0, end=20)

interactive = pn.bind("insert_find_outliers_fn", window=window, sigma=sigma)
