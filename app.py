from flask import Flask, render_template, url_for, redirect, request, session
import databases

app = Flask(__name__)
app.config['SECRET_KEY'] = 'https://www.researchgate.net/publication/318429418_A_128-bit_secret_key_generation_using_un'

current_username = None

@app.route('/' ,  methods=['GET','POST'])
def home():
	if request.method == "POST":
		name = request.form["name"]
		email = request.form["email"]
		message = request.form["message"]
		databases.add_feedback(name=name,email=email,message=message)
		return render_template("home.html")

	
	else:
		return render_template("home.html")


@app.route('/login' , methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        user = databases.query_by_name(request.form["username"])
        print(request.form['username'])
        if user is not None:
            if user.password == request.form["password"]:
                session['username'] = user.username
                global current_username
                current_username = user.username
                return redirect(url_for("home", username = user.username))

            else:
                error = 'password does not match'
                return render_template('home.html', error = error)
        else:

            error = 'username does not exist'
            return render_template('home.html', error = error)

    else:

        return render_template('login.html')


@app.route('/signup' ,  methods = ['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        name = request.form['username']
        password = request.form['password']
        email = request.form['email']
        print("form posted")
        
        databases.add_user(name , password, email)
        return redirect(url_for("login"))


@app.route('/womenpolitics',methods=['GET','POST'])
def womenpolitics():
	if request.method == 'GET':
		womenpoliticspost = databases.query_by_topic("womenpolitics")
		return render_template("womenpolitics.html" , womenpoliticspost=womenpoliticspost)
	else:
		return render_template("womenpolitics.html")

@app.route('/discussion',methods=["GET","POST"])
def discussion():
	if request.method == 'GET':
		return render_template("discussion.html")
	else:
		message = request.form['message']
		global current_username
		user = current_username
		databases.add_message(message, user)
		all_my_messages = databases.query_all_message()
		return render_template("discussion.html",all_my_messages=all_my_messages)

@app.route('/projects', methods=["POST","GET"])
def projects():
	if request.method == 'POST':
		username = request.form['username']
		project = request.form['project']
		date = request.form['date']
		time=request.form['time']
		place = request.form['place']
		databases.add_project(username,project,date,time,place)
		all_my_projects = databases.query_all_projects()


		return render_template("projects.html", all_my_projects=all_my_projects)
	else:
		all_my_projects = databases.query_all_projects()
		return render_template("projects.html", all_my_projects=all_my_projects)
@app.route('/profile/<string:username>')
# def profile(username):
# 	user = databases.query_by_name(username)
# 	if user is not None:
# 		return render_template('profile.html', user = user)
# 	else:
# 		return redirect(url_for('login'))
@app.route('/stories' , methods=['GET','POST'])
def stories():
	print(request.method)
	if request.method == 'GET':
		return render_template('stories.html')
	else:
		username = request.form['username']
		story = request.form['story']
		topic = request.form.get('topics')
		databases.add_post(username,story,topic)
		return redirect(url_for('womenpolitics'))

if __name__ == '__main__':
	app.run(debug=True)

