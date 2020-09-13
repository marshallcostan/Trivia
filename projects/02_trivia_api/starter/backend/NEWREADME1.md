# Trivia API Backend

This API provides endpoints for a trivia game whose front end was created by developers at Udacity. Its been said that when it came to creating an API for their game they needed help so they enlisted myself who has absolutely no experience doing so, fingers crossed. With that said
I do hope you find the experience of setting up this app and working with it intuitive.

All backend code follows PEP8 style guidelines, thanks developers!

## Getting Started

### Installing Dependencies

For developers working on this project Python3, pip, PostgreSQL, and Node should be installed on their local machines.

#### Python 3

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

It is recommended to work within a virtual environment when using Python for projects. 

#### Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

*Verify the current version of Werkzeug is installed to avoid errors.*

## Database Setup

Start the Postgres server, create a database named "trivia" and tables will be created and populated using the trivia.psql file provided. From the backend folder in terminal run:

```bash
psql trivia < trivia.psql
```

## Running the server

To run the server, from within the `backend` directory execute the following commands:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

These commands direct the app to use the __init__.py file in the flaskr folder as well as setting the app  development mode. In development mode the server will automatically
restart if any changes are made to the code.

The default URL the app runs on is: http://127.0.0.1:5000/

## Frontend

Assuming the installation of Node, from the `frontend` folder run the following commands to install dependencies and start the client:

Dependencies:

```bash
npm install
``` 
Start the client:

```bash
npm start
```

The default URL the frontend runs on is: http://127.0.0.1:3000


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
*The first time these tests are run omit the dropdb command.*


# API Reference 

Base URL: When run locally the backend by default is hosted at http://127.0.0.1:5000/ which is set as a proxy in the front end configuration.

Authentication: This version of the application does not require authentication or API keys.


## Error Handling

Errors are returned as JSON objects using the following format:
```bash
{
"success": False,
"error": 422,
"message": "unprocessable"
}
```

This API will return these error types when requests fail:

- 400: Bad Request
- 404: Resource not found
- 405: Method not allowed
- 422: Unprocessable
- 500: Internal server error


## Endpoints

### GET /categories

   General:
        
   - Returns a dictionary of all categories as ID, Type key:value pairs and a success value.
        
   Sample:  
         
    curl http://127.0.0.1:5000/categories
```bash 
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
```


### GET /questions

   General:
      
   - Returns success value, questions(a list of question ojects), total questions, categories, and current category. All questions are returned from the database.

   - Results are paginated in groups of 10.
    
   Sample:  
     
    curl http://127.0.0.1:5000/questions
```bash    
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "success": true, 
  "totalQuestions": 49
}
```

### DELETE /questions/{question_id}
   General:
    
   - Deletes a question with the ID supplied to the endpoint.
        
   - Returns a success value, the ID of the deleted question, success message.
        
   Sample:  
   
    curl -X DELETE http://127.0.0.1:5000/questions/15

```bash
{
  "deleted": 15, 
  "message": "Successfully deleted", 
  "success": true
}
```    

### POST /questions

   General:
    
   - Creates a new question using the submitted question, answer, difficulty and category(ID) values.
        
   - Returns a success value.
        
   Sample:  
   
    curl -X POST -H "Content-Type: application/json" -d '{"question":"Whats up?", "answer":"Not much", "difficulty":"1" , "category":"2"}' http://127.0.0.1:5000/questions
```bash
{
  "success": true
}
```
Updated questions:

```bash
$ curl http://127.0.0.1:5000/questions?page=2
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Scarab", 
      "category": 4, 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }, 
    {
      "answer": "Not much", 
      "category": 2, 
      "difficulty": 1, 
      "id": 24, 
      "question": "Whats up?"
    }
  ], 
  "success": true, 
  "totalQuestions": 20
```

### POST /searchQuestions

General:
    
   - Returns questions matching search criteria as a success value, list of questions, number of question list and current category.
        
   
   Sample:
 
    curl -X POST -H "Content-Type: application/json" -d '{"searchTerm": "Clay"}'  http://127.0.0.1:5000/searchQuestions
```bash
{
  "current_category": null, 
  "questions": [
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }
  ], 
  "success": true, 
  "total_questions": 1
}
```

### GET /categories/category_id/questions

General

   - Returns a success value, a list of questions sorted by the given category, total questions, and current category .
        
   
   Sample:
 
    curl http://127.0.0.1:5000/categories/2/questions


```bash
{
  "current_category": null, 
  "questions": [
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "Not much", 
      "category": 2, 
      "difficulty": 1, 
      "id": 24, 
      "question": "Whats up?"
    }
  ], 
  "total_questions": 5
}
```

### POST /quizzes
General:
        
   - Returns a success value, a random question from all the possible questions or from the chosen category if one was supplied, a list of the previous questions if any. 
    Sample: 
       
    curl -X POST -H "Content-Type: application/json" -d '{"previous_questions": [2],"quiz_category": {"id": "5"}}' http://127.0.0.1:5000/quizzes
```bash
{
  "previousQuestions": [
    2
  ], 
  "question": {
    "answer": "Edward Scissorhands", 
    "category": 5, 
    "difficulty": 3, 
    "id": 6, 
    "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
  }, 
  "success": true
}

