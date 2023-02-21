import os
from dotenv import load_dotenv
from farcaster import Warpcast
from flask import jsonify

class FollowController:
    def __init__(self):
        load_dotenv()
        token = access_token=os.getenv("WARP_SECRET")
        print("token:", token)

        self.warpcast = Warpcast(access_token=token)

    def get_followers(self):
        res = self.warpcast.get_followers(fid=533)
        users = []
        for user in res.users:
            users.append({
                "fid": user.fid,
                "username": user.username,
                "dispaly": user.display_name,
            })
        return users
    
def get_followers():
    controller = FollowController()
    return controller.get_followers()