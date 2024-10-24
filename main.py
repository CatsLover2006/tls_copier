from flask import request, Flask, Response
import requests

app = Flask(__name__)

@app.route('/<path:url>')
def fallback(url):
    r = requests.get(url, stream=True)
    return Response(r.iter_content(chunk_size=10*1024),
                    content_type=r.headers['Content-Type'],
                    status=r.status_code)

app.run(port=66, host="0.0.0.0")
