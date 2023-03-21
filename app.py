import os
from flask import Flask, render_template, request, send_file, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename
from video_sum import enter_url, sentiment_analysis, senti_analysis, combining_audio_video, vid_id
from article_sum import article_date, article_title, article_authors, article_summary, article_sentiment, senti_analysisa
from Action_Recognition import action_recognition_app
from Event_based import event_based_video
from Object_based import object_based_summarization
from images_to_video import images_to_video
from keyword_based_images import enter_url_images, keywords_images, sentiment_analysis_images, senti_analysis_images

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contact_info.db"
contact_info = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'src/input/files'


class contact(contact_info.Model):
    mes_id = contact_info.Column(contact_info.Integer, primary_key=True, autoincrement=True)
    name = contact_info.Column(contact_info.String(50), nullable = False)
    email = contact_info.Column(contact_info.String(50), nullable = False)
    subject = contact_info.Column(contact_info.String(100), nullable = False)
    msg = contact_info.Column(contact_info.String(300), nullable = False)
    datetime = contact_info.Column(contact_info.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return str(self.mes_id) + (self.subject)

with app.app_context():
    contact_info.create_all()

@app.route("/", methods=['GET','POST'])
def main():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['msg']
        con_info = contact(name=name, email=email, subject=subject, msg=msg)
        contact_info.session.add(con_info)
        contact_info.session.commit()
    all_con = contact.query.all()
    return render_template('index.html', all_con=all_con)

@app.route("/about")
def about():
    return render_template('base.html')

@app.route("/services")
def services():
    return render_template('index.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/video_sum")
def video_sum():
    return render_template('video_sum.html')

@app.route("/video_sum", methods=['GET','POST'])
def video_sum1():
    if request.method=='POST':
        url = request.form['url']
        summary = enter_url(url)
        sentiment = sentiment_analysis(summary)
        analysis = senti_analysis(summary)
    return render_template('video_sum.html',url=url, summary=summary, sentiment=sentiment, analysis=analysis)

@app.route("/article_sum")
def article_sum():
    return render_template('article_sum.html')

@app.route("/article_sum", methods=['GET','POST'])
def article_sum1():
    if request.method=='POST':
        url = request.form['url']
        date = article_date(url)
        title = article_title(url)
        authors = article_authors(url)
        summary = article_summary(url)
        sentiment = article_sentiment(url)
        analysisv = senti_analysisa(url)
    return render_template('article_sum.html', date=date, authors = authors, title = title, summary=summary, sentiment=sentiment, analysis=analysisv)

@app.route("/action_recognition")
def action_recognition():
    if os.path.exists ("static\\animation.gif") :
        os.remove ("static\\animation.gif")
    return render_template('action_recognition.html')

@app.route("/action_recognition", methods=['GET','POST'])
def action_recognition1():
    if request.method=='POST':
        url = request.form['url_act']
        action_recog = action_recognition_app(url)
    return render_template('action_recognition.html', action_recog0 = action_recog[0], action_recog1 = action_recog[1], action_recog2 = action_recog[2], action_recog3 = action_recog[3], action_recog4 = action_recog[4])

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/shorten_video')
def shorten_video1():
    form1 = UploadFileForm()
    if os.path.exists ("static\\shorten_video.mp4") :
        os.remove ("static\\shorten_video.mp4")
    return render_template('shorten_video.html', form1=form1)

@app.route('/shorten_video', methods=['GET','POST'])
def shorten_video2():
    form1 = UploadFileForm()
    if request.method=='POST':
        # option_radio = request.form.get("RadioOption", False)
        option_radio = request.form.get("RadioOption")
        print(option_radio)
        if option_radio=='Event based Video Summarization':
            print("fail")
            ans = 'event'
        elif option_radio=='Object based Video Summarization':
            ans = 'object'
        else:
            ans = "Please Select Option"
        if form1.validate_on_submit():
            file = form1.file.data 
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) 
            shorten_files = os.listdir('src\\input\\files\\')
            if ans=='event':
                event_based_video(f"src\\input\\files\\{shorten_files[0]}")
            elif ans=='object':
                object_based_summarization(f"src\\input\\files\\{shorten_files[0]}")
            elif ans=='Please Select Option':
                message_shorten = 'Please Select any Option' 
                return render_template('shorten_video.html', option_radio=option_radio,message_shorten=message_shorten, ans=ans, form1=form1)
            os.remove(f"src\\input\\files\\{shorten_files[0]}")
        return render_template('shorten_video.html', option_radio=option_radio,ans=ans, form1=form1)
    return render_template('shorten_video.html', form1=form1)

@app.route('/download_shorten')
def download_file():
    path = "static\\shorten_video.mp4" 
    return send_file(path, as_attachment=True)

@app.route('/simple_audios')
def simple_audios(): 
    if os.path.exists ("static\\simple_audio.mp4") :
        os.remove ("static\\simple_audio.mp4")
    return render_template('simple_audio.html')

@app.route("/simple_audios", methods=['GET','POST'])
def simple_audios1():
    if request.method=='POST':
        url = request.form['url']
        summary = enter_url(url)
        sentiment = sentiment_analysis(summary)
        analysis = senti_analysis(summary)
    return render_template('simple_audio.html', url=url, summary=summary, sentiment=sentiment, analysis=analysis)

@app.route('/download_audio')
def download_audio():
    path = "static/simple_audio.mp4" 
    return send_file(path, as_attachment=True)

@app.route('/random_videos')
def random_videos(): 
    if os.path.exists ("static\\random_videos.mp4") :
        os.remove ("static\\random_videos.mp4")
    return render_template('random_video.html')

@app.route("/random_videos", methods=['GET','POST'])
def random_videos1():
    if request.method=='POST':
        url = request.form['url']
        summary = enter_url(url)
        sentiment = sentiment_analysis(summary)
        analysis = senti_analysis(summary)
        video = combining_audio_video()
    return render_template('random_video.html', video=video, url=url, summary=summary, sentiment=sentiment, analysis=analysis)

@app.route('/download_random_video')
def download_random_video():
    path = "static/random_videos.mp4" 
    return send_file(path, as_attachment=True)

@app.errorhandler(404)
def page_not_found(e):
    return "<h2>Video/Audio will be shown here</h2>", 404

@app.route('/random_images')
def random_images():
    if os.path.exists ("static\\images_to_video.mp4") :
        os.remove ("static\\images_to_video.mp4")
    return render_template('random_images.html')

@app.route("/random_images", methods=['GET','POST'])
def random_images1():
    if request.method=='POST':
        url = request.form['url']
        summary = enter_url(url)
        sentiment = sentiment_analysis(summary)
        analysis = senti_analysis(summary)
        video = images_to_video()
    return render_template('random_images.html', video=video, url=url, summary=summary, sentiment=sentiment, analysis=analysis)

@app.route('/download_random_images')
def download_random_images():
    path = "static/images_to_video.mp4" 
    return send_file(path, as_attachment=True)

@app.route("/image_generation")
def image_generation():
    if os.path.exists ("static\\gen_image.png") :
        os.remove ("static\\gen_image.png")
    return render_template('image_generation.html')

@app.route("/image_generation", methods=['GET','POST'])
def image_generation1():
    if request.method=='POST':
        prompt = request.form['prompt']
        # generated_image = image_generation_code(prompt)
    return render_template('image_generation.html',prompt=prompt)

@app.route('/download_generated_image')
def download_generated_image():
    path = "static/gen_image.png" 
    return send_file(path, as_attachment=True)

@app.route('/summary_based_video')
def summary_based_video(): 
    # if os.path.exists ("static\\random_videos.mp4") :
    #     os.remove ("static\\random_videos.mp4")
    return render_template('keyword_based_video.html')

@app.route("/summary_based_video", methods=['GET','POST'])
def summary_based_video1():
    if request.method=='POST':
        url = request.form['url']
        summary = enter_url_images(url)
        keywords = keywords_images(summary)
        sentiment = sentiment_analysis_images(summary)
        analysis = senti_analysis_images(summary)
    return render_template('keyword_based_video.html', url=url, keywords = keywords, summary=summary, sentiment=sentiment, analysis=analysis)

# @app.route('/download_random_video')
# def download_random_video():
#     path = "static/random_videos.mp4" 
#     return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0",port=5555) 