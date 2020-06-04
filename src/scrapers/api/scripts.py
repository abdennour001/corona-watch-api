from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from random import sample
from ..models import YoutubeVideo
import requests


def remove_old_videos():
    print("[*] Remove old videos...")
    videos = YoutubeVideo.objects.all()
    for video in videos:
        video.delete()


def scrap_youtube_videos():
    print("[*] Refresh database with new videos...")
    api_key = settings.SCRAPERS_SETTINGS.get("YOUTUBE").get("YOUTUBE_API_KEY")
    query = sample(settings.SCRAPERS_SETTINGS.get("YOUTUBE").get("QUERY_SET"), 1)[0]
    max_results = settings.SCRAPERS_SETTINGS.get("YOUTUBE").get("MAX_RESULTS")
    youtube_api_response = requests.get(
        f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={api_key}&type=video&maxResults={max_results}"
    )
    for item in sample(youtube_api_response.json()['items'], len(youtube_api_response.json()['items'])):
        video = YoutubeVideo(
            video_embed_url=f"http://www.youtube.com/embed/{item.get('id').get('videoId')}",
            video_id=item.get('id').get('videoId'),
            published_at=item.get("snippet").get("publishedAt"),
            title=item.get("snippet").get("title"),
            description=item.get("snippet").get("description"),
            channel_title=item.get("snippet").get("channelTitle"),
        )
        video.save()


def main():
    remove_old_videos()
    scrap_youtube_videos()


def run():
    scheduler = BackgroundScheduler()
    scheduler.add_job(main, 'interval', hours=23)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler error.")
