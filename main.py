from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test2.db'
app.config['SQLALCEHMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class History(db.Model):
    id = db.Column('id',db.Integer, primary_key=True)
    message = db.Column('message',db.String(500))
    time = db.Column('time',db.String(500))

@app.route('/')
def sessions():
    messages = History.query.all()
    return render_template('message.html',messages=messages[::-1])

def messageReceived(methods=['GET','POST']):
    print('message was recieved!')

@socketio.on('my event')
def handle_my_custom_event(json,methods=['GET','POST']):
    print('recieved my event: ' +str(json))

    message = History(message=str(json['message']),time=str(json['time_of_post']))
    db.session.add(message)
    db.session.commit()

    socketio.emit('my response',json, callback=messageReceived)



if __name__=='__main__':
    socketio.run(app, debug=True)
#$( 'input.username' ).val()

#{$ for msg in messages %}
#    append


