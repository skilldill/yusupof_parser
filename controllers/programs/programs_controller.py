from flask_restful import Resource
from ysupof_parser import parser


class ProgramsController(Resource):
    def get(self):
        programs = parser.get_programs()
        return programs
