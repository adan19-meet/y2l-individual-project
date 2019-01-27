from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_user(username, password, email):
	print("Added a user!")
	user = User(username = username, password = password, email=email)
	session.add(user)
	session.commit()

def query_all_users():
	return session.query(User).all()

def query_by_name(username):
	return session.query(User).filter_by(username = username).first()

def query_by_username(username):
	return session.query(Post).filter_by(username = username).all()

def add_post(username,story,topic):
	print("Added a post!")
	post = Post(username=username, story=story, topic=topic)
	session.add(post)
	session.commit()

def query_by_topic(topic):
	return session.query(Post).filter_by(topic = topic).all()
def query_all_posts():
	return session.query(Post).all()

def add_project(username,project,date,time,place):
	print("added a project")
	project = Project(username=username,Project=project,date=date,time=time,place=place)
	session.add(project)
	session.commit()

def query_all_projects():
	return session.query(Project).all()


def add_message(message, user):
	message = Messages(message=message, user = user)
	session.add(message)
	session.commit()

def query_all_message():
	return session.query(Messages).all()
def add_feedback(name,email,message):
	feedback = Feedback(name=name,email=email,message=message)
	session.add(feedback)
	session.commit
	print("feedback")
def query_all_feedback(name,email,message):
	return session.query(Feedback).all()
