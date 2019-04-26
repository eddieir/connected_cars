from flask import Flask, render_template
from flask_socketio import SocketIO
import socket
import urllib
from werkzeug import secure_filename
import os
from datetime import datetime as dt
import json
from flask import Flask, abort, request
from flask import send_file

app = Flask(__name__,template_folder="templates")
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


current_user = "Eddie"
def allowed_file(filename):
        return '.' in filename and \
        filename.rsplit('.', 1)[1]     
def uploadFile():
    format = "%Y-%m-%dT%H:%M:%S"
    now = dt.utcnow().strftime(format)
    try:
        file = request.files['file']
    except:
        file = None
    try:
        url = request.form['url']
    except:
        url = None

    if file and allowed_file(file.filename):
        filename = now + '_' +str(current_user) + '_' + file.filename
        filename = secure_filename(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_uploaded = True

    elif url:
        format = "%Y-%m-%dT%H:%M:%S"
        now = dt.utcnow().strftime(format)
        file = urllib.request.urlopen(url)
        filename = url.split('/')[-1]
        filename = now + '_' +str(current_user) + '_' + filename
        filename = secure_filename(filename)

        if file and allowed_file(filename):
            open(os.path.join(app.config['UPLOAD_FOLDER'], filename),
                     'wb').write(file.read())
            file_uploaded = True

        else:
            filename = None
            file_uploaded = False

        return file_uploaded, filename 
@app.route("/information")
def data():
    import flask
    from flask import jsonify
    try:

        # Initialize a employee list
        employeeList = []

        # create a instances for filling up employee list
        for i in range(0,2):
            empDict = {
                'firstName': 'Roy',
                'lastName': 'Augustine'}

            employeeList.append(empDict)
    
        # convert to json data
        jsonStr = json.dumps(employeeList)

    except Exception as e:
        print (str(e))

    return flask.jsonify(Employees=jsonStr)

@app.route('/InputTXTdata',methods= ['GET','POST']) # it need to modify
def InputTXTdata():
    if not request.json:
        abort(400)
    print(request.json)
    return json.dumps(request.json)
@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader/', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      #return f
      return 'file uploaded successfully'

@app.route('/file-download/')
def file_download():
    try:
        return render_template('downloads.html')
    except Exception as e:
        return str(e)    
@app.route('/return-files/')
def return_file():
    try:
        data = send_file('/home/eddie/Desktop/connecred_car/MockServer/Python_Flask_Server/static/data1.json')
        print(data)
        return data

    except Exception as e:
        return str(e)

"""
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: '+ str(json))
    socketio.emit('my response', json, callback=messageReceived)    
"""
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=123456789)
    socketio.run(app, debug=True)
    
