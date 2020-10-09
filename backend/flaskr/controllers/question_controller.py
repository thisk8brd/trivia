from flask import jsonify
from app import app
from decorators import parse_request, Argument, marshal_with
from flaskr.controllers.category_controller import get_categories
from models import Question
from flaskr.repositories.question_repository import QuestionRepository
from flaskr.repositories.category_repository import CategoryRepository
from schemas import QuestionCollectionSchema


repository = QuestionRepository()
category_repository = CategoryRepository()

"""
@TODO: 
Create an endpoint to handle GET requests for questions, 
including pagination (every 10 questions). 
This endpoint should return a list of questions, 
number of total questions, current category, categories. 
TEST: At this point, when you start the application
you should see questions and categories generated,
ten questions per page and pagination at the bottom of the screen for three pages.
Clicking on the page numbers should update the questions. 
"""


@app.route("/api/questions")
@parse_request(
    [
        Argument(name="page", default=10, type=int),
        Argument(name="offset", default=1, type=int),
        Argument(name="current_category", default=None, type=str),
    ]
)
@marshal_with(QuestionCollectionSchema())
def get_questions(page, offset, current_category=None):
    categories = category_repository.filter().all()
    query = repository.filter()
    count = query.count()
    questions = query.limit(page).offset(offset).all()
    return {
        "questions": questions,
        "total_questions": count,
        "categories": categories,
        "current_category": current_category,
    }


"""

@TODO: 
Create an endpoint to DELETE question using a question ID. 
TEST: When you click the trash icon next to a question, the question will be removed.
This removal will persist in the database and when you refresh the page. 
"""

"""
@TODO: 
Create an endpoint to POST a new question, 
which will require the question and answer text, 
category, and difficulty score.
TEST: When you submit a question on the "Add" tab, 
the form will clear and the question will appear at the end of the last page
of the questions list in the "List" tab.  
"""

"""
@TODO: 
Create a POST endpoint to get questions based on a search term. 
It should return any questions for whom the search term 
is a substring of the question. 
TEST: Search by any phrase. The questions list will update to include 
only question that include that string within their question. 
Try using the word "title" to start. 
"""

"""
@TODO: 
Create a GET endpoint to get questions based on category. 
TEST: In the "List" tab / main screen, clicking on one of the 
categories in the left column will cause only questions of that 
category to be shown. 
"""

"""
@TODO: 
Create a POST endpoint to get questions to play the quiz. 
This endpoint should take category and previous question parameters 
and return a random questions within the given category, 
if provided, and that is not one of the previous questions. 
TEST: In the "Play" tab, after a user selects "All" or a category,
one question at a time is displayed, the user is allowed to answer
and shown whether they were correct or not. 
"""

"""
@TODO: 
Create error handlers for all expected errors 
including 404 and 422. 
"""