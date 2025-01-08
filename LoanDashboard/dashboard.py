import pandas as pd
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

# Load the data
data = pd.read_csv("loan_data.csv")

# Initialize the Dash app with Bootstrap CSS
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Navbar Component
navbar = dbc.Navbar(
    dbc.Container([
        dbc.NavbarBrand("Loan Credibility Dashboard", className="ml-2"),
        dbc.Nav([
            dbc.NavItem(dbc.NavLink("Home", href="#")),
            dbc.NavItem(dbc.NavLink("About", href="#")),
            dbc.NavItem(dbc.NavLink("Contact", href="#")),
        ], className="ml-auto", navbar=True),
    ]),
    color="dark",
    dark=True,
    sticky="top",
)

# Layout for the dashboard
app.layout = html.Div([
    navbar,
    html.Div([
        html.H1("Interactive Loan Dashboard", style={'text-align': 'center', 'margin-top': '20px'}),

        # Row 1: Loan Amount Graph
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id="loan-amount-graph",
                    figure=px.histogram(
                        data, x="Loan Amount Requested", color="Loan Eligibility",
                        title="Loan Amount Distribution by Eligibility"
                    ).update_layout(template="plotly_dark"),
                ), width=6
            ),
            dbc.Col(
                dcc.Graph(
                    id="income-vs-loan",
                    figure=px.scatter(
                        data, x="Monthly Income", y="Loan Amount Requested", color="Loan Eligibility",
                        title="Monthly Income vs Loan Amount"
                    ).update_layout(template="plotly_dark"),
                ), width=6
            ),
        ]),

        # Row 2: Repayment History Pie Chart
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id="repayment-history",
                    figure=px.pie(data, names="Loan Repayment History", title="Loan Repayment History Distribution")
                    .update_layout(template="plotly_dark"),
                ), width=6
            ),
        ]),

        # Search Customer Section
        html.Div([
            html.H3("Search Customer by ID", style={'text-align': 'center', 'margin-top': '20px'}),
            dbc.Input(id="customer-id-input", placeholder="Enter Customer ID", type="text"),
            html.Div(id="customer-details", style={'margin-top': '20px'}),
        ], className="search-section"),
    ], className="container"),
])


# Callback for Customer Search
@app.callback(
    Output('customer-details', 'children'),
    [Input('customer-id-input', 'value')]
)
def search_customer(customer_id):
    if customer_id:
        customer = data[data["Customer ID"] == customer_id]
        if not customer.empty:
            return html.Div([
                html.P(f"Name: {customer.iloc[0]['Name']}"),
                html.P(f"Age: {customer.iloc[0]['Age']}"),
                html.P(f"Loan Amount Requested: {customer.iloc[0]['Loan Amount Requested']}"),
                html.P(f"Monthly Income: {customer.iloc[0]['Monthly Income']}"),
                html.P(f"Loan Eligibility: {'Approved' if customer.iloc[0]['Loan Eligibility'] == 1 else 'Rejected'}"),
            ], style={'padding': '10px', 'backgroundColor': '#f8f9fa', 'borderRadius': '5px'})
        else:
            return html.P("Customer not found!", style={'color': 'red'})
    return html.P("Enter a Customer ID to search.")


if __name__ == '__main__':
    app.run_server(debug=True)
