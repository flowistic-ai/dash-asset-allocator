import dash
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify
import pandas as pd

dash._dash_renderer._set_react_version("18.2.0")

stylesheets = dmc.styles.ALL

#  make dataframe from  spreadsheet:
df = pd.read_csv("assets/historic.csv")

MAX_YR = df.Year.max()
MIN_YR = df.Year.min()
START_YR = 2007

# since data is as of year end, need to add start year
df = (
    df.append({"Year": MIN_YR - 1}, ignore_index=True)
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

app = dash.Dash(__name__, external_stylesheets=stylesheets)

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


if __name__ == "__main__":
    app.run_server(debug=True)