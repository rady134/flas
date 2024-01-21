from flask import Flask, jsonify, request
import youtube_dl

app = Flask(__name__)

def get_video_info(video_url):
    options = {
        'format': 'best',
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        return info_dict

@app.route('/get_video_info', methods=['GET'])
def api_get_video_info():
    video_url = request.args.get('video_url')

    if not video_url:
        return jsonify({"error": "Missing 'video_url' parameter"}), 400

    try:
        video_info = get_video_info(video_url)
        return jsonify(video_info)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

