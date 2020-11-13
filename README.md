# Diseases - World Cases

A Dash Map showing Diseases around the World.
App available on Heroku [here](https://octochart.herokuapp.com/).
Students Projectwork at TH-Bingen (Germany).

## Author

Ben Seifert

## Project Title

octochart

## Install

`./docs/installation.md`

## Software Version

`./requirements.txt`

## Design

* __assets  
  * style.css #CSS-File for the Dash-Layout  
* __data  
  * __pickle  
    * world_info.p #location of precomputed figure  
  * __raw
    * measles,rubella.xls #location of downloaded data files  
    * iso3coords.csv #file for convert ISO3 Country Codes to Latitude and Longitude  
* __docs
  * installation.md #textfile for installation of this software
* __scripts  
  * create_fig.py #build the figure and save it as pickle  
  * utils.py #pickle managment, read config file  
* app.py #Dash-App load precomputed pickle-file in an HTML file  
* config.ini #location of paths  
* Procfile #declaring command for heroku  
* requirements.txt #software bibs used  
* update_data.sh #Shell-Script for Update the Data (only necessary when offline)  
* update_fig.sh #Shell-Script for Update the Figure  

## Data

- [measles dataset](https://www.who.int/immunization/monitoring_surveillance/burden/vpd/rubellacasesbycountrybymonth.xls?ua=1)
- [rubella dataset](https://www.who.int/immunization/monitoring_surveillance/burden/vpd/measlescasesbycountrybymonth.xls?ua=1)
- [iso3 lon/lat dataset](https://gist.github.com/tadast/8827699)

## Other resources

- <https://plotly.com/python/scattermapbox/>
- <https://plotly.com/python/bubble-maps/>
- <https://plotly.com/python/reference/layout/>
- <https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html>
- <https://dash.plotly.com/deployment>
- <https://pythonbasics.org/pickle/>
- <https://plotly.com/python/maps/>
- <https://stackoverflow.com/>

## Contact Details

ben@octobit.net

## Notes

- To run update data script, you need to have wget installed.
- To test the Scatter_Map without Dash, just uncomment `fig_world.show()`in ./scripts/create_fig.py and run it
