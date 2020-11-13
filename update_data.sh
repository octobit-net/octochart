rm data/raw/rubellacasesbycountrybymonth.xls
rm data/raw/measlescasesbycountrybymonth.xls
rm data/pickle/world_info.p

wget -O data/raw/rubellacasesbycountrybymonth.xls "https://www.who.int/immunization/monitoring_surveillance/burden/vpd/rubellacasesbycountrybymonth.xls?ua=1"
wget -O data/raw/measlescasesbycountrybymonth.xls "https://www.who.int/immunization/monitoring_surveillance/burden/vpd/measlescasesbycountrybymonth.xls?ua=1"

cd scripts && echo ls && python create_fig.py
cd ..
python app.py