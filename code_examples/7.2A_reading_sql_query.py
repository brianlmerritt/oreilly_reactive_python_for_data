from sqlalchemy import create_engine, text
from rx import from_, operators as ops

engine = create_engine('sqlite:///../resources/rexon_metals.db')
conn = engine.connect()


def get_all_customers():
    stmt = text("SELECT * FROM CUSTOMER")
    return from_(conn.execute(stmt))


get_all_customers().pipe(
    ops.map(lambda r: r[1])
).subscribe(lambda r: print(r))
