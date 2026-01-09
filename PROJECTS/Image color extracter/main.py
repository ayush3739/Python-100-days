from flask import Flask,render_template,redirect,Response,request
from PIL import Image
from collections import Counter
import os

app=Flask(__name__)
app.secret_key='secret-key'



def img_color_extracter(image_file):
    try:
        img = Image.open(image_file)
        img = img.resize((150, 150))
        img = img.convert('RGB')
        
        pixels = list(img.getdata())
        total_pixels = len(pixels)
        counter = Counter(pixels)
        most_common = counter.most_common(20)
        
        colors = [{'rgb': color, 'hex': '#{:02x}{:02x}{:02x}'.format(*color), 'percentage': round((count / total_pixels) * 100, 2)} 
                  for color, count in most_common]
        return colors
    except Exception as e:
        return []

@app.route('/',methods=["GET",'POST'])
def home():
    colors = []
    demo_image_path = 'static/demo_image.png'
    
    if request.method=="POST":
        image = request.files.get('image-input')
        if image:
            # Save uploaded image temporarily
            upload_path = 'static/uploaded_image.png'
            image.save(upload_path)
            colors = img_color_extracter(upload_path)
            return render_template('home.html', colors=colors, is_demo=False)
    
    # Load demo image on initial GET request
    try:
        colors = img_color_extracter(demo_image_path)
    except Exception as e:
        print(f"Error loading demo image: {e}")
        colors = []
    
    return render_template('home.html', colors=colors, is_demo=True)


if __name__=="__main__":
    app.run(debug=True)