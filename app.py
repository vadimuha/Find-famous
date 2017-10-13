from flask import Flask,url_for,render_template,request,jsonify
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("db.sqlite",check_same_thread=False)
db = conn.cursor()

''' Backend created by Vadim Igorovich vadimuha13@gmail.com '''

@app.route("/", methods=["GET","POST"])
def index():
	return render_template("index.html")

def select_type(table,column_name,search_by,query):
	db.execute("SELECT {} FROM {} WHERE {} LIKE ? GROUP BY {}".format(column_name,table,search_by,column_name),[('%{}%'.format(query))])
	result = db.fetchall()
	return result
def select_all_actors(query):
	db.execute("SELECT actor_1_name,actor_2_name,actor_3_name FROM data WHERE actor_1_name LIKE ? OR actor_2_name LIKE ? OR actor_3_name LIKE ? GROUP BY actor_1_name,actor_2_name,actor_3_name",(["%{}%".format(query),"%{}%".format(query),"%{}%".format(query)]))
	result = db.fetchall()
	return result

@app.route("/get_acrot")
def get_actor():
	if request.method == "GET":
		name = request.args.get("q")
		directors = select_type("data","director_name","director_name",name)
		actors = select_all_actors(name)
		nobel = select_type("nobel","firstname,surname,category,motivation,name","firstname",name)
		json = [0]*3
		json[0] = directors
		json[1] = actors
		json[2] = nobel
		return jsonify(json)