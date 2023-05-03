from app import db
from app.models.book import Book
from flask import Blueprint,jsonify, make_response,request, abort

#CREATE BP/ENDPOINT
books_bp = Blueprint("books_bp",__name__, url_prefix="/books")

#HELPER FUNCTION
def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message":f"book {book_id} invalid"},400))
    
    book = Book.query.get(book_id)

    if not book:
        abort(make_response({"message":f"book {book_id} not found"},404))
    
    return book


#ROUTE FUNCTIONS
#CREATE ONE BOOK
@books_bp.route("",methods =["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book(
    title=request_body["title"],
    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Book {new_book.title} successfully created",201))

#RETURN ONE BOOK





#RETURNS ALL THE BOOKS
@books_bp.route("",methods=["GET"])
def read_all_books():
    books = Book.query.all() #query the db/get all the books/put in local var 
    books_list = []
    
    for book in books:
        books_list.append(dict(
            id = book.id,
            title = book.title,
            description = book.description
        ))

    return jsonify(books_list)

#RETURNS REQUESTED BOOK
@books_bp.route("/<book_id>",methods=["GET"])
def read_one_book(book_id):
    book = validate_book(book_id)
    return {
        "id": book.id,
        "title": book.title,
        "description": book.description
    }

#UPDATE ONE BOOK: has a request body
@books_bp.route("/<book_id>",methods=["PUT"])
def update_book(book_id):
    book = validate_book(book_id)
    
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(jsonify(f"Book #{book_id} successfully updated"))

#DELETE RECORD
@books_bp.route("/<book_id>",methods=["DELETE"])
def delete_book(book_id):
    book = validate_book(book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(jsonify(f"Book #{book_id} successfully deleted"))

