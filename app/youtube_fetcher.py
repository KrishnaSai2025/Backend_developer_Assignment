import requests
from .models import Video
from . import db
from datetime import datetime

YOUTUBE_API_KEYS = ["YOUR_API_KEY"]
SEARCH_QUERY = "cricket"
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

def fetch_and_store_videos():
    for api_key in YOUTUBE_API_KEYS:
        params = {
            'part': 'snippet',
            'q': SEARCH_QUERY,
            'type': 'video',
            'order': 'date',
            'maxResults': 5,
            'key': api_key,
        }
        response = requests.get(YOUTUBE_SEARCH_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            for item in data.get('items', []):
                video_id = item['id']['videoId']
                snippet = item['snippet']

                if not Video.query.get(video_id):
                    video = Video(
                        id=video_id,
                        title=snippet['title'],
                        description=snippet['description'],
                        published_at=datetime.fromisoformat(snippet['publishedAt'].replace('Z', '+00:00')),
                        thumbnail_url=snippet['thumbnails']['high']['url'],
                    )
                    db.session.add(video)
            db.session.commit()
            break
        else:
            continue
