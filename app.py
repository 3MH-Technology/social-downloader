from flask import Flask, request, jsonify, render_template, send_file
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_video(url):
    ydl_opts = {
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        'format': 'best'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return filename

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/download", methods=["POST"])
def api_download():
    url = request.json.get("url")

    if not url:
        return jsonify({"error": "No URL"}), 400

    try:
        file_path = download_video(url)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return jsonify({
            "error": str(e),
            "developer": "White Wolf | @j49_c"
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
