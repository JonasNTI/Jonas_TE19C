import plotly.express as px 
import dash
import dash_core_components as dcc
import dash_html_components as HTML
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Plockar ut och separerar de värdena som graferna behöver från filen
df_main = pd.read_csv("National_Total_Deaths_by_Age_Group.csv")
df_age = df_main["Age_Group"]
df_c = df_main["Total_Cases"]
df_i = df_main["Total_ICU_Admissions"]
df_d = df_main["Total_Deaths"]
case_tot = df_c.sum()
icu_tot = df_i.sum()
death_tot = df_d.sum()

# skapar en dataframe för smittade per åldersgrupp
frekvens_dict_c = dict(age = df_age, smittade = df_c)
df_age_c = pd.DataFrame(frekvens_dict_c)

# skapar en dataframe för döda per åldersgrupp
frekvens_dict_d = dict(age = df_age, dödsfall = df_d)
df_age_d = pd.DataFrame(frekvens_dict_d)

# skapar dataframe för totala antalet smittade/döda/icu admissions
frekvens_dict_cid = dict(smittade_döda_ICU = ["Smittade", "Döda", "ICU"], antal = [case_tot, death_tot, icu_tot])
df_cid = pd.DataFrame(frekvens_dict_cid)

# samlar värden för smittade/döda till cirkeldiagram
döda_smittade = death_tot
levande_smittade = case_tot - döda_smittade

# skapar en allmän figur
fig = px.bar(df_age_c, x="age", y="smittade", title="Smittade per åldersgrupp")

# utseendet
app.layout = HTML.Div(children=[
    HTML.H1(children = "Covid-19 statistik"), 

    # dropdownmeny
    dcc.Dropdown(
        id = "drop",
        options = [dict(label = "Cases per åldersgrupp", value="smittade"), dict(label = "Dödsfall per åldersgrupp", value="dödsfall"), dict(label = "smittade_döda_ICU", value="cid"), dict(label = "Smittade/Döda_Procent", value="cd")],
        value="smittade"
    ),

    # rendera visualisering för graferna
    dcc.Graph(
        id = "graph",
        figure = fig
    )
])

@app.callback(
    Output("graph", "figure"),
    [Input("drop", "value")]
)

# funktion som skapar graferna efter vilken knapp i dropdownmenyn som användaren väljer
def update_figure(value):
    if value == "smittade":
         df = df_age_c
         fig = px.bar(df, x="age", y=value, title=f"Antal {value} per åldersgrupp") # stapeldiagram (smittade per åldersgrupp)
    elif value == "dödsfall":
        df = df_age_d
        fig = px.bar(df, x="age", y=value, title=f"Antal {value} per åldersgrupp") # stapeldiagram (döda per åldersgrupp)
    elif value == "cid":
        df = df_cid
        fig = px.bar(df, x="antal", y="smittade_döda_ICU", orientation="h", title=f"Totalt antal smittade, döda och intensivvårdade") # liggande stapeldiagram (antal smittade/döda/ICU)
    elif value == "cd":
        fig = px.pie(names=["levande som är/varit smittade", "smittade som dött"], values=[levande_smittade,döda_smittade], title=f"Procentuell andel av alla covid fall som lett till död") # cirkeldiagram (smittade som har/inte har dött)

    fig.update_layout(transition_duration=500) # tiden det tar för en graf att bytas ut mot en annan
    return fig  # returnerar figuren(grafen)

# startar server i webbläsaren
if __name__ == "__main__":
    app.run_server(debug = True)
