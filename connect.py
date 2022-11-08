from pymodm import connect, MongoModel, fields
def init_mongo_db():
    #connect("mongodb+srv://m4c11in:Myrevi20@bme547.yr5kjvq.mongodb.net/?retryWrites=true&w=majority")
    #connect("mongodb+srv://m4c11in:Myrevi20@bme547.yr5kjvq.mongodb.net/test?retryWrites=true")
    connect("mongodb+srv://m4c11in:Myrevi20@bme547-nlfrn.mongodb.net/adalberto?retryWrites=true&w=majority")


class User(MongoModel):
    email = fields.EmailField(primary_key=True)
    first_name = fields.CharField()
    last_name = fields.CharField()
    age = fields.IntegerField()


def add_new_user(email_arg, first_name_arg, last_name_arg, age_arg):
    u = User(email=email_arg,
             first_name=first_name_arg,
             last_name=last_name_arg,
             age=age_arg)
    u.save()
    print("Saved to database")


def get_users():
    for user in User.objects.raw({}):
        print(user.email)
    return


if __name__ == '__main__':
    init_mongo_db()
    add_new_user("awaxye@yahoo.com", "Adam", "Wax", 30)
    add_new_user("david.a.ward@duke.edu", "David", "Ward", "45")
    get_users()