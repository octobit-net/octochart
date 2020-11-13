# Classic libaries
import pandas as pd
from datetime import date 

# Custom function
import utils as f

# Plotly Import - express bib
import plotly.express as px


def melt(df):
    # get January, February, .. December in column Date
    df = df.melt(id_vars=['Country','ISO3','Region','Year'], var_name='Date')
    # combine Year and Date in %B-Format to one
    df['Date'] = pd.to_datetime(df.pop('Year').astype(str) + df['Date'], format='%Y%B')
    # set Date to Year.Month - Format and back to String for output and sorting
    df['Date'] = df['Date'].dt.strftime('%Y.%m')
    return (df)

def process_all_data(df_diseases):
    # get the disease dataframes and process it
    df_measles=melt(df_diseases[0])
    df_rubella=melt(df_diseases[1])
    # Combine two Dataframes to one
    df=pd.merge(df_measles,df_rubella,how="outer",on=['Country','Date','ISO3','Region'],suffixes=('_measles', '_rubella'))
    # combine suffixes in disease column
    df = df.melt(id_vars=['Country','ISO3','Region','Date'], var_name='Disease')
    # renaming
    df['Disease'] = df['Disease'].replace(['value_measles'],'Measles')
    df['Disease'] = df['Disease'].replace(['value_rubella'],'Rubella')
    # defining size values nan = 0
    df['size'] = df['value'].fillna(0)
    # filling nan values with "no info"-text
    df['value'] = df['value'].fillna('no information given')
    # Columns renaming
    df.columns = [col.lower() for col in df.columns]
    # Extracting latitute and longitude from the coords file
    df = pd.merge(df,coords,how="inner",on=['iso3'])
    # sorting the values for country and date
    df = df.sort_values(['country','date'], ignore_index=True)
    return (df)

def create_fig(df_diseases):
    # create a plotly figure out of the dataframe
    fig= px.scatter_mapbox(df_diseases, 
        # set the coordinates
        lon="lon", 
        lat="lat", 
        # define the traces
        color="disease",
        # define the information which will be shown
        hover_data=[
                     "country","value"# value instead of size
                      # because the information given could also be 'nan' instead of 0
                 ],
        # compute the sizes         
        size="size",
        # set the data for the slider
        animation_frame="date",
        # which mapbox style, also possible to combine it with mapbox.com token
        mapbox_style="open-street-map",
        # display options of the map
        center={'lon': 40.52, 'lat': 34.34},
        zoom=1.3,
        # maximum of the computed bubblesizes, "100" looks good 
        size_max=100,
        )
    # optimize the layout of the scatter_mapbox    
    fig.update_layout(
        # set layout of the figure to display
        margin={"r":0,"t":0,"l":0,"b":0},
        autosize=True,
        # layout of the traces: diseases
        legend={
            # set a border
            "borderwidth":1,
            # get it in the bottom, left corner
            "x":0,
            "y":0,
            # show a title above
            "title":{"text":"Diseases [Year.Month]:",
                },
            },  
    )    

    return fig
if __name__ =="__main__":  
    # Load necessary information
        #online
    raw_dataset_path_measles = 'https://www.who.int/immunization/monitoring_surveillance/burden/vpd/measlescasesbycountrybymonth.xls?ua=1'
    raw_dataset_path_rubella = 'https://www.who.int/immunization/monitoring_surveillance/burden/vpd/rubellacasesbycountrybymonth.xls?ua=1'
        #offline
    #raw_dataset_path_rubella = f.RAW_PATH + f.parser['path']['rubella']
    #raw_dataset_path_measles = f.RAW_PATH + f.parser['path']['measles']
    raw_dataset_path_iso3_coord = f.RAW_PATH + f.parser['path']['iso3coord'] #iso3-country code to lat,lon - file

    # Load datasets
    measles = pd.read_excel(raw_dataset_path_measles, sheet_name=1)
    rubella = pd.read_excel(raw_dataset_path_rubella, sheet_name=1)
    coords = pd.read_csv(raw_dataset_path_iso3_coord, index_col=0)

    # Creating dataFrames and process them
    diseases=[measles,rubella]
    df_diseases=process_all_data(diseases)

    # Preparing figure
    fig_world = create_fig(df_diseases)

    # Storing all necessay information for app
    save = {'figure':fig_world,
            'last_date':date.today()}
    f.save_pickle(save, 'world_info.p')

    # Display Map directly
    fig_world.show()
