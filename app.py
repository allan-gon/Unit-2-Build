import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import pickle
from Wrangle import predict

with open('the_model_code/Models/tuned_xgb','rb') as myfile:
    model = pickle.load(myfile)

app = dash.Dash()

left = html.Div(
    children = [
    html.Label("What type will the media become?"),
    dcc.Dropdown(
        id='Type',
        options = [
            {'label':'TV','value':'TV'},
            {'label':'Movie','value':'Movie'},
            {'label':'OVA','value':'OVA'},
            {'label':'Special','value':'Special'},
            {'label':'ONA','value':'ONA'},
            {'label':'Music','value':'Music'}
        ],
        value='TV'
    ),
    html.Label("How long will the episode(s) be?"),
    dcc.Dropdown(
        id='Duration',
        options = [
            {'label':'Less than a minute','value':'less than a minute'},
            {'label':'1-20 minutes','value':'1-20'},
            {'label':'21-30 minutes','value':'21-30'},
            {'label':'31-59 minutes','value':'31-59'},
            {'label':'1 hour +','value':'60+'}
        ],
        value='21-30'
    ),
    html.Label("What was the source material?"),
    dcc.Dropdown(
        id='Source',
        options = [
            {'label':'Book','value':'book'},
            {'label':'Game','value':'game'},
            {'label':'Manga','value':'manga'},
            {'label':'Music','value':'music'},
            {'label':'Novel','value':'novel'},
            {'label':'Radio','value':'radio'},
            {'label':'Original','value':'original'},
            {'label':'Other','value':'other'},
            {'label':'Uknown','value':'unknown'}
        ],
        value='manga'
    ),
    html.Label("What's the maturity rating?"),
    dcc.Dropdown(
        id='Rating',
        options = [
            {'label':'G - All Ages','value':'G - All Ages'},
            {'label':'PG','value':'PG - Children'},
            {'label':'PG-13','value':'PG-13 - Teens 13 or older'},
            {'label':'R - 17+','value':'R - 17+ (violence & profanity)'},
            {'label':'R+','value':'R+ - Mild Nudity'},
            {'label':'Rx','value':'Rx - Hentai'},
            {'label':'None','value':'None'}
        ],
        value='PG-13 - Teens 13 or older'
    ),
    html.Label("What studio will be animating it?"),
    dcc.Dropdown(
        id='Studio',
        options = [
            {'label':'Toei','value':'Toei Animation'},
            {'label':'Sunrise','value':'Sunrise'},
            {'label':'Madhouse','value':'Madhouse'},
            {'label':'J.C.Staff','value':'J.C.Staff'},
            {'label':'Production I.G','value':'Production I.G'},
            {'label':'Studio Pierrot','value':'Studio Pierrot'},
            {'label':'TMS Entertainment','value':'TMS Entertainment'},
            {'label':'Studio Deen','value':'Studio Deen'},
            {'label':'Nippon Animation','value':'Nippon Animation'},
            {'label':'Other','value':'other'}
        ],
        value='Madhouse'
    ),
    html.Br(),
    html.Br(),
    
    html.Div([
            html.Label("How many episodes will the show/movie have? "),
            dcc.Input(
                id = 'Episodes',
                placeholder= "Input the number of episodes",
                type = 'number',
                value = 0
            ),
    ]),
    html.Br(),
    html.Br(),
    
    html.Div([
            html.Label("How how much related material does the show/movie have? "),
            dcc.Input(
                id = "Related",
                placeholder= "Input the number of related material",
                type = 'number',
                value = 0
            )
    ]),
    html.Br(),
    html.Br(),
    html.Label("Check all genres that apply"),
    html.Div(
    dcc.Checklist(
        id = 'Genre',
        options = [
            {'label':'Yaoi','value':'Yaoi'},
            {'label':'Yuri','value':'Yuri'},
            {'label':'Ecchi','value':'Ecchi'},
            {'label':'Harem','value':'Harem'},
            {'label':'Hentai','value':'Hentai'},
            {'label':'Josei','value':'Josei'},
            {'label':'Shounen Ai','value':'Shounen Ai'},
            {'label':'Shoujo Ai','value':'Shoujo Ai'},
            {'label':'Romance','value':'Romance'},
            {'label':'Martial Arts','value':'Martial Arts'},
            {'label':'Sports','value':'Sports'},
            {'label':'Kids','value':'Kids'},
            {'label':'Seinen','value':'Seinen'},
            {'label':'Shoujo','value':'Shoujo'},
            {'label':'Shounen','value':'Shounen'},
            {'label':'Super Power','value':'Super Power'},
            {'label':'Slice of Life','value':'Slice of Life'},
            {'label':'School','value':'School'},
            {'label':'Action','value':'Action'},
            {'label':'Mystery','value':'Mystery'},
            {'label':'Psychological','value':'Psychological'},
            {'label':'Dementia','value':'Dementia'},
            {'label':'Drama','value':'Drama'},
            {'label':'Horror','value':'Horror'},
            {'label':'Thriller','value':'Thriller'},
            {'label':'Demons','value':'Demons'},
            {'label':'Fantasy','value':'Fantasy'},
            {'label':'Game','value':'Game'},
            {'label':'Magic','value':'Magic'},
            {'label':'Supernatural','value':'Supernatural'},
            {'label':'Vampire','value':'Vampire'},
            {'label':'Sci-Fi','value':'Sci-Fi'},
            {'label':'Cars','value':'Cars'},
            {'label':'Space','value':'Space'},
            {'label':'Comedy','value':'Comedy'},
            {'label':'Parody','value':'Parody'},
            {'label':'Military','value':'Military'},
            {'label':'Police','value':'Police'},
            {'label':'Mecha','value':'Mecha'},
            {'label':'Historical','value':'Historical'},
            {'label':'Samurai','value':'Samurai'},
            {'label':'Music','value':'Music'}
        ],value=['Shounen']),style={'width':'50%'}
    ),
    html.Br(),
    html.Br(),
    html.Label('Enter the title: '),
    dcc.Input(id='Title',value='None',type='text',placeholder='Enter the title'),
    html.Br(),
    html.Header("What the model thinks"),
    html.Br(),
    html.Label(id='Prediction',children="Nothing for now..."),
    html.Br(),
    html.Br(),
    html.Button('Run Model',id='Button',n_clicks=0)
    ])

@app.callback(
    Output('Prediction','children'),
    [Input('Button','n_clicks')],
    state=[State('Title','value'),
    State('Type','value'),
    State('Source','value'),
    State('Episodes','value'),
    State('Duration','value'),
    State('Rating','value'),
    State('Studio','value'),
    State('Related','value'),
    State('Genre','value')])
def get_vars(n_clicks,title,types,source,episodes,duration,rating,studio, num_related, genres):
    if n_clicks == 0:
        return "Nothing for now..."
    else:
        genres = ", ".join(genres)
        pred = predict(model,title,types,source,episodes,duration,rating,studio, num_related, genres)
        return pred


app.layout = html.Div(left,style={'width':'50%'})

if __name__ == "__main__":
    app.run_server(debug=True)