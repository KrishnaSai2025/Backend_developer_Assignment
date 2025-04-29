# YouTube Fetcher Flask App + Streamlit UI

## Setup

```bash
git clone <repo_url>
cd youtube_fetcher_flask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

## Docker

```bash
docker build -t youtube-fetcher .
docker run -p 5000:5000 youtube-fetcher
```

## API Endpoints

- `GET /videos` - Paginated videos
- `GET /search?query=...` - Search videos

## Streamlit UI

```bash
streamlit run streamlit_app.py
```
