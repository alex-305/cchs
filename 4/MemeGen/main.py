from flask import Flask, render_template, request, send_from_directory
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
MEME_FOLDER = "static/memes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MEME_FOLDER, exist_ok=True)


def add_text_to_image(image_path, top_text, bottom_text, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    # Load font
    try:
        font = ImageFont.truetype("/System/Library/Fonts/NewYork.htf", 100)  # Adjust font size as needed
    except IOError:
        font = ImageFont.load_default()


    # Define text position
    text_color = "white"
    outline_color = "black"

    def draw_text(draw, text, position, font, text_color, outline_color):
        x, y = position

        # Outline effect for better visibility
        offsets = [-2, 2]
        for dx in offsets:
            for dy in offsets:
                draw.text((x + dx, y + dy), text, font=font, fill=outline_color)

        # Main text
        draw.text(position, text, font=font, fill=text_color)

    # Draw top text
    draw_text(draw, top_text.upper(), (image.width // 10, 10), font, text_color, outline_color)

    # Draw bottom text
    draw_text(draw, bottom_text.upper(), (image.width // 10, image.height - 60), font, text_color, outline_color)

    # Save meme
    image.save(output_path)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        top_text = request.form["top_text"]
        bottom_text = request.form["bottom_text"]
        
        if file:
            filename = file.filename
            img_path = os.path.join(UPLOAD_FOLDER, filename)
            meme_path = os.path.join(MEME_FOLDER, "meme_" + filename)
            file.save(img_path)

            # Generate meme
            add_text_to_image(img_path, top_text, bottom_text, meme_path)

            return render_template("index.html", meme_path=meme_path)
    
    return render_template("index.html", meme_path=None)

@app.route("/static/memes/<filename>")
def meme_file(filename):
    return send_from_directory(MEME_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)

