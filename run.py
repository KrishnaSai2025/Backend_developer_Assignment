from app import create_app, db
from app.youtube_fetcher import fetch_and_store_videos
from apscheduler.schedulers.background import BackgroundScheduler

app = create_app()

with app.app_context():
    db.create_all()

scheduler = BackgroundScheduler()
scheduler.add_job(func=lambda: fetch_and_store_videos(), trigger="interval", seconds=10)
scheduler.start()

if __name__ == "__main__":
    app.run(debug=True)
