import json
from flask import Blueprint, jsonify, request
from ditti_api.services.tracker import TrackerService
from ditti_api.auth import require_auth


tracker_bp = Blueprint('tracker', __name__)
tracker_service = TrackerService()

class TrackerController:
    
    # GET /api/v1/follow-trackers/{fid}
    @tracker_bp.route('/follow-trackers/<int:fid>', methods=['GET'])
    @require_auth
    def get_follow_trackers(fid):
        # Call the TrackerService method to retrieve follow trackers for the given fid
        follow_trackers = tracker_service.get_follow_tracker_entries_by_fid(fid)
        return jsonify(follow_trackers)

    # POST /api/v1/follow-trackers/{fid}
    @require_auth
    @tracker_bp.route('/follow-trackers/<int:fid>', methods=['POST'])
    def post_follow_trackers(fid):
        # Call the TrackerService method to run the post follow tracker service for the given fid
        result = tracker_service.post_follow_tracker_entry_by_fid(fid)

        # Return a JSON response containing the result of the service call
        return jsonify(result)

    # GET /api/v1/profile-trackers/{fid}
    @tracker_bp.route('/profile-trackers/<int:fid>', methods=['GET'])
    @require_auth
    def get_profile_trackers(fid):
        # Call the TrackerService method to retrieve profile trackers for the given fid
        profile_trackers = tracker_service.get_profile_tracker_entries_by_fid(fid)

        # Return a JSON response containing the profile trackers
        return jsonify(profile_trackers)

    # POST /api/v1/profile-trackers/{fid}
    @tracker_bp.route('/profile-trackers/<int:fid>', methods=['POST'])
    @require_auth
    def post_profile_trackers(fid):
        # Call the TrackerService method to run the post profile tracker service for the given fid
        result = tracker_service.post_profile_tracker_entry_by_fid(fid)

        # Return a JSON response containing the result of the service call
        return jsonify(result)

    # GET /api/v1/trackees/{fid}
    @tracker_bp.route('/trackees/<int:fid>', methods=['GET'])
    @require_auth
    def get_trackees(fid):
        # Call the TrackerService method to retrieve trackees for the given manager fid
        trackees = tracker_service.get_trackees_by_manager_fid(fid)

        # Return a JSON response containing the trackees
        return jsonify(trackees)

    # POST /api/v1/tracker-manager
    @tracker_bp.route('/tracker-manager', methods=['POST'])
    @require_auth
    def post_tracker_manager():
        # Get the manager_fid and trackee_fid from the request body
        data = request.get_json()
        manager_fid = data['manager_fid']
        trackee_fid = data['trackee_fid']

        # Call the TrackerService method to create a new tracker manager
        result = tracker_service.post_trackee_by_manager_fid(manager_fid, trackee_fid)
        
        # Return a JSON response containing the result of the service call
        return jsonify(result)
