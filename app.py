from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Mock data for testing
comments_data = [
    {"at": "2023-01-15", "author": "Fredrick", "like": 3, "reply": 2, "text": "Economic comment"},
    {"at": "2023-01-20", "author": "Alice", "like": 1, "reply": 0, "text": "Random comment"},
    {"at": "2023-01-25", "author": "Fredrick", "like": 5, "reply": 3, "text": "Another economic comment"},
]

def filter_comments(criteria):
    filtered_comments = comments_data

    # Filter by author name
    if 'search_author' in criteria:
        filtered_comments = [c for c in filtered_comments if criteria['search_author'].lower() in c['author'].lower()]

    # Filter by date range
    if 'at_from' in criteria and 'at_to' in criteria:
        at_from = datetime.strptime(criteria['at_from'], '%d-%m-%Y')
        at_to = datetime.strptime(criteria['at_to'], '%d-%m-%Y')
        filtered_comments = [c for c in filtered_comments if at_from <= datetime.strptime(c['at'], '%Y-%m-%d') <= at_to]

    # Filter by like and reply count range
    if 'like_from' in criteria and 'like_to' in criteria:
        filtered_comments = [c for c in filtered_comments if criteria['like_from'] <= c['like'] <= criteria['like_to']]

    if 'reply_from' in criteria and 'reply_to' in criteria:
        filtered_comments = [c for c in filtered_comments if criteria['reply_from'] <= c['reply'] <= criteria['reply_to']]

    # Filter by search text
    if 'search_text' in criteria:
        filtered_comments = [c for c in filtered_comments if criteria['search_text'].lower() in c['text'].lower()]

    return filtered_comments

@app.route('/search', methods=['GET'])
def search_comments():
    criteria = request.args.to_dict()
    search_results = filter_comments(criteria)
    return jsonify(search_results)

if __name__ == '__main__':
    app.run(debug=True)
