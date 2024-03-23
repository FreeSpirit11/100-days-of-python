from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

MOVIE_DB_API_KEY = '518d2b345ead650e1be31072fc69ade0'
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_DETAILS_URL = f"https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


class RateMovieForm(FlaskForm):
    rating = FloatField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label='Done')


class FindMovieForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
        db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=['POST', 'GET'])
def rate_movie():
    id = request.args.get('id')
    selected_movie = db.get_or_404(Movie, id)
    form = RateMovieForm()
    if request.method == 'POST' and form.validate_on_submit():
        selected_movie.rating = form.rating.data
        selected_movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=selected_movie, form=form)


@app.route('/delete/<id>')
def delete_movie(id):
    # alternative way can be
    # id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    form = FindMovieForm()
    if request.method == 'POST':
        movie_title = form.title.data
        params = {
            'api_key': MOVIE_DB_API_KEY,
            'query': f'{movie_title}',
        }
        response = requests.get(MOVIE_DB_SEARCH_URL, params=params)
        response.raise_for_status()
        data = response.json()["results"]
        return render_template('select.html', options=data)
    return render_template('add.html', form=form)


@app.route('/find')
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        response = requests.get(f"{MOVIE_DB_DETAILS_URL}/{movie_api_id}", params={'api_key': MOVIE_DB_API_KEY})
        response.raise_for_status()
        movie_data = response.json()
        title = movie_data['original_title']
        img_url = f'{MOVIE_DB_IMAGE_URL}/{movie_data["poster_path"]}'
        year = movie_data['release_date'].split("-")[0]
        description = movie_data['overview']

        new_movie = Movie(title=title, img_url=img_url, year=year, description=description)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('rate_movie', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
