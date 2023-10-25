import random
from app.dbworker import *


DataBase.init_db()
for _ in range(0, 10):
    title = "".join(i for i in random.choices('abzcmyeirpotpotpqlakjfhmzs', k=10))
    content = "".join(i for i in random.choices('abzcmyeirpotpotpqlakjfhmzs', k=100))
    DataBase.test_db(title=title, content=content)

