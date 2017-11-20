#!/usr/bin/env python
# coding=utf-8

# <bitbar.title>Yahoo Weather</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Christian M. Blesing</bitbar.author>
# <bitbar.author.github>picturaluce</bitbar.author.github>
# <bitbar.desc>Shows the current weather.</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

# Special thanks goes out to Yahoo for their Weather API: https://developer.yahoo.com/weather/

import json
import urllib2

# WOEID City goes here (Search-Tool: http://woeid.rosselliot.co.nz/)
woeid = '638242'

# API URL
api_yahoo1 = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D'
api_yahoo2 = '&format=json&diagnostics=true&callback='
api_yahoo_final = api_yahoo1 + woeid + api_yahoo2

# API Request Yahoo Weather API
yahoo_request = urllib2.Request(api_yahoo_final)
yahoo_response = urllib2.urlopen(yahoo_request).read()
yahoo_result = json.loads(yahoo_response)
weather_location_city = str(yahoo_result['query']['results']['channel']['location']['city'])
weather_location_country = str(yahoo_result['query']['results']['channel']['location']['country'])
weather_temp_f = int(yahoo_result['query']['results']['channel']['item']['condition']['temp'])
weather_condition = str(yahoo_result['query']['results']['channel']['item']['condition']['text'])
weather_wind = int(yahoo_result['query']['results']['channel']['wind']['speed'])
weather_sunrise = str(yahoo_result['query']['results']['channel']['astronomy']['sunrise'])
weather_sunset = str(yahoo_result['query']['results']['channel']['astronomy']['sunset'])
weather_humidity = str(yahoo_result['query']['results']['channel']['atmosphere']['humidity'])
weather_pressure = str(yahoo_result['query']['results']['channel']['atmosphere']['pressure'])

weather_fc1_date = str(yahoo_result['query']['results']['channel']['item']['forecast'][1]['date'])
weather_fc1_day = str(yahoo_result['query']['results']['channel']['item']['forecast'][1]['day'])
weather_fc1_high = int(yahoo_result['query']['results']['channel']['item']['forecast'][1]['high'])
weather_fc1_low = int(yahoo_result['query']['results']['channel']['item']['forecast'][1]['low'])
weather_fc1_text = str(yahoo_result['query']['results']['channel']['item']['forecast'][1]['text'])
weather_fc2_date = str(yahoo_result['query']['results']['channel']['item']['forecast'][2]['date'])
weather_fc2_day = str(yahoo_result['query']['results']['channel']['item']['forecast'][2]['day'])
weather_fc2_high = int(yahoo_result['query']['results']['channel']['item']['forecast'][2]['high'])
weather_fc2_low = int(yahoo_result['query']['results']['channel']['item']['forecast'][2]['low'])
weather_fc2_text = str(yahoo_result['query']['results']['channel']['item']['forecast'][2]['text'])
weather_fc3_date = str(yahoo_result['query']['results']['channel']['item']['forecast'][3]['date'])
weather_fc3_day = str(yahoo_result['query']['results']['channel']['item']['forecast'][3]['day'])
weather_fc3_high = int(yahoo_result['query']['results']['channel']['item']['forecast'][3]['high'])
weather_fc3_low = int(yahoo_result['query']['results']['channel']['item']['forecast'][3]['low'])
weather_fc3_text = str(yahoo_result['query']['results']['channel']['item']['forecast'][3]['text'])
weather_fc4_date = str(yahoo_result['query']['results']['channel']['item']['forecast'][4]['date'])
weather_fc4_day = str(yahoo_result['query']['results']['channel']['item']['forecast'][4]['day'])
weather_fc4_high = int(yahoo_result['query']['results']['channel']['item']['forecast'][4]['high'])
weather_fc4_low = int(yahoo_result['query']['results']['channel']['item']['forecast'][4]['low'])
weather_fc4_text = str(yahoo_result['query']['results']['channel']['item']['forecast'][4]['text'])
weather_fc5_date = str(yahoo_result['query']['results']['channel']['item']['forecast'][5]['date'])
weather_fc5_day = str(yahoo_result['query']['results']['channel']['item']['forecast'][5]['day'])
weather_fc5_high = int(yahoo_result['query']['results']['channel']['item']['forecast'][5]['high'])
weather_fc5_low = int(yahoo_result['query']['results']['channel']['item']['forecast'][5]['low'])
weather_fc5_text = str(yahoo_result['query']['results']['channel']['item']['forecast'][5]['text'])

weather_temp_c = str(round(((weather_temp_f - 32) * 0.555555556),0))
weather_wind_kmh = str(round((weather_wind * 1.60934),1))

weather_fc1_high_c = str(round(((weather_fc1_high - 32) * 0.555555556),0))
weather_fc1_low_c = str(round(((weather_fc1_low - 32) * 0.555555556),0))
weather_fc2_high_c = str(round(((weather_fc2_high - 32) * 0.555555556),0))
weather_fc2_low_c = str(round(((weather_fc2_low - 32) * 0.555555556),0))
weather_fc3_high_c = str(round(((weather_fc3_high - 32) * 0.555555556),0))
weather_fc3_low_c = str(round(((weather_fc3_low - 32) * 0.555555556),0))
weather_fc4_high_c = str(round(((weather_fc4_high - 32) * 0.555555556),0))
weather_fc4_low_c = str(round(((weather_fc4_low - 32) * 0.555555556),0))
weather_fc5_high_c = str(round(((weather_fc5_high - 32) * 0.555555556),0))
weather_fc5_low_c = str(round(((weather_fc5_low - 32) * 0.555555556),0))

# Output
print(weather_temp_c + ' °C')
print('---')
print(weather_location_city +', '+ weather_location_country)
print('---')
print('Condition: ' + weather_condition + ' @ ' + weather_temp_c + ' °C')
print('Humidity: ' + weather_humidity + '%')
print('Pressure: ' + weather_pressure + 'hPa')
print('Wind: ' + weather_wind_kmh + 'km/h')
print('---')
print('Sunrise: ' + weather_sunrise)
print('Sunset: ' + weather_sunset)
print('---')
print(weather_fc1_day + ', ' + weather_fc1_date + ' ‖ ⬆ High: ' + weather_fc1_high_c + ' °C' + ' ‖ ⬇ Low: ' + weather_fc1_low_c + ' °C')
print(weather_fc2_day + ', ' + weather_fc2_date + ' ‖ ⬆ High: ' + weather_fc2_high_c + ' °C' + ' ‖ ⬇ Low: ' + weather_fc2_low_c + ' °C')
print(weather_fc3_day + ', ' + weather_fc3_date + ' ‖ ⬆ High: ' + weather_fc3_high_c + ' °C' + ' ‖ ⬇ Low: ' + weather_fc3_low_c + ' °C')
print(weather_fc4_day + ', ' + weather_fc4_date + ' ‖ ⬆ High: ' + weather_fc4_high_c + ' °C' + ' ‖ ⬇ Low: ' + weather_fc4_low_c + ' °C')
print(weather_fc5_day + ', ' + weather_fc5_date + ' ‖ ⬆ High: ' + weather_fc5_high_c + ' °C' + ' ‖ ⬇ Low: ' + weather_fc5_low_c + ' °C')


# print('Forecast:' + weather_forecast + '| color=red') /// 