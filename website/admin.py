from flask import Blueprint, render_template
from flask_login import login_required, current_user
from forms import ShopItemForm

admin = Blueprint('admin', __name__)

@admin.route('/add-shop-items', methods=['GET','POST'])
@login_required
def add_shop_items():
    if current_user.id == 1:
        form = ShopItemForm

    return render_template('404.html')