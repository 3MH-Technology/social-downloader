import gradio as gr
import yt_dlp
import os

# حقوق المشروع
BRANDING = "White Wolf Downloader 🐺"
DEVELOPER = "@j49_c"

def get_download_link(url):
    if not url:
        return "يرجى إدخال رابط صالح"
    
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get('url')
            title = info.get('title', 'video')
            return f"### [اضغط هنا لتحميل: {title}]({video_url})"
    except Exception as e:
        return f"خطأ: {str(e)}"

# بناء الواجهة بتصميم داكن (Cyberpunk Style)
with gr.Blocks(theme=gr.themes.Soft(primary_hue="cyan", neutral_hue="slate")) as demo:
    gr.Markdown(f"# {BRANDING}")
    gr.Markdown(f"### Developed by {DEVELOPER} | White Wolf Infrastructure")
    
    with gr.Row():
        url_input = gr.Textbox(placeholder="ضع رابط الفيديو من (TikTok, Instagram, YouTube...)", label="رابط الفيديو")
    
    download_btn = gr.Button("استخراج رابط التحميل", variant="primary")
    output = gr.Markdown(label="النتيجة")

    download_btn.click(fn=get_download_link, inputs=url_input, outputs=output)

    gr.HTML(f"<div style='text-align:center; margin-top:20px; color:#555;'>© 2026 {BRANDING}</div>")

if __name__ == "__main__":
    demo.launch()
