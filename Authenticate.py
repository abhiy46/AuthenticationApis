from flask import Flask,jsonify,request
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome!"

@app.route("/create" , methods=['GET','POST'])
def Create():
    if (request.method == 'POST'):
        with open('data4.json', 'r') as f:
            data = json.loads(f.read())
            dataFromPost = request.get_json()
            data.append(dataFromPost)
            with open('data4.json','w') as out:
                out.write(json.dumps(data))
            return jsonify({"you sent":dataFromPost}),201

@app.route("/Login" , methods=['GET','POST'])
def Login():
    if (request.method == 'POST'):
        dataFromPost = request.get_json()#read data from request 
        dataStr = json.dumps(dataFromPost)
        dataJson = json.loads(dataStr)#convert the data to json
        email = dataJson["email"]
        password = dataJson["password"]
        with open('data4.json', 'r') as f:
            data = json.loads(f.read())
            
            for i in range(len(data)):
                if((data[i]['email']==email) and (data[i]['password']==password)):
                    
                    return jsonify({"Login successfull, Welcome":data[i]["name"]})
            
            return jsonify({"Login Failure":""})

@app.route("/Reset" , methods=['GET','POST'])
def Reset():
    if (request.method == 'POST'):
        dataFromPost = request.get_json()#read data from request 
        dataStr = json.dumps(dataFromPost)
        dataJson = json.loads(dataStr) #convert the data to json
        email = dataJson["email"]
        NewPassword = dataJson["NewPassword"]
        with open('data4.json', 'r') as f:
            data = json.loads(f.read())
            
            for i in range(len(data)):
                if((data[i]['email']== email)):
                    data[i]['password']=NewPassword
                    with open('data4.json','w') as out:
                        out.write(json.dumps(data))
                    return jsonify({"Password changed successfully!":""})
                
                
            return jsonify({"No records found":""})



        
if __name__ == '__main__':
    app.run(debug=True)
