# dash-mapbox

A Map showing Diseases around the World.
App available on Heroku [here](https://octochart.herokuapp.com/)

## Author

Ben Seifert

## Project Title

octochart

## Install

`./docs/installation.md`

## Software Version

`./requirements.txt`

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
