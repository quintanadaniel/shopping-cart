from http import HTTPStatus

from application import create_app, page_not_found

app = create_app()

if __name__ == "__main__":
    app.register_error_handler(HTTPStatus.NOT_FOUND, page_not_found)
    app.run(debug=True, host="0.0.0.0")
