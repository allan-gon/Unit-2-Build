import dash
import dash_core_components as dcc
import dash_html_components as html




app = dash.Dash()

app.layout = html.Div([
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
            html.Label("How many episodes will the show/movie have?"),
            dcc.Input(
                placeholder= "Input the number of episodes",
                type = 'number',
                value = ''
            )
    ]),
    html.Br(),
    html.Br(),
    
    html.Div([
            html.Label("How how much related material does the show/movie have?"),
            dcc.Input(
                placeholder= "Input the number of related material",
                type = 'number',
                value = ''
            )
    ]),
    html.Br(),
    html.Br(),
    html.Label("Check all genres that apply"),
    dcc.Checklist(
        options = [
            {'label':'Yaoi','value':'Yaoi'},
            {'label':'Yuri','value':'Yuri'},
            {'label':'Ecchi','value':'Ecchi'},
            {'label':'Harem','value':'Harem'},
            {'label':'Hentai','value':'Hentai'},
            {'label':'Josei','value':'Josei'},
            {'label':'Shounen Ai','value':'Shounen Ai'},
            {'label':'Shoujo Ai','value':'Shoujo Ai'},
            {'label':'Romance','value':'Romance'}
        ]
    ),
    dcc.Checklist(
        options = [
            {'label':'Martial Arts','value':'Martial Arts'},
            {'label':'Sports','value':'Sports'}
        ]
    ),
    dcc.Checklist(
        options = [
            {'label':'Kids','value':'Kids'},
            {'label':'Seinen','value':'Seinen'},
            {'label':'Shoujo','value':'Shoujo'},
            {'label':'Shounen','value':'Shounen'},
            {'label':'Super Power','value':'Super Power'},
            {'label':'Slice of Life','value':'Slice of Life'},
            {'label':'School','value':'School'},
            {'label':'Action','value':'Action'}
        ]
    ),
    dcc.Checklist(
        options = [
            {'label':'Adventure','value':'Adventure'},
            {'label':'Mystery','value':'Mystery'},
            {'label':'Psychological','value':'Psychological'},
            {'label':'Dementia','value':'Dementia'}
        ]
    ),
    dcc.Checklist(
        options = [
            {'label':'Drama','value':'Drama'},
            {'label':'Horror','value':'Horror'},
            {'label':'Thriller','value':'Thriller'}
        ]
    ),
    dcc.Checklist(
        options = [
            {'label':'Demons','value':'Demons'},
            {'label':'Fantasy','value':'Fantasy'},
            {'label':'Game','value':'Game'},
            {'label':'Magic','value':'Magic'},
            {'label':'Supernatural','value':'Supernatural'},
            {'label':'Vampire','value':'Vampire'},
            {'label':'Sci-Fi','value':'Sci-Fi'},
            {'label':'Cars','value':'Cars'},
            {'label':'Space','value':'Space'}
        ]
    ),
    dcc.Checklist(
        options = [
            {'label':'Comedy','value':'Comedy'},
            {'label':'Parody','value':'Parody'}
        ]
    ),
    dcc.Checklist(
        options = [
            {'label':'Military','value':'Military'},
            {'label':'Police','value':'Police'},
            {'label':'Mecha','value':'Mecha'}
        ]
    ),
    dcc.Checklist(
        options = [
            {'label':'Historical','value':'Historical'},
            {'label':'Samurai','value':'Samurai'},
            {'label':'Music','value':'Musice'}
        ]
    ),
    
])


# x = df.source.str.lower().unique()

# bins = set()
# for i in x:
#     if 'manga' in i:
#         bins.add('manga')
#     elif i == 'original':
#         bins.add(i)
#     elif 'novel' in i:
#         bins.add('novel')
#     elif i == 'unknown':
#         bins.add(i)
#     elif i == 'other':
#         bins.add(i)
#     elif i == 'music':
#         bins.add(i)
#     elif 'game' in i:
#         bins.add('game')
#     elif 'book' in  i:
#         bins.add('book')
#     elif i == 'radio':
#         bins.add(i)
#     else:
#         raise ValueError



# # This runs the app

if __name__ == "__main__":
    app.run_server(debug=True)