import os
from dotenv import load_dotenv

load_dotenv()

User_role = {"Patron": 0, "Admin": 1, "Global_Admin": 2}
map_api = f"https://api.locationiq.com/v1/autocomplete?key={os.getenv("MAP_API_KEY")}&q="
book_api1 = "https://openlibrary.org/search.json?title="
book_api2 = "https://www.googleapis.com/books/v1/volumes?q="

db_host = os.getenv("DB_HOST", "localhost")
db_user = os.getenv("DB_USER", "root")
db_password = os.getenv("DB_PASSWORD", "")
db_name = os.getenv("DB_NAME", "ShelfSyncV2")
db_port = int(os.getenv("DB_PORT", 3306))
