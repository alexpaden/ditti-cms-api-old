from ditti_web.database import warpcast
from flask import jsonify

def get_followers():
    res = warpcast.get_followers(fid=533)
    users = []
    for user in res.users:
        users.append({
            "fid": user.fid,
            "username": user.username,
            "dispaly": user.display_name,
        })
    return users