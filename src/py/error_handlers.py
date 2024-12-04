from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({'error': 'Bad request'}), 400

    @app.errorhandler(Exception)
    def handle_generic_error(e):
        return jsonify({'error': f'An unexpected internal server error occurred: {str(e)}'}), 500
