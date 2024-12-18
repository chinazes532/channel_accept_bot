import aiosqlite as sq

from config import DB_NAME


async def create_db():
    async with sq.connect(DB_NAME) as db:
        print("Database created!")

        await db.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT
        )""")

        await db.commit()


async def insert_user(user_id, username):
    async with sq.connect(DB_NAME) as db:
        await db.execute("INSERT OR REPLACE INTO users VALUES (?, ?)", (user_id, username))
        await db.commit()

