import tkinter as tk
from tkinter import ttk, Frame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class YouTubeView(tk.Tk):
    """
    Represent a main window of 'YouTube Trend Analysis' application.
    """
    def __init__(self, controller):
        """
        Initialize a YouTubeView object.
        :param controller: The controller object for managing the GUI.
        """
        super().__init__()
        self.title('YouTube Trend Analysis')
        self.configure(bg='#f8f6f2')
        self.controller = controller
        self.canvas = None
        self.fig = None
        self.check_menu = None
        self.init_component()

    def init_component(self):
        """
        Set up the main component of 'YouTube Trend Analysis' application
        and also create component of the home page,
        story page, menu graph page, and suggest page .
        :return: None
        """
        self.top_frame = Frame(self, bg='#f8f6f2', height=130, highlightbackground='#cd3c3c',
                               highlightthickness=4)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        self.menu_page = Frame(self, bg='#f1e8d7')
        self.menu_page.pack(side=tk.LEFT, anchor='w', fill=tk.Y)
        self.name = tk.Label(self.top_frame, text='YouTube Trend Analysis', font=('BM Jua', 70),
                             fg='#cd3c3c', bg='#f8f6f2')
        self.name.pack(fill=tk.X, expand=True)
        self.home_button = tk.Button(self.menu_page, text='Home', font=('BM Jua', 20), bd=0,
                                     fg='#cd3c3c', width=10)
        self.home_button.pack(side=tk.TOP, padx=10, pady=40)

        self.story_button = tk.Button(self.menu_page, text='Story Telling', font=('BM Jua', 20),
                                      bd=0, fg='#cd3c3c', width=10)
        self.story_button.pack(side=tk.TOP, padx=10, pady=40)

        self.create_button = tk.Button(self.menu_page, text='Create Graph', font=('BM Jua', 20),
                                      bd=0, fg='#cd3c3c', width=10)
        self.create_button.pack(side=tk.TOP, padx=15, pady=40)

        self.suggest_button = tk.Button(self.menu_page, text='Suggest Channel', font=('BM Jua', 20),
                                      bd=0, fg='#cd3c3c', width=10)
        self.suggest_button.pack(side=tk.TOP, padx=15, pady=40)

        self.exit_button = tk.Button(self.menu_page, text='Exit', font=('BM Jua', 20),
                                      bd=0, fg='#cd3c3c', width=10, command=self.exit_app)
        self.exit_button.pack(side=tk.BOTTOM, padx=10, pady=40)
        self.show_menu = Frame(self, bg='#f8f6f2', width=900)
        self.create_home_page()
        self.show_home_page()
        self.create_story_page()
        self.create_menu_graph_page()
        self.create_suggest_page()

    def create_home_page(self):
        """
        Set up components of home menu.
        :return: None
        """
        self.home_frame = Frame(self.show_menu, bg='#f8f6f2',
                                width=900)
        self.welcome_label = tk.Label(self.home_frame, text="Welcome to YouTube Trend Analysis!\n "
                                                            "This app is for "
                                                            "people who want to create their own "
                                                            "channels. Let's "
                                                            "explore!",
                                      font=('BM Jua', 25), bg='#f1e8d7', fg='#cd3c3c', height=5)
        self.welcome_label.pack(side=tk.TOP, padx=30, pady=30, fill=tk.X, expand=True)
        self.home_icon = tk.PhotoImage(file='home_icon.png')
        self.home_label = tk.Label(self.home_frame, image=self.home_icon, bg='#f8f6f2')
        self.home_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20, pady=20)

    def show_home_page(self):
        """
        Display home menu.
        :return: None
        """
        self.clear_menu()
        self.home_frame.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.show_menu.pack(side=tk.TOP, anchor='w', fill=tk.X, expand=True)

    def create_story_page(self):
        """
        Set up components of 'story telling' menu.
        :return: None
        """
        self.story_frame = Frame(self.show_menu, bg='#f8f6f2', width=900)
        self.story_menu_frame = Frame(self.story_frame, bg='#cd3c3c', height=80)
        self.story_menu_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.show_graph_frame = Frame(self.story_frame, bg='#f8f6f2', width=200, height=700)
        self.show_graph_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.table_frame = Frame(self.show_graph_frame, width=650, height=680)
        self.create_table()
        self.story_canvas = tk.Canvas(self.show_graph_frame, bg='red', width=400, height=400)
        self.story_canvas.pack(side=tk.TOP, anchor='w',
                               fill=tk.BOTH, expand=True)
        self.corr_button = tk.Button(self.story_menu_frame, text='Correlation', width=15, height=1,
                                     font=('BM Jua', 20),
                                     bd=0, fg='#cd3c3c')
        self.corr_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=52, pady=5)
        self.year_trend_button = tk.Button(self.story_menu_frame, text='Year Trend',
                                           width=15, height=1,
                                           font=('BM Jua', 20), bd=0, fg='#cd3c3c')
        self.year_trend_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=52, pady=5)
        self.avg_earning_button = tk.Button(self.story_menu_frame, text='Average Earning',
                                            width=15, height=1,
                                            font=('BM Jua', 20), bd=0, fg='#cd3c3c')
        self.avg_earning_button.pack(side=tk.LEFT, fill=tk.X,
                                     expand=True, padx=52, pady=5)
        self.descriptive_button = tk.Button(self.story_menu_frame, text='Descriptive',
                                            width=15, height=1,
                                            font=('BM Jua', 20), bd=0, fg='#cd3c3c')
        self.descriptive_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=52, pady=5)

    def show_story_page(self):
        """
        Display story telling menu.
        :return: None
        """
        self.clear_menu()
        self.story_frame.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
        self.show_menu.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)

    def create_menu_graph_page(self):
        """
        Set up components of 'create graph' menu and also set up components for selecting
        different types of graphs such as histogram, scatter graph, pie chart, and bar graph
        :return: None
        """
        self.select_type_frame = Frame(self.show_menu, bg='#f8f6f2')
        self.select_first_row = Frame(self.select_type_frame, bg='#f8f6f2')
        self.select_first_row.pack(side=tk.TOP, fill=tk.X, expand=True, padx=0)
        self.select_second_row = Frame(self.select_type_frame, bg='#f8f6f2')
        self.select_second_row.pack(side=tk.TOP, fill=tk.X, expand=True, padx=0)
        self.create_graph_canvas = tk.Canvas(self.select_type_frame, bg='red',
                                             width=400, height=400)
        self.create_graph_canvas.pack(side=tk.BOTTOM, anchor='w', fill=tk.BOTH, expand=True)

        self.hist_icon = tk.PhotoImage(file='histogram_icon.png')
        self.hist_button = tk.Button(self.select_first_row, image=self.hist_icon)
        self.hist_button.pack(side=tk.LEFT, expand=True)
        self.hist_label = tk.Label(self.select_first_row, text='Histogram',
                                   bg='#cd3c3c', fg='#f8f6f2',
                                   font=('BM Jua', 22), width=30, height=2)
        self.hist_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=30)

        self.scatter_icon = tk.PhotoImage(file='scatter_icon.png')
        self.scatter_button = tk.Button(self.select_first_row, image=self.scatter_icon)
        self.scatter_button.pack(side=tk.LEFT, expand=True)
        self.scatter_label = tk.Label(self.select_first_row, text='Scatter Graph',
                                      bg='#cd3c3c', fg='#f8f6f2',
                                      font=('BM Jua', 22), width=30, height=2)
        self.scatter_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=30)

        self.pie_icon = tk.PhotoImage(file='pie_icon.png')
        self.pie_button = tk.Button(self.select_second_row, image=self.pie_icon)
        self.pie_button.pack(side=tk.LEFT, expand=True)
        self.pie_label = tk.Label(self.select_second_row, text='Pie Chart',
                                  bg='#cd3c3c', fg='#f8f6f2',
                                  font=('BM Jua', 22), width=30, height=2)
        self.pie_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=30)

        self.bar_icon = tk.PhotoImage(file='bar_icon.png')
        self.bar_button = tk.Button(self.select_second_row, image=self.bar_icon)
        self.bar_button.pack(side=tk.LEFT, expand=True)
        self.bar_label = tk.Label(self.select_second_row, text='Bar Graph',
                                  bg='#cd3c3c', fg='#f8f6f2',
                                  font=('BM Jua', 22), width=30, height=2)
        self.bar_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=30)

        self.hist_selected()
        self.bar_selected()
        self.scatter_selected()
        self.pie_selected()

    def hist_selected(self):
        """
        Set up components for selecting a histogram.
        :return: None
        """
        self.show_hist_frame = Frame(self.select_type_frame, bg='#f8f6f2')
        self.select_hist_label = tk.Label(self.show_hist_frame,
                                          text='Select attribute to see histogram',
                                          font=('BM Jua', 22), fg='#cd3c3c', bg='#f1e8d7')
        self.select_hist_label.pack(side=tk.LEFT, padx=15, pady=15)
        self.select_hist_att = ttk.Combobox(self.show_hist_frame, state='readonly', width=30)
        self.select_hist_att['values'] = ['Subscribers', 'Video views', 'Average monthly earnings']
        self.select_hist_att.current(newindex=0)
        self.select_hist_att.pack(side=tk.LEFT, padx=5)

    def scatter_selected(self):
        """
        Set up components for selecting a scatter plot.
        :return: None
        """
        self.show_scatter_frame = Frame(self.select_type_frame, bg='#f8f6f2')
        self.select_scatter_label = tk.Label(self.show_scatter_frame,
                                             text='Select attribute to see scatter graph',
                                             font=('BM Jua', 22), fg='#cd3c3c', bg='#f1e8d7')
        self.select_scatter_label.pack(side=tk.LEFT, padx=15, pady=15)
        self.select_scatter_att_1 = ttk.Combobox(self.show_scatter_frame,
                                                 width=20, state='readonly')
        self.select_scatter_att_1['values'] = ['Subscribers', 'Video views', 'Uploaded videos',
                                               'Average monthly earnings']
        self.select_scatter_att_1.current(newindex=0)
        self.select_scatter_att_1.pack(side=tk.LEFT, padx=5)
        self.select_scatter_att_2 = ttk.Combobox(self.show_scatter_frame,
                                                 width=20, state='readonly')
        self.select_scatter_att_2['values'] = ['Subscribers', 'Video views', 'Uploaded videos',
                                               'Average monthly earnings']
        self.select_scatter_att_2.current(newindex=0)
        self.select_scatter_att_2.pack(side=tk.LEFT, padx=5)

    def pie_selected(self):
        """
        Set up components for selecting a pie chart.
        :return: None
        """
        self.show_pie_frame = Frame(self.select_type_frame, bg='#f8f6f2')
        self.select_pie_label = tk.Label(self.show_pie_frame, text='Category created in the year',
                                         font=('BM Jua', 22), fg='#cd3c3c', bg='#f1e8d7')
        self.select_pie_label.pack(side=tk.LEFT, padx=15, pady=15)
        self.select_pie_att = ttk.Combobox(self.show_pie_frame, width=20, state='readonly')
        self.select_pie_att['values'] = ['2005', '2006', '2007', '2008', '2009', '2010',
                                         '2011', '2012', '2013', '2014',
                                         '2015', '2016', '2017', '2018', '2019',
                                         '2020', '2021', '2022']
        self.select_pie_att.current(newindex=0)
        self.select_pie_att.pack(side=tk.LEFT, padx=5)

    def bar_selected(self):
        """
        Set up components for selecting a bar graph.
        :return: None
        """
        self.show_bar_frame = Frame(self.select_type_frame, bg='#f8f6f2')
        self.select_bar_label = tk.Label(self.show_bar_frame, text='See average of',
                                          font=('BM Jua', 22), fg='#cd3c3c', bg='#f1e8d7')
        self.select_bar_label.pack(side=tk.LEFT, padx=15, pady=15)
        self.select_bar_att = ttk.Combobox(self.show_bar_frame, width=20, state='readonly')
        self.select_bar_att['values'] = ['Subscribers', 'Video views',
                                         'Uploaded videos', 'Average monthly earnings']
        self.select_bar_att.current(newindex=0)
        self.select_bar_att.pack(side=tk.LEFT, padx=5)
        self.select_bar_label_2 = tk.Label(self.show_bar_frame, text='for each category',
                                           font=('BM Jua', 22), fg='#cd3c3c', bg='#f1e8d7')
        self.select_bar_label_2.pack(side=tk.LEFT, padx=5)

    def show_create_graph_page(self, num, event):
        """
        Displays the menu based on the user-selected option. It clears any previous menu
        components, sets up the new menu components based on the selected option.
        :param num: The number representing the menu selection.
        :return: None
        """
        self.clear_menu()
        self.clear_previous()
        self.select_type_frame.pack(side=tk.TOP, anchor='w', fill=tk.X, expand=True)
        self.show_menu.pack(side=tk.LEFT, anchor='w', fill=tk.BOTH, expand=True)
        if num == 1:
            self.clear_menu()
            self.show_create_hist()
            self.check_menu = 'histogram'
        elif num == 2:
            self.clear_menu()
            self.show_create_scatter()
            self.check_menu = 'scatter'
        elif num == 3:
            self.clear_menu()
            self.show_create_pie()
            self.check_menu = 'pie'
        elif num == 4:
            self.clear_menu()
            self.show_create_bar()
            self.check_menu = 'bar'

    def clear_previous(self):
        """
        Clears any previous menu components.
        :return: None
        """
        if self.check_menu == 'histogram':
            self.show_hist_frame.pack_forget()
        elif self.check_menu == 'scatter':
            self.show_scatter_frame.pack_forget()
        elif self.check_menu == 'pie':
            self.show_pie_frame.pack_forget()
        elif self.check_menu == 'bar':
            self.show_bar_frame.pack_forget()

    def show_create_hist(self):
        """
        Displays the components for creating a histogram.
        :return: None
        """
        self.select_type_frame.pack(side=tk.TOP, anchor='w', fill=tk.X, expand=True)
        self.show_hist_frame.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
        self.show_menu.pack(side=tk.LEFT, anchor='w', fill=tk.BOTH, expand=True)

    def show_create_scatter(self):
        """
        Displays the components for creating a scatter graph.
        :return: None
        """
        self.select_type_frame.pack(side=tk.TOP, anchor='w', fill=tk.X, expand=True)
        self.show_scatter_frame.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
        self.show_menu.pack(side=tk.LEFT, anchor='w', fill=tk.BOTH, expand=True)

    def show_create_pie(self):
        """
        Displays the components for creating a pie chart.
        :return: None
        """
        self.select_type_frame.pack(side=tk.TOP, anchor='w', fill=tk.X, expand=True)
        self.show_pie_frame.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
        self.show_menu.pack(side=tk.LEFT, anchor='w', fill=tk.BOTH, expand=True)

    def show_create_bar(self):
        """
        Displays the components for creating a bar graph.
        :return: None
        """
        self.select_type_frame.pack(side=tk.TOP, anchor='w', fill=tk.X, expand=True)
        self.show_bar_frame.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
        self.show_menu.pack(side=tk.LEFT, anchor='w', fill=tk.BOTH, expand=True)

    def create_suggest_page(self):
        """
        Set up components for 'suggest channel' menu.
        :return: None
        """
        self.suggest_frame = Frame(self.show_menu, bg='#f8f6f2')
        self.suggest_label = tk.Label(self.suggest_frame, text="This menu will suggest a YouTube"
                                                               " channel in a category "
                                                               "you're"
                                                               " interested in, \nso you can "
                                                               "explore how those "
                                                               "YouTubers "
                                                               "engage their audience effectively.",
                                      font=('BM Jua', 22), fg='#cd3c3c', bg='#f1e8d7')
        self.suggest_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20, pady=20)
        self.suggest_select_frame = Frame(self.suggest_frame, bg='#f8f6f2')
        self.suggest_select_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20, pady=20)
        self.select_suggest_label = tk.Label(self.suggest_select_frame, text='Select category',
                                          font=('BM Jua', 22), fg='#f1e8d7', bg='#cd3c3c')
        self.select_suggest_label.pack(side=tk.LEFT, anchor='w', padx=15)
        self.select_suggest_att = ttk.Combobox(self.suggest_select_frame,
                                               state='readonly', width=30)
        unique_category = self.controller.get_unique_category()
        not_use = ['Education', 'Sports', 'People & Blogs', 'Shows',
                   'Other', 'Movies', 'Pets & Animals',
                   'Autos & Vehicles', 'Travel & Events',
                   'Nonprofits & Activism', 'Trailers']
        self.select_suggest_att['values'] = [category for category in
                                             unique_category if category not in not_use]
        self.select_suggest_att.current(newindex=0)
        self.select_suggest_att.pack(side=tk.LEFT, anchor='w', padx=5)
        self.select_suggest_from = Frame(self.suggest_frame, bg='#f8f6f2')
        self.from_sub = tk.Button(self.select_suggest_from,
                                  text='Top 10 by Subscribers', font=('BM Jua', 22),
                                  fg='#cd3c3c', width=25)
        self.from_sub.pack(side=tk.LEFT, anchor='w', padx=15, fill=tk.X, expand=True)
        self.from_view = tk.Button(self.select_suggest_from,
                                   text='Top 10 by Video views', font=('BM Jua', 22),
                                   fg='#cd3c3c', width=25)
        self.from_view.pack(side=tk.LEFT, anchor='w', padx=15, fill=tk.X, expand=True)
        self.select_suggest_from.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20)
        self.suggest_canvas = tk.Canvas(self.suggest_frame, bg='red', width=400, height=400)
        self.suggest_canvas.pack(side=tk.BOTTOM, anchor='e', fill=tk.BOTH, expand=True)

    def show_suggest_page(self):
        """
        Display suggest channel menu.
        :return: None
        """
        self.clear_menu()
        self.suggest_frame.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)
        self.show_menu.pack(side=tk.TOP, anchor='w', fill=tk.BOTH, expand=True)

    def display_graph(self, fig, graph):
        """
        Display the graph on the canvas.
        :param fig: The matplotlib figure object.
        :param graph: The canvas that will display graph.
        :return: None
        """
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, master=graph)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        plt.close(fig)

    def clear_menu(self):
        """
        Clear all widget from the menu frame.
        :return: None
        """
        for w in self.show_menu.winfo_children():
            w.pack_forget()

    def create_table(self):
        """
        Create table to display descriptive and statistic of data.
        :return: None
        """
        df = self.controller.get_data()
        df_to_describe = df[['subscribers', 'video views', 'uploads', 'average_monthly_earnings']]
        summary_stats = df_to_describe.describe(percentiles=[.25, .50, .75])
        mean = summary_stats.loc['mean'].to_list()
        std = summary_stats.loc['std'].to_list()
        min_val = summary_stats.loc['min'].to_list()
        max_val = summary_stats.loc['max'].to_list()
        attribute = ['Subscribers', 'Video views', 'Uploaded videos', 'Average monthly earnings']
        header1 = tk.Label(self.table_frame, text="Attribute", padx=10,
                           pady=5, borderwidth=1, relief="solid",
                           width=15, height=2, font=('BM Jua', 20),
                           bg='#f1e8d7', fg='#cd3c3c')
        header2 = tk.Label(self.table_frame, text="Mean", padx=10,
                           pady=5, borderwidth=1, relief="solid",
                           width=15, height=2, font=('BM Jua', 20),
                           bg='#f1e8d7', fg='#cd3c3c')
        header3 = tk.Label(self.table_frame, text="Std", padx=10,
                           pady=5, borderwidth=1, relief="solid",
                           width=15, height=2, font=('BM Jua', 20),
                           bg='#f1e8d7', fg='#cd3c3c')
        header4 = tk.Label(self.table_frame, text="Min", padx=10,
                           pady=5, borderwidth=1, relief="solid",
                           width=15, height=2, font=('BM Jua', 20),
                           bg='#f1e8d7', fg='#cd3c3c')
        header5 = tk.Label(self.table_frame, text="Max", padx=10,
                           pady=5, borderwidth=1, relief="solid",
                           width=15, height=2, font=('BM Jua', 20),
                           bg='#f1e8d7', fg='#cd3c3c')

        header1.grid(row=0, column=0)
        header2.grid(row=0, column=1)
        header3.grid(row=0, column=2)
        header4.grid(row=0, column=3)
        header5.grid(row=0, column=4)

        for i, attr in enumerate(attribute):
            label_attr = tk.Label(self.table_frame, text=attr,
                                  padx=10, pady=5, borderwidth=1,
                                  width=15, height=2, font=('BM Jua', 18),
                                  fg='#3d251e')
            label_attr.grid(row=i + 1, column=0)

            label_mean = tk.Label(self.table_frame, text=f"{mean[i]:.4f}",
                                  padx=10, pady=5, borderwidth=1,
                                  width=15, height=2, font=('BM Jua', 18),
                                  fg='#3d251e')
            label_mean.grid(row=i + 1, column=1)

            label_std = tk.Label(self.table_frame, text=f"{std[i]:.4f}",
                                 padx=10, pady=5, borderwidth=1,
                                 width=15, height=2, font=('BM Jua', 18),
                                 fg='#3d251e')
            label_std.grid(row=i + 1, column=2)

            label_min = tk.Label(self.table_frame, text=f"{min_val[i]:.4f}",
                                 padx=10, pady=5, borderwidth=1,
                                 width=15, height=2, font=('BM Jua', 18),
                                 fg='#3d251e')
            label_min.grid(row=i + 1, column=3)

            label_max = tk.Label(self.table_frame, text=f"{max_val[i]:.4f}",
                                 padx=10, pady=5, borderwidth=1,
                                 width=15, height=2, font=('BM Jua', 18),
                                 fg='#3d251e')
            label_max.grid(row=i + 1, column=4)

    def show_table(self):
        """
        Display descriptive and statistic table.
        :return: None
        """
        self.table_frame.pack(pady=25)

    def exit_app(self):
        """
        Exit application.
        :return: None
        """
        self.destroy()
        self.quit()

    def bind(self, sequence=None, func=None, add=None):
        """
        Bind function to an event for all children widgets.
        :param sequence: A string representing the event sequence.
        :param func: The function to bind to the event.
        :param add: Optional parameter.
        :return: None
        """
        for w in self.winfo_children():
            w.bind(sequence, func)
