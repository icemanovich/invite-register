from app import app
from flask import render_template, flash, Response, request, redirect, url_for

import logging
import traceback


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html',)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(Exception)
def exception(e):
    if request.is_xhr or request.json:
        logging.error(traceback.format_exc())
        return Response(str(e), 500)

    flash(str(e))
    logging.error(traceback.format_exc())
    return redirect(request.args.get('next') or request.referrer or url_for('main'), code=303)
