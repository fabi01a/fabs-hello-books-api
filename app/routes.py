from flask import Blueprint,jsonify #need to import in order to make endpoints

class Book:
    def __init__(self,id,title,description):
        self.id = id
        self.title = title
        self.description = description

#Create a list of Book instances.
books = [
    Book(1,"Are You There God It's Me, Margaret","Fiction"),
    Book(2,"Neuromancer","Sci-Fi Fantasy"),
    Book(3,"The Tipping Point","Non-Fiction"),
    Book(4,"You Are What You Eat","Self-Help")
]

#Create endpoints: Blueprints 
bp = Blueprint("books",__name__, url_prefix="/books")

#endpoint that returns all books
@bp.route("",methods=["GET"])
def handle_books():
    books_list = []
    
    for book in books:
        books_list.append(dict(
            id = book.id,
            title = book.title,
            description = book.description
        ))

    return jsonify(books_list)


@bp.route("/<book_id>",methods=["GET"]) #this returns the req book
def handle_book(book_id):
    # book_id = int(book_id)
    try:
        book_id = int(book_id)
    except:
        return {"message":f"book {book_id} invalid"},400
    
    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
    return {"message":f"book {book_id} not found"},404
   #create API that returns a 404 for a non-existing book. 