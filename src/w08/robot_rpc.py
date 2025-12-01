import requests


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


# if __name__ == "__main__":
#     r = RobotRPC.run_action("go_forward_one_step")
#     print(r)