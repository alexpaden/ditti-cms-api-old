from functools import wraps
from flask import request, jsonify
from ditti_api.database import supabase

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get("Authorization")
        if not api_key:
            return jsonify({"message": "API key required"}), 401

        # Check if the API key is valid
        res = supabase.from_("api_keys").select("*").eq("token", api_key).execute()

        if not res.data:
            return jsonify({"message": "Invalid API key"}), 401

        return f(*args, **kwargs)

    return decorated
