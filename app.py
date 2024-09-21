from dash import dcc, html, Input, Output, dash_table, State, callback_context, Dash, _dash_renderer
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify
import pandas as pd

_dash_renderer._set_react_version("18.2.0")

stylesheets = dmc.styles.ALL

#  make dataframe from  spreadsheet:
df = pd.read_csv("assets/historic.csv")

MAX_YR = df.Year.max()
MIN_YR = df.Year.min()
START_YR = 2007

# since data is as of year end, need to add start year
df = (
    pd.concat([df, pd.DataFrame([{"Year": MIN_YR - 1}])], ignore_index=True)
    .sort_values("Year", ignore_index=True)
    .fillna(0)
)

COLORS = {
    "cash": "#3cb521",
    "bonds": "#fd7e14",
    "stocks": "#446e9b",
    "inflation": "#cd0200",
    "background": "whitesmoke",
}

app = Dash(__name__, external_stylesheets=stylesheets)


"""
==========================================================================
Markdown Text
"""

datasource_text = dcc.Markdown(
)

asset_allocation_text = dcc.Markdown(
)

learn_text = dcc.Markdown(
)

cagr_text = dcc.Markdown(
)

footer = html.Div(
)

"""
==========================================================================
Tables
"""

total_returns_table = dash_table.DataTable(
)

annual_returns_pct_table = dash_table.DataTable(
)


def make_summary_table(dff):
    return dbc.Table.from_dataframe(df_table, bordered=True, hover=True)


"""
==========================================================================
Figures
"""


def make_pie(slider_input, title):
    return fig


def make_line_chart(dff):
    return fig


"""
==========================================================================
Make Tabs
"""

# =======Play tab components

asset_allocation_card = dbc.Card(asset_allocation_text, className="mt-2")

slider_card = dbc.Card(
)


time_period_data = [
]


time_period_card = dbc.Card(
)

# ======= InputGroup components

start_amount = dbc.InputGroup(
)
start_year = dbc.InputGroup(
)
number_of_years = dbc.InputGroup(
)
end_amount = dbc.InputGroup(
)
rate_of_return = dbc.InputGroup(
)

input_groups = html.Div(
    [start_amount, start_year, number_of_years, end_amount, rate_of_return],
    className="mt-4 p-4",
)

# =====  Results Tab components

results_card = dbc.Card(
)


data_source_card = dbc.Card(
)


# ========= Learn Tab  Components
learn_card = dbc.Card(
)


# ========= Build tabs
tabs = dbc.Tabs(
)

header = dmc.AppShellHeader(
    dmc.Group(
        [
            dmc.Burger(id="burger-button", hiddenFrom="sm", size="sm"),
            DashIconify(icon="fluent:chart-multiple-16-filled", width=30, height=30, color="blue"),
            dmc.Text("Asset Allocator", size="xl", ta="center"),
        ],
        h="100%",
        px="xl",
    ),
)

navbar = dmc.AppShellNavbar(
    [
        dmc.AppShellSection("Parameters:"),
        dmc.AppShellSection(
            [
                dmc.ScrollArea(
                    [
                        dmc.Text("60 links in a scrollable section"),
                        *[
                            dmc.Skeleton(h=28, mt="xl", animate=False)
                            for _ in range(60)
                        ],
                    ],
                    type="hover",
                    scrollbarSize=12,
                    h=0,
                    style={"flexGrow": 1},
                ),
            ],
            grow=True,
            my="xl",
            style={"display": "flex", "flexDirection": "column"},
        ),
        dmc.AppShellSection("Navbar footer – always at the bottom"),
    ],
    p="xl",
    id="navbar",
    style={"display": "flex", "flexDirection": "column"},
)

app_shell = dmc.AppShell(
    [
        header,
        navbar,
        dmc.AppShellMain("Main"),
    ],
    header={"height": 60},
    navbar={
        "width": 300,
        "breakpoint": "sm",
        "collapsed": {"mobile": True},
    },
    padding="md",
    id="app-shell",
)


app.layout = dmc.MantineProvider([app_shell])


@app.callback(
    Output("app-shell", "navbar"),
    Input("burger-button", "opened"),
    State("app-shell", "navbar"),
)
def toggle_navbar(opened, navbar):
    navbar["collapsed"]["mobile"] = not opened
    return navbar

"""
==========================================================================
Helper functions to calculate investment results, cagr and worst periods
"""


def backtest(stocks, cash, start_bal, nper, start_yr):
    return dff


def cagr(dff):
    return f"{cagr_result:.1%}"


def worst(dff, asset):
    return f"{worst_yr_loss:.1%} in {worst_yr}"

"""
==========================================================================
Callbacks
"""


@app.callback(
    Output("allocation_pie_chart", "figure"),
    Input("stock_bond", "value"),
    Input("cash", "value"),
)
def update_pie(stocks, cash):
    return figure


@app.callback(
    Output("stock_bond", "max"),
    Output("stock_bond", "marks"),
    Output("stock_bond", "value"),
    Input("cash", "value"),
    State("stock_bond", "value"),
)
def update_stock_slider(cash, initial_stock_value):
    return max_slider, marks_slider, stocks


@app.callback(
    Output("planning_time", "value"),
    Output("start_yr", "value"),
    Output("time_period", "value"),
    Input("planning_time", "value"),
    Input("start_yr", "value"),
    Input("time_period", "value"),
)
def update_time_period(planning_time, start_yr, period_number):
    return planning_time, start_yr, period_number


@app.callback(
    Output("total_returns", "data"),
    Output("returns_chart", "figure"),
    Output("summary_table", "children"),
    Output("ending_amount", "value"),
    Output("cagr", "value"),
    Input("stock_bond", "value"),
    Input("cash", "value"),
    Input("starting_amount", "value"),
    Input("planning_time", "value"),
    Input("start_yr", "value"),
)
def update_totals(stocks, cash, start_bal, planning_time, start_yr):
    return data, fig, summary_table, ending_amount, ending_cagr


if __name__ == "__main__":
    app.run_server(debug=True)