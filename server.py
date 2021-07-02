import csv
from os import name
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)     # An instance of FlaskApp


@app.route('/')  # Decorator 'route'
def my_home():
    return render_template('./index.html')


@app.route('/<string:page_name>')  # Decorator 'route'
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        # 'a': append this file
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{name}, {email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        # 'a': append this file
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # csv_writer.writerow(['Name', 'email', 'subject', 'Message'])
        csv_writer.writerow([name, email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'],)
# GET: it means that the browser wants us to send information
# POST: it means that the browser wants us to save information
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # Put all the data into a dictionary
            write_to_csv(data)
            name_user = data['name']
            return redirect(url_for("thankyou_it", name=name_user))
        except:
            return 'Did not save to Database'
    else:
        return "something went wrong. Try again!"


@app.route("/thankyou_it/<name>")
def thankyou_it(name):
    return render_template("./ThankYou.html", name=name)


@app.route('/thankyou_it/contact.html')  # Decorator 'route'
def html_comeback_contact():
    return redirect(url_for("html_page", page_name='contact.html'))


@app.route('/thankyou_it/works.html')  # Decorator 'route'
def html_comeback_works():
    return redirect(url_for("html_page", page_name='works.html'))


@app.route('/thankyou_it/about.html')  # Decorator 'route'
def html_comeback_about():
    return redirect(url_for("html_page", page_name='about.html'))


@app.route('/thankyou_it/index.html')  # Decorator 'route'
def html_comeback_home():
    return redirect(url_for("html_page", page_name='index.html'))
