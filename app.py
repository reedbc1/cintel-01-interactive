import matplotlib.pyplot as plt
import numpy as np
from shiny.express import input, render, ui

# adding title
ui.page_opts(title = "PiShiny App with Plots", fillable=True)

# generating random data
# define number of data points
def generate_data():
    count_of_points: int = 400
    # set seed so that data can be reproduced
    np.random.seed(3)
    # generate random data array
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    return random_data_array

random_data_array = generate_data()

# creating UI sidebar slider input
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of bins", 0, 100, 20)

with ui.card(full_screen=True):
    ui.card_header("Density Histogram")
    @render.plot(alt="A histogram showing a random data distribution")
    def histogram():
        # create plot
        # 1st argument: data
        # 2nd argument: input.input_label_name()
        # 3rd argument: density (True makes the graph a probability density function)
        plt.hist(random_data_array, input.selected_number_of_bins(), density=True, color="purple")

with ui.card(full_screen=True):
    ui.card_header("Scatterplot")
    @render.plot(alt="A scatterplot showing a random data distribution")
    def scatterplot():
        x = list(range(1,401))
        y = random_data_array
        plt.scatter(x, y, color="purple")
