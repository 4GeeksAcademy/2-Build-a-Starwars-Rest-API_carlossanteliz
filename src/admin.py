# import os
# from flask_admin import Admin
# from models import db, User, People, Planet, FavoritePeople, FavoritePlanet
# from flask_admin.contrib.sqla import ModelView

# def setup_admin(app):
#     app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
#     app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
#     admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

#     admin.add_view(ModelView(User, db.session))
#     admin.add_view(ModelView(People, db.session))
#     admin.add_view(ModelView(Planet, db.session))
#     admin.add_view(ModelView(FavoritePeople, db.session))
#     admin.add_view(ModelView(FavoritePlanet, db.session))

import os
from flask_admin import Admin
from models import db, User, People, Planet, FavoritePeople, FavoritePlanet
from flask_admin.contrib.sqla import ModelView

class FavoritePlanetAdmin(ModelView):
    column_list = ('id', 'user_id', 'planet_id', 'planet', 'user')
    column_labels = {
        "user_id": "User ID",
        "planet_id": "Planet ID",
        "planet": "Planet",
        "user": "User"
    }

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(People, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(FavoritePeople, db.session))

    admin.add_view(FavoritePlanetAdmin(FavoritePlanet, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))