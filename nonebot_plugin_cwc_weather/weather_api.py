import requests

def get_weather(city: str):
    # 构造API请求的URL
    url = f"https://api.cwc.caner.hk/interface/cangcu_bot.php?apikey=ChongChuk&location={city}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果响应码不是 200，则抛出异常
        data = response.json()
        
        # 返回原始的天气数据
        return data
    except requests.exceptions.RequestException as e:
        return {"error": f"请求错误：{e}"}
    except KeyError:
        return {"error": "返回数据格式异常，请检查API接口。"}
