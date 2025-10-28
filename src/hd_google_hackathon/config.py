import os

# Default model used by agents
DEFAULT_MODEL = "gemini-2.5-flash"

# Path to the mock database file on the filesystem. The container will place
# the file at /data/mock.db by default. You can override this with the
# DATABASE_PATH environment variable.
DATABASE_PATH = os.getenv("DATABASE_PATH", "/data/mock.db")


def get_database_path() -> str:
	"""Return the filesystem path to the mock database.

	This helper centralizes where code should read the DB path from so it's
	easy to swap to a different location (or Cloud SQL) later.
	"""
	return os.getenv("DATABASE_PATH", DATABASE_PATH)