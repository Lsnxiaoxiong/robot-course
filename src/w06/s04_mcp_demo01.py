"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""
import random
import time
from typing import TypedDict, Optional

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# 定义返回结构（TypedDict 只是为了类型检查）
class WeatherInfo(TypedDict):
    温度: str        # 如 "23°C"
    湿度: str        # 如 "56%"
    风速: str        # 如 "3.2 m/s"
    风向: str        # 如 "东南偏东"
    天气: str        # 如 "多云"
    气压: str        # 如 "1013 hPa"
    更新时间: str    # ISO 格式时间 / 或本地时间字符串
    备注: Optional[str]  # 额外说明（可选）

# ------------------------------
# Mock 实现（用于测试 / 没有 API 的场景）
# ------------------------------
@mcp.tool()
def get_weather_mock(city: str) -> WeatherInfo:
    """
    返回编造/模拟的天气信息（用于测试）。
    """
    # 随机但可重复性：使用 city 的 hash 生成一些稳定的数值（避免每次都完全随机）
    seed = abs(hash(city)) % 10000
    random.seed(seed + int(time.time() // 3600))  # 每小时略有变化
    temp_c = round(15 + (seed % 10) + (random.random() - 0.5) * 6, 1)
    humidity = random.randint(30, 90)
    wind_speed = round(random.uniform(0.5, 8.0), 1)
    pressure = 1000 + (seed % 30)
    conditions = ["晴", "多云", "阴", "小雨", "中雨", "阵雨", "雾", "雪"]
    cond = random.choice(conditions)
    directions = ["北", "东北", "东", "东南", "南", "西南", "西", "西北"]
    wind_dir = random.choice(directions)

    return WeatherInfo(
        温度=f"{temp_c}°C",
        湿度=f"{humidity}%",
        风速=f"{wind_speed} m/s",
        风向=wind_dir,
        天气=cond,
        气压=f"{pressure} hPa",
        更新时间=time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime()),
        备注="模拟数据，仅作测试用"
    )


def main():
    # Initialize and run the server
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()