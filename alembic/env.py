import os
import sys
from logging.config import fileConfig
 
from sqlalchemy import engine_from_config
from sqlalchemy import pool
 
from alembic import context
 
# Add the app directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
 
# This is the Alembic Config object
config = context.config
 
# Interpret the config file for Python logging
fileConfig(config.config_file_name)
 
# Import all models (THIS IS IMPORTANT for autogenerate)
from app.models import Base
from app.database import DATABASE_URL
 
# Override the sqlalchemy.url in alembic.ini with our database URL
config.set_main_option("sqlalchemy.url", DATABASE_URL)
 
# Set target metadata
target_metadata = Base.metadata
 
# Other values, defined by env.py's initial template
def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
 
    with context.begin_transaction():
        context.run_migrations()
 
 
def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
 
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
 
        with context.begin_transaction():
            context.run_migrations()
 
 
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
 