from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
import resolver as r


app = Flask(__name__)

type_defs = load_schema_from_path('schema.graphql')

#query = QueryType()
query = ObjectType("Query")
mutation = ObjectType("Mutation")
student = ObjectType('Student')
classes = ObjectType('Classes')

#Set Query fields
query.set_field("student",r.getStudents)
query.set_field("class",r.getClasses)

#Set Mutation fields
mutation.set_field("newStudent",r.addStudent)
mutation.set_field("newClass",r.addClass)
mutation.set_field("updateClass",r.updateClass)

schema = make_executable_schema(type_defs, [query, student, classes, mutation])

@app.route('/graphql', methods=['GET'])
def playground():
    return PLAYGROUND_HTML, 200
    
@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
    schema,
    data,
    context_value=None,
    debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code