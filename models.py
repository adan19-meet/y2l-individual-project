from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


# Write your classes here :
class User(Base):
	__tablename__ = "Users"
	user_id = Column(Integer, primary_key = True)
	username = Column(String)
	password = Column(String)
	email = Column(String)
	#picture = Column(String)

	def __repr__(self):
		return ("user name:{}, user pass:{}, user email: {}".format(self.username, self.password, self.email))


class Post(Base):
	__tablename__ = "Posts"
	post_id = Column(Integer, primary_key = True)
	username = Column(String)
	story = Column(String)
	topic = Column(String)
	def __repr__(self):
		return ("Post username: {}, Post story: {}, Post topic: {}".format(self.username, self.story, self.topic))

class Project(Base):
	__tablename__ = "Projects"
	project_id = Column(Integer,primary_key=True)
	username = Column(String)
	Project = Column(String)
	date= Column(String)
	time = Column(String)
	place = Column(String)
	def __repr__(self):
		return("Project username: {}, Project project: {}, Project date: {},Project time: {}, Project place: {}".format(self.username,self.Project,self.date,self.time,self.place))

class Messages(Base):
	__tablename__ = "Messages"
	messages_id = Column(Integer,primary_key=True)
	message = Column(String)
	user = Column(String)
	def __repr__():
		return("Messages message: {}".format(self.message))

class Feedback(Base):
	__tablename__ = "Feedback"
	feedback_id = Column(Integer,primary_key=True)
	name = Column(String)
	email = Column(String)
	message = Column(String)
	def __repr__():
		return("Feedback name: {}, Feedback email: {},Feedback message: {}".format(self.name , self.email , self.message))

		

		

		
