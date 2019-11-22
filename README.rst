Message Board Instructions
==========================

1. Install Flask and extensions

   .. code-block:: bash

      $ pip install flask
      $ pip install flask-socketio
      $ pip install flask-sqlalchemy

2. Create database by importing database object from an interactive Python Shell

   .. code-block:: python

      >>> from main.py import db
      >>> db.create_all()

3. Run the application using command:

   .. code-block:: bash

      $ python main.py

4. Open up your web browser of choice and go the URL: http://127.0.0.1:5000/
