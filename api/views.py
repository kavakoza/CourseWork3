from flask import jsonify, Blueprint
from dao.dao_ import PostManagerDAO
import logging

api_blueprint = Blueprint('api_blueprint', __name__)
posts = PostManagerDAO('data/posts.json', 'data/comments.json')
logging.basicConfig(filename='logs/api.log', encoding='utf-8',level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts():
    logging.info(f'Запрос /api/posts/')
    return jsonify(posts.load_posts_json())

@api_blueprint.route('/api/posts/<int:postid>', methods=['GET'])
def get_post_by_id(postid):
    logging.info(f'Запрос /api/posts/{postid}')
    return jsonify(posts.get_post_by_pk_json(postid))



