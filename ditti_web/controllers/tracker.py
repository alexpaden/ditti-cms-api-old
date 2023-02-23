from ditti_web.database import warpcast, supabase

class TrackerController:
    def get_follow_tracker_by_fid(self, fid: int):
        pass
        #services.query_follow_tracker_by_fid
        
    def request_new_follow_track(self, fid: int):
        pass
        #services.request_new_follow_track
        
    def post_new_trackee_fid(self, fid: int):
        pass
        #services.post_new_trackee_fid
        
    def post_new_tracker_manager(self, trackee_fid: int, tracker_fid: int):
        pass
        #services.post_new_tracker_manager
        
    def get_all_trackees_by_fid(self, fid: int):
        pass
        #services.get_all_trackees_by_fid