from flask import Blueprint, jsonify, abort, make_response


#HELPER FUNCTION
def validate_book(cls,book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message":f"book {book_id} invalid"},400))
    
    book = cls.query.get(book_id)

    if not book:
        abort(make_response({"message":f"book {book_id} not found"},404))
    
    return book