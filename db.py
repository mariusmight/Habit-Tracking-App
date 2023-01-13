import os
from sqlite3 import dbapi2 as sqlite3

DATABASE = "db.sqlite3"


def connect_db():
    """Connects to the specific database."""
    return sqlite3.connect(DATABASE)


def init_db():
    """Initializes the database."""
    # create the database
    if not os.path.exists(DATABASE):
        # create the file
        open(DATABASE, "w").close()

    db = connect_db()
    # check if table exists
    cur = db.execute(
        'select name from sqlite_master where type="table" and name="habits"'
    )
    if cur.fetchone() is None:
        schema = """
        create table main.habits
        (
            name          text    not null,
            specification text    not null,
            periodicity   integer not null,
            history       text    not null,
            date_created  text    not null
        );
        """
        db.cursor().executescript(schema)
    db.commit()
    db.close()


def save_habit(habit):
    """Saves a habit to the database."""
    db = connect_db()
    db.execute(
        "insert into habits (name, specification, periodicity, history, date_created) values (?, ?, ?, ?, ?)",
        habit.to_sql(),
    )
    db.commit()
    db.close()


def update_habit(habit):
    """Updates a habit in the database."""
    db = connect_db()
    db.execute(
        "update habits set history = ? where name = ?",
        (
            ",".join([h.strftime("%Y-%m-%d %H:%M:%S") for h in habit.history]),
            habit.name,
        ),
    )
    db.commit()
    db.close()


def get_habits():
    """Returns all habits from the database."""
    db = connect_db()
    cur = db.execute("select * from habits order by name asc")
    habits = cur.fetchall()
    db.close()
    return habits
