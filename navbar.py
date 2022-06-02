import dash_bootstrap_components as dbc


nav_item = dbc.NavItem(dbc.NavLink("Link", href="#"))

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Item1"),
        dbc.DropdownMenuItem("Item2"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Item3"),
    ],
    nav=True,
    in_navbar=True,
    label="Menu",
)

nav_contents = [
    dbc.NavItem(dbc.NavLink("Home", href="#", active=True)),
    dbc.NavItem(dbc.NavLink("Charts", href="#")),
    dbc.NavItem(dbc.NavLink("Trending", href="#")),
    dbc.NavItem(dbc.DropdownMenu(
    label="More",
    children=[
        dbc.DropdownMenuItem("Register"),
        dbc.DropdownMenuItem("Sign in"),
        dbc.DropdownMenuItem("Help"),
    ],))

]

navbar = dbc.Nav(nav_contents, pills=True,  fill=True)



