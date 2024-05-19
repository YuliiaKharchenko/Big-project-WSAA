# flask server that links to an activitiesDAO


from flask import Flask, jsonify, request, abort
from activitiesDAO import activitiesDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"



@app.route('/activities')
def get_all():
    # print("in getall")
    results = activitiesDAO.get_all()
    return jsonify(results)



@app.route('/activities/<int:number>')
def find_by_number(number):
    foundactivity = activitiesDAO.find_by_number(number)

    return jsonify(foundactivity)



@app.route('/activities', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
     
    activities = {
        "category": request.json["category"],
        "name": request.json["name"],
        "duration": request.json["duration"],
    }
    addedactivity = activitiesDAO.create(activities)
    
    return jsonify(addedactivity)



@app.route('/activities/<int:number>', methods=['PUT'])
def update(number):
    foundactivity = activitiesDAO.find_by_number(number)
    if not foundactivity:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if "duration" in reqJson and type(reqJson["duration"]) is not int:
        abort(400)

    if "category" in reqJson:
        foundactivity["category"] = reqJson["category"]
    if "name" in reqJson:
        foundactivity["name"] = reqJson["name"]
    if "duration" in reqJson:
        foundactivity["duration"] = reqJson["duration"]
    activitiesDAO.update(number,foundactivity)
    return jsonify(foundactivity)
        

    

@app.route('/activities/<int:number>' , methods=['DELETE'])
def delete(number):
    activitiesDAO.delete(number)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)