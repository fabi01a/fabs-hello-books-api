from app import db
from app.models.book import Book
from flask import Blueprint,jsonify, make_response,request, abort
from routes.routes_helpers import validate_book

#CREATE BP/ENDPOINT
books_bp = Blueprint("books_bp",__name__, url_prefix="/books")

#ROUTE FUNCTIONS
#CREATE ONE BOOK
@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book.from_dict(request_body)

    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Book {new_book.title} successfully created"), 201)

#RETURN ONE BOOK
def read_one_book(book_id):
    book = validate_book(book_id)
    return book.to_dict()

#RETURNS ALL THE BOOKS
@books_bp.route("",methods=["GET"])
def read_all_books():
    # books = Book.query.all() #query the db/get all the books/put in local var 
    title_query = request.args.get("title")
    if title_query:
        books = Book.query.filter_by(title=title_query)
    else:
        books = Book.query.all()
    
    books_response = []
    for book in books:
        books_response.append(books.to_dict())
    return jsonify(books_response)

# #RETURNS REQUESTED BOOK
@books_bp.route("/<book_id>",methods=["GET"])
def read_one_book(book_id):
    book = validate_book(book_id)
    return book.to_dict()

#UPDATE ONE BOOK: has a request body
@books_bp.route("/<book_id>",methods=["PUT"])
def update_book(book_id):
    book = validate_book(Book,book_id)
    
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(jsonify(f"Book #{book_id} successfully updated"))

#DELETE RECORD
@books_bp.route("/<book_id>",methods=["DELETE"])
def delete_book(book_id):
    book = validate_book(Book,book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(jsonify(f"Book #{book_id} successfully deleted"))

