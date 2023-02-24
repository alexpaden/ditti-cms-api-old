GET /api/v1/follow-trackers/{fid}
Description: Get the follow trackers for a given fid.
Parameters:
fid: integer (required)
Response:
Status code: 200 (OK)
Body: JSON object containing follow trackers data.

POST /api/v1/follow-trackers/{fid}
Description: Request the post follow tracker service to run for a given fid.
Parameters:
fid: integer (required)
Response:
Status code: 200 (OK)
Body: JSON object containing response data.

GET /api/v1/profile-trackers/{fid}
Description: Get the profile trackers for a given fid.
Parameters:
fid: integer (required)
Response:
Status code: 200 (OK)
Body: JSON object containing profile trackers data.

POST /api/v1/profile-trackers/{fid}
Description: Request the post profile tracker service to run for a given fid.
Parameters:
fid: integer (required)
Response:
Status code: 200 (OK)
Body: JSON object containing response data.

GET /api/v1/trackees/{fid}
Description: Get all trackees for a given manager fid.
Parameters:
fid: integer (required)
Response:
Status code: 200 (OK)
Body: JSON object containing trackees data.

POST /api/v1/tracker-manager
Description: Post a new tracker manager with manager and trackee fids.
Body: JSON object containing manager_fid and trackee_fid.
Response:
Status code: 200 (OK)
Body: JSON object containing response data.
