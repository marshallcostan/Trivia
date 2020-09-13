from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    current_questions = questions[start:end]
    return current_questions

#  CREATE APP
#  ----------------------------------------------------------------


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={'/': {'origins': "*"}})

    @app.after_request  # adds headers to response
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    #  CATEGORY AND QUESTION ENDPOINTS
    #  ----------------------------------------------------------------
    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories = Category.query.order_by(Category.id).all()
        data = {}
        try:
            for c in categories:
                data[c.id] = c.type

            return jsonify({
              'categories': data,
              'success': True
            })
        except():
            abort(404)

    @app.route('/questions', methods=['GET'])
    def get_questions():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)

        if len(current_questions) == 0:
            abort(404)

        categories = Category.query.all()
        category_list = {}
        try:
            for c in categories:
                category_list[c.id] = c.type
            return jsonify({
              'success': True,
              'questions': current_questions,
              'totalQuestions': len(Question.query.all()),
              'categories': category_list,
              'current_category': None
            })
        except():
            abort(404)

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.get(question_id)

            if question is None:
                abort(400)

            question.delete()
            return jsonify({
                'success': True,
                'deleted': question.id,
                'message': 'Successfully deleted'})

        except():
            abort(422)

    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()
        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        difficulty = body.get('difficulty', None)
        category = body.get('category', None)
        try:
            new_question = Question(question=new_question, answer=new_answer, difficulty=difficulty, category=category)
            new_question.insert()

            return jsonify({
                'success': True,
            })

        except():
            abort(422)

    @app.route('/searchQuestions', methods=['POST'])
    def search_question():
        try:
            # define search term
            body = request.get_json()
            search_term = body.get('searchTerm', '')
            result = Question.query.filter(Question.question.ilike('%{}%'.format(search_term))).all()
            formatted_questions = [question.format() for question in result]
            return jsonify({
                'success': True,
                'questions': formatted_questions,
                'total_questions': len(result),
                'current_category': None
            })
        except():
            abort(422)

    @app.route('/categories/<int:category_id>/questions')
    def sort_by_categories(category_id):
        try:
            sorted_questions = Question.query.filter(Question.category == category_id).all()
            formatted_sorted_questions = [question.format() for question in sorted_questions]
            return jsonify({
                'success': True,
                'questions': formatted_sorted_questions,
                'total_questions': len(sorted_questions),
                'current_category': None
            })

        except():
            abort(422)

    #  START QUIZ
    #  ----------------------------------------------------------------
    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        try:
            body = request.get_json()
            previous_questions = body.get('previous_questions', None)
            quiz_category = body.get('quiz_category', None)
            print(quiz_category)
            category_id = quiz_category['id']
            print(category_id)

            if category_id == 0:
                questions = Question.query.all()
            else:
                questions = Question.query.filter(Question.category == category_id).all()

            sorted_questions = []
            for question in questions:
                if question.id not in previous_questions:
                    sorted_questions.append(question.format())

            question = random.choice(sorted_questions)

            return jsonify({
                'success': True,
                'question': question,
                'previousQuestions': previous_questions
            })
        except():
            abort(422)

    #  ERROR HANDLING
    #  ----------------------------------------------------------------
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
              "success": False,
              "error": 404,
              "message": "resource not found"
          }), 404

    @app.errorhandler(405)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
              "success": False,
              "error": 422,
              "message": "unprocessable"
          }), 422

    @app.errorhandler(500)
    def bad_request(error):
        return jsonify({
              "success": False,
              "error": 500,
              "message": "internal server error"
          }), 500

    return app

