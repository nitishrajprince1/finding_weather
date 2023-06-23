from utils import get_weather_data, into_xml_format, into_json_format


def get_weather(city, output_format):
    weather_data = get_weather_data(city)

    if output_format == 'xml':
        return into_xml_format(weather_data)
    elif output_format == 'json':
        return into_json_format(weather_data)
    else:
        print('use correct choice')
