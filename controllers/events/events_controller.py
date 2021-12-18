from flask_restful import Resource
from ysupof_parser import parser


class EventsController(Resource):

    def get(self):
        events = parser.get_events()
        return events

