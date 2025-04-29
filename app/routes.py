from flask import Blueprint, request, jsonify
from .models import Video
from . import db

main = Blueprint('main', __name__)

@main.route('/videos')
def get_videos():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    videos = Video.query.order_by(Video.published_at.desc()).paginate(page=page, per_page=per_page)
    result = [{
        'id': v.id,
        'title': v.title,
        'description': v.description,
        'published_at': v.published_at.isoformat(),
        'thumbnail_url': v.thumbnail_url,
    } for v in videos.items]

    return jsonify({
        'videos': result,
        'total': videos.total,
        'pages': videos.pages,
        'current_page': videos.page,
    })

@main.route('/search')
def search_videos():
    query = request.args.get('query', '')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    videos = Video.query.filter(
        (Video.title.ilike(f'%{query}%')) | (Video.description.ilike(f'%{query}%'))
    ).order_by(Video.published_at.desc()).paginate(page=page, per_page=per_page)

    result = [{
        'id': v.id,
        'title': v.title,
        'description': v.description,
        'published_at': v.published_at.isoformat(),
        'thumbnail_url': v.thumbnail_url,
    } for v in videos.items]

    return jsonify({
        'videos': result,
        'total': videos.total,
        'pages': videos.pages,
        'current_page': videos.page,
    })
