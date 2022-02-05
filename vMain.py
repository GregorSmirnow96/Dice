from cGameContext import game_context_blueprint
from cShop import shop_blueprint


app = Flask(__name__)

app.register_blueprint(game_context_blueprint)
app.register_blueprint(shop_blueprint)

app.run()
