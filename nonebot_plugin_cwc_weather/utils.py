import json
import datetime


def format_weather_data(weather_data: dict) -> str:
    """格式化天气信息为字符串"""
    
    # 检查是否是字符串（错误信息）
    if isinstance(weather_data, str):
        print(f"Error response: {weather_data}")
        return weather_data
    
    # 确保数据类型是字典
    if not isinstance(weather_data, dict):
        print(f"Unexpected data format: {type(weather_data)}")
        return "数据格式错误"
    
    # 打印出返回的天气数据
    #print(f"Weather data: {json.dumps(weather_data, ensure_ascii=False, indent=2)}")
    
    # 提取城市名称，默认为"未知城市"
    city = weather_data.get("location", "未知城市")
    
    # 提取天气描述，默认值为"未知天气"
    description = weather_data["weather"][0].get("description", "未知天气")
    
    # 提取温度相关信息
    temp = weather_data["main"].get("temp", "未知温度")
    feels_like = weather_data["main"].get("feels_like", "未知体感温度")
    humidity = weather_data["main"].get("humidity", "未知湿度")
    
    # 提取风速和风阵风
    wind_speed = weather_data["wind"].get("speed", "未知风速")
    wind_gust = weather_data["wind"].get("gust", "未知风阵风")
    
    # 获取时区（假设API返回的"timezone"字段是秒数）
    timezone = weather_data.get("timezone", 0)
    
    # 提取日出和日落时间戳
    sunrise = weather_data["sys"].get("sunrise", 0)
    sunset = weather_data["sys"].get("sunset", 0)
    
    # 转换时间戳为可读格式
    local_sunrise_time = datetime.datetime.utcfromtimestamp(sunrise + timezone).strftime('%H:%M:%S') if sunrise else "未知时间"
    local_sunset_time = datetime.datetime.utcfromtimestamp(sunset + timezone).strftime('%H:%M:%S') if sunset else "未知时间"

    
    # 返回格式化的天气信息
    return f"{city}的当前天气：\n" \
           f"天气：{description}\n" \
           f"温度：{temp}°C\n" \
           f"体感温度：{feels_like}°C\n" \
           f"湿度：{humidity}%\n" \
           f"风速：{wind_speed} m/s\n" \
           f"风速阵风：{wind_gust} m/s\n" \
           f"日出时间：{local_sunrise_time}\n" \
           f"日落时间：{local_sunset_time}"
