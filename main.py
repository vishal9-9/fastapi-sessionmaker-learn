from database.engine import Session, get_db
from models.roles import Roles

# for directly using sessionmaker

db = Session()

data = {'id': 1, 'roles': 'admin'}
data = Roles(**data)
db.add(data)
db.commit()
db.close()

# for using yield funtion(get-db())

other_db = get_db()
new_sess = other_db.__next__()

data = {'id': 2, 'roles': 'admin'}
data = Roles(**data)
new_sess.add(data)
new_sess.commit()
