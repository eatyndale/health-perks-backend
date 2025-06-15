from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

def test_database_connection():
    try:
        # Use the provided database URL
        database_url = "postgresql://postgres:PVjOqRRfoQgQjjXlIMESPYPpfdwLxpGQ@shortline.proxy.rlwy.net:55331/railway"
        
        # Create engine
        engine = create_engine(database_url)
        
        # Test connection
        with engine.connect() as connection:
            # Try to execute a simple query
            result = connection.execute(text("SELECT 1"))
            print("✅ Database connection successful!")
            
            # Print database information
            db_info = connection.execute(text("SELECT version()")).fetchone()
            print(f"Database version: {db_info[0]}")
            
            return True
            
    except SQLAlchemyError as e:
        print(f"❌ Database connection failed: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing database connection...")
    test_database_connection() 