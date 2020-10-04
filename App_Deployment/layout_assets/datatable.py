#--------------------- Packages
import pandas as pd
import dash_table

#--------------------- Datatable
def datatable_asset(df):
    """Function to create a datatable which is used to return the tweets and sentiment."""
    datatable = dash_table.DataTable( 
        id = 'typing_formatting_1',
        data = df.to_dict('records'),
        columns =
        [
            {
                'id': 'Tweets',
                'name': 'Tweet',
                'type': 'text'
            }, 

            {
                'id': 'Sentiment',
                'name': 'Sentiment',
                'type': 'text'
            }, 

            


        ],
        
        # Highlight Cells based on conditions - first, second, and third row
        style_data_conditional =
        [
            # Highlighting sentiment analysis results
            {
                "if": {"column_id": "Sentiment",
                       "filter_query": "{Sentiment} = Positive"},
                "backgroundColor": "#a6f1a6",
                'color': 'black'
            },

            {
                "if": {"column_id": "Sentiment",
                       "filter_query": "{Sentiment} = Negative"},
                "backgroundColor": "#ff0000",
                'color': 'black'
            },

            {
                "if": {"column_id": "Sentiment",
                       "filter_query": "{Sentiment} = Neutral"},
                "backgroundColor": "#e0e0e0",
                'color': 'black'
            },
            # Fix columnd widths
            {'if': {'column_id': 'Tweets'},
             'width': '90%'},
            
            {'if': {'column_id': 'Sentiment'},
             'width': '10%'},
        ],
        
        # Formatting the data/headers cells
        style_cell = {'backgroundColor': '#f7f7f7', 'font-family': 'helvetica',
                      'fontColor': '#000000', 'fontSize': 24, 'textAlign': 'left'
                     },

        style_data = {'border': '1px solid #00a8ff', 'font-size': 24,
                      'font-family': 'helvetica', 'whiteSpace': 'normal', 
                     },

        style_header = {'border': '1px solid #00a8ff', 'font-size': 28,
                        'font-family': 'helvetica', 'textAlign': 'center',
                        'fontWeight': 'bold'
                       },

        css = [{
            'selector': '.dash-spreadsheet td div',
            'rule': '''
            line-height: 35px;
            max-height: 70px; min-height: 70px; height: 70px;
            display: block;
            overflow-y: hidden;
            '''
        }],
        
        tooltip_data = [{
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
        }
            for row in df.to_dict('rows')
        ],
        
        tooltip_duration = None,
        editable = True,
        page_size = 10,
        filter_action = "native",
        sort_action = "native",
        sort_mode = "multi",
        column_selectable = "single",
        row_selectable = "multi",
        row_deletable = True,
        selected_columns = [],
        selected_rows = [],
        page_action = "native",
        
    )
    return datatable