from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('cafe location', validators=[DataRequired()])
    opening_time = StringField('opening timeing', validators=[DataRequired()])
    closing_time = StringField('closeing timeing', validators=[DataRequired()])
    coffie_rating = SelectField('coffie rataing', choices=['☕️', '☕️☕️', '☕️☕️☕', '☕☕☕☕', '☕☕☕☕☕'])
    wifi_strength_rating = SelectField('wifi strength rating', choices=['✘', '💪', '💪💪️', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    power_socket = SelectField('power socket Availability', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe() -> None:
    """
    Saves form entered data to csv.
    Arguments:
        None
    Return:
        None
    """
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='', encoding="utf8") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.cafe_location.data},"
                           f"{form.opening_time.data},"
                           f"{form.closing_time.data},"
                           f"{form.coffie_rating.data},"
                           f"{form.wifi_strength_rating.data},"
                           f"{form.power_socket.data}")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            print(row)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

