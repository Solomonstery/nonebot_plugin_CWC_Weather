import nonebot
import re
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, Bot, Event
from .weather_api import get_weather
from .utils import format_weather_data
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name='苍簇CWC天气',
    description='获取实时天气信息，数据来源于Caner Weather Channe！',
    usage='/天气 [城市名]',
    
    extra={
        'menu_data': [
            {
                'func': '获取天气',
                'trigger_method': 'on_cmd',
                'trigger_condition': '/天气 [城市名]',
                'brief_des': '通过城市名获取天气信息',
                'detail_des': '使用此命令可以获取指定城市的当前天气信息。只需要输入“/天气 城市名”，即可获取温度、天气描述、风速、湿度等信息。'
            },
        ],
        'menu_template': 'default'
    }
)


# 创建一个命令来获取天气信息
weather = on_command("天气", priority=5)

@weather.handle()
async def _(bot: Bot, event: Event):
    # 获取纯文本消息
    message_text = event.get_plaintext().strip()
    
    # 使用正则表达式提取城市名
    match = re.match(r"天气\s*(\S.*)$", message_text)
    if match:
        city = match.group(1).strip()  # 获取城市名
    else:
        city = ""
    
    if not city:
        await weather.finish("请输入城市名，例如：天气 北京")
    
    # 获取天气数据
    weather_data = get_weather(city)
    formatted_weather = format_weather_data(weather_data)
    
    # 发送天气信息
    await weather.finish(formatted_weather)


