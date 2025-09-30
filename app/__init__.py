from flask import Flask

# This Function will create an instance for our Flask Application and return it
def create_app():
    '''
    Application factory function.
    This function creates and configures the Flask application instance.
    '''
    app =  Flask(__name__)

    return app

