from datetime import datetime
from ditti_web.database import warpcast, supabase
import logging

class TrackerService:
    
    def get_follow_tracker_entries_by_fid(self, fid: int):
        try:
            res = supabase.from_('follow_trackers').select('*').eq('fid', fid).execute()
            return res.data
        except Exception as e:
            logging.error(f"error in get_follow_tracker_entries_by_fid: {e}")


    def get_profile_tracker_entries_by_fid(self, fid: int):
        try:
            res = supabase.from_('profile_trackers').select('*').eq('fid', fid).execute()
            return res.data
        except Exception as e:
            logging.error(f"error in get_profile_tracker_entries_by_fid: {e}")
       
            
    def get_recent_follow_tracker_entry_by_fid(self, fid: int):
        try:
            res = supabase.from_('follow_trackers').select('*').eq('fid', fid).order('created_at', desc=True).limit(1).execute()
            return res.data
        except Exception as e:
            logging.error(f"error in get_recent_follow_tracker_entry_by_fid: {e}")
            
            
    def get_tracker_changes_by_fid(self, fid: int, current_following: list, current_followers: list):
        try:
            recent = self.get_recent_follow_tracker_entry_by_fid(fid)
            if not recent:
                no_recent = {
                    "added": [],
                    "removed": []
                }
                return no_recent, no_recent
            recent_following = recent[0]['following_fids']
            recent_followers = recent[0]['follower_fids']

            # Find which followers have been added or removed from the following list
            following_changes = {
                'added': list(set(current_following) - set(recent_following)),
                'removed': list(set(recent_following) - set(current_following))
            }

            # Find which followers have been added or removed from the followers list
            follower_changes = {
                'added': list(set(current_followers) - set(recent_followers)),
                'removed': list(set(recent_followers) - set(current_followers))
            }

            return (following_changes, follower_changes)
        except Exception as e:
            logging.error(f"Error in get_tracker_changes_by_fid: {e}")

    def post_follow_tracker_entry_by_fid(self, fid: int):
        try:
            following_list = self.get_fid_following_list(fid)
            follower_list = self.get_fid_follower_list(fid)
            following_changes, follower_changes = self.get_tracker_changes_by_fid(fid, following_list, follower_list)
            if not any(following_changes.values()) and not any(follower_changes.values()):
                if not self.get_recent_follow_tracker_entry_by_fid(fid):
                    res = supabase.from_('follow_trackers').insert({
                        'fid': fid,
                        'created_at': datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                        'following_fids': following_list,
                        'following_changes': following_changes,
                        'follower_fids': follower_list,
                        'follower_changes': follower_changes
                    }).execute()
                    return res.data
                else:
                    # no changes to the following/follower lists
                    return
            res = supabase.from_('follow_trackers').insert({
                'fid': fid,
                'created_at': datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'following_fids': following_list,
                'following_changes': following_changes,
                'follower_fids': follower_list,
                'follower_changes': follower_changes
            }).execute()
            return res.data
        except Exception as e:
            logging.error(f"error in post_follow_tracker_entry_by_fid: {e}")
        return None


    def get_fid_following_list(self, fid: int):
        following_fids = []
        res = warpcast.get_all_following(fid=fid)
        following_fids = [user.fid for user in res.users]
        return following_fids
        
        
    def get_fid_follower_list(self, fid: int):
        follower_fids = []
        res = warpcast.get_all_followers(fid=fid)
        follower_fids = [user.fid for user in res.users]
        return follower_fids
    
    
    def get_following_changes(self, new_fids: list[int]):
        pass