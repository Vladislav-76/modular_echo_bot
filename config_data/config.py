from environs import Env


env = Env()
env.read_env()

database: str = env('DATABASE')
db_host: str = env('DB_HOST')
db_user: str = env('DB_USER')
db_password: str = env('DB_PASSWORD')

token: str = env('BOT_TOKEN')
admin_ids: list[int] = list(map(int, env.list('ADMIN_IDS')))
