from flask import Flask
from flask_restful import Api
from controllers import UsersController, EventsController, ProgramsController

app = Flask(__name__)
api = Api(app)

api.add_resource(UsersController, '/users', endpoint='users')
api.add_resource(EventsController, '/events', endpoint='events')
api.add_resource(ProgramsController, '/programs', endpoint='programs')

if __name__ == '__main__':
    app.run(debug=True)

