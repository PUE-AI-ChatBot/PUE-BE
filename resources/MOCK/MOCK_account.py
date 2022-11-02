from models import UserModel

def make_account():
    user = UserModel(
        user_name="well87865@gmail.com",
        user_subname="Chanee",
        password="123123",
        make_date="20221020"
    )
    user.num_of_userchats = 5
    user.num_of_counselling = 1
    user.save_to_db()

    return user