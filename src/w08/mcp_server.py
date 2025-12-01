import requests
from mcp.server.fastmcp import FastMCP


class RobotRPC:

    base_url = "http://192.168.1.104:50000"

    def run_action(action_name: str, times:int = 1) ->  dict:

        url = f"{RobotRPC.base_url}/robot/run_once"
        payload = {
            "action_name": action_name,
            "times": times
        }
        r = requests.get(url, params=payload, timeout=10)
        return r.json()


# Create an MCP server
mcp = FastMCP("robot-controller")


@mcp.tool(name="run_action")
def run_action(action_name: str, times: int = 1)-> dict:
    """
    运行机器人的动作，动作名称列表：[
    {'action_name':'go_forward_one_step','desc':'向前走一步'},
    {'action_name':'left_move','desc':'向左移动一步'},
    {'action_name':'right_move','desc':'向右移动一步'},
    {'action_name':'back_one_step','desc':'向后移动一步'},
    ]
    :param action_name:动作名称，从动作名称列表中获取
    :param times:执行次数，默认为1
    :return:返回执行动作结果
    """
    return RobotRPC.run_action(action_name, times)

def main():
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()