# -*- coding: utf-8 -*-
"""
Created on Sat May 29 09:36:33 2021

@author: gcferna2
"""
# import libraries
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'                # relative path 
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    views = db.Column(db.Integer, nullable = False)
    likes = db.Column(db.Integer, nullable = False)
    
    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes})"        

# db.create_all()  # create only once in the beginning in order to not overwrite the data.

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type = str, help="Required name of the video", required = True)
video_put_args.add_argument("views", type = int, help="Required views of the video", required=True)
video_put_args.add_argument("likes", type = int, help="Required likes of the video", required=True)


video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type = str, help="Name of the video")
video_update_args.add_argument("views", type = int, help="Views of the video")
video_update_args.add_argument("likes", type = int, help="Likes of the video")



# along with marshal_with returns a serializable json of the query from VideoModel instance.
resource_fields = {                                                            
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
    } 


# Resource helps us handle GET, PUT, DELETE requests
class Video(Resource):
    
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, messages = "could not find video")
        return result
    
    @marshal_with(resource_fields)    
    def put(self, video_id):                                                   # most likely to be POST
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id).first()
        if result:
            abort(409, messages = "video already exists")
            
        video = VideoModel(id =video_id, name = args["name"], views = args["views"], likes = args["likes"])
        db.session.add(video)
        db.session.commit()
        return video, 201
    
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id).first()
        
        if not result:
            abort(404, message = "video does not exist")
        if args['name']:
            result.name = args["Name"]
        if args['views']:
            result.views = args["views"]
        if args['likes']:
            result.views = args["likes"]
        
        db.session.commit()
        
        return result
    
    def delete(self, video_id):
        del videos[video_id]
        return '', 204    
        
    
# how do we find the resource
api.add_resource(Video, "/video/<int:video_id>")   
    
    
if __name__ == "__main__":
    app.run(debug=True)
