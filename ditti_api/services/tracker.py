from datetime import datetime
from ditti_api.database import warpcast, supabase
import logging
import time

class TrackerService:
    
    def get_follow_tracker_entries_by_fid(self, fid: int):
        try:
            columns=['id', 'created_at', 'follower_changes', 'following_changes']
            res = supabase.from_('follow_trackers').select(*columns).eq('fid', fid).execute()
            entries = []
            for data in res.data:
                follower_changes = {
                    "added": data["follower_changes"]["added"],
                    "removed": data["follower_changes"]["removed"]
                }
                data["follower_changes"] = follower_changes
                entries.append(data)
            return entries
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
                'added': [fid for fid in set(current_following) - set(recent_following)],
                'removed': [fid for fid in set(recent_following) - set(current_following)]
            }
            # Find which followers have been added or removed from the followers list
            follower_changes = {
                'added': [fid for fid in set(current_followers) - set(recent_followers)],
                'removed': [fid for fid in set(recent_followers) - set(current_followers)]
            }
            return (following_changes, follower_changes)
        except Exception as e:
            logging.error(f"Error in get_tracker_changes_by_fid: {e}")


    def post_follow_tracker_entry_by_fid(self, fid: int):
        try:
            following_list = self.get_fid_following_list(fid)
            follower_list = self.get_fid_follower_list(fid)
            following_changes, follower_changes = self.get_tracker_changes_by_fid(fid, following_list, follower_list)
            print("done")
            if not any(following_changes.values()) and not any(follower_changes.values()):
                if not self.get_recent_follow_tracker_entry_by_fid(fid):
                    # first entry for a fid in follow tracker
                    print("here")
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


    def get_fid_following_list(self, fid: int):
        following_fids = []
        following_fids = [user.fid for user in warpcast.get_all_following(fid=fid).users]
        return following_fids
        
        
    def get_fid_follower_list(self, fid: int):
        follower_fids = []
        follower_fids = [user.fid for user in warpcast.get_all_followers(fid=fid).users]
        return follower_fids


    def post_profile_tracker_entry_by_fid(self, fid: int):
        try:
            farc_user = warpcast.get_user(fid=fid)
            profile_data = {
                'fid': fid,
                'username': farc_user.username,
                'display_name': farc_user.display_name,
                'bio': farc_user.profile.bio.text,
                'pfp_url': farc_user.pfp.url
            }
            recent_entry = self.get_recent_profile_tracker_entry_by_fid(fid)
            recent_entry = self.get_recent_profile_tracker_entry_by_fid(fid)
            if recent_entry and all(profile_data[key] == recent_entry[0][key] for key in profile_data):
                return None
            profile_data['created_at'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            profile_data['follower_count'] = farc_user.follower_count
            profile_data['following_count'] = farc_user.following_count
            res = supabase.from_('profile_trackers').insert(profile_data).execute()
            return res.data
        except Exception as e:
            logging.error(f"error in post_profile_tracker_entry_by_fid: {e}")


    def get_recent_profile_tracker_entry_by_fid(self, fid: int):
        try:
            res = supabase.from_('profile_trackers').select('*').eq('fid', fid).order('created_at', desc=True).limit(1).execute()
            return res.data
        except Exception as e:
            logging.error(f"error in get_recent_profile_tracker_entry_by_fid: {e}")

    
    def get_profile_tracker_entries_by_fid(self, fid: int):
        try:
            res = supabase.from_('profile_trackers').select('*').eq('fid', fid).execute()
            return res.data
        except Exception as e:
            logging.error(f"error in get_profile_tracker_entries_by_fid: {e}")
    
    
    def get_trackees_by_manager_fid(self, manager_fid: int):
        try:
            res = supabase.from_('trackees').select('trackee_fid').eq('manager_fid', manager_fid).execute()
            return res.data
        except Exception as e:
            logging.error(f"error in get_trackees_by_manager_fid: {e}")
    
    
    def post_trackee_by_manager_fid(self, manager_fid: int, trackee_fid: int):
        try:
            existing_manager_trackee = supabase.from_('tracker_managers').select().eq('manager_fid', manager_fid).eq('trackee_fid', trackee_fid).execute()
            existing_trackee = supabase.from_('trackees').select().eq('fid', trackee_fid).execute()
            if not existing_manager_trackee.get('count'):
                if not existing_trackee.get('count'):
                    tracked = supabase.from_('trackees').insert({
                        'fid': trackee_fid
                    }).execute()
                res = supabase.from_('tracker_managers').insert({
                    'manager_fid': manager_fid,
                    'trackee_fid': trackee_fid
                }).execute()
                return res.data
            else:
                return "Manager and trackee already linked"
        except Exception as e:
            logging.error(f"error in post_trackee_by_manager_fid: {e}")


    def user_to_object(fid, max_attempts=3, retry_delay=1):
        attempts = 0
        while attempts < max_attempts:
            try:
                user = warpcast.get_user(fid)
                user_obj = {
                    'fid': fid,
                    'username': user.username,
                    'display_name': user.display_name,
                    'pfp_url': getattr(user.pfp, 'url', 'https://explorer.farcaster.xyz/avatar.png'),
                    'bio': user.profile.bio.text,
                    'follower_count': user.follower_count,
                    'following_count': user.following_count,
                }
                return user_obj
            except Exception as e:
                attempts += 1
                logging.error(f"Error in user_to_object for fid {fid}: {e}. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
        logging.error(f"Failed to get user for fid {fid} after {max_attempts} attempts.")
        return None