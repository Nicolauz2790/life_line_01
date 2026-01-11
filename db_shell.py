import sqlite3
import sys

def run_shell():
    db_path = 'life_ledger.db'
    print(f"Connecting to {db_path}...")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        print("Connected! Enter your SQL queries below completely. Type 'exit' to quit.")
        print("Example: SELECT * FROM transactions LIMIT 5;")
        
        while True:
            query = input("SQL> ")
            if query.lower() in ('exit', 'quit'):
                break
            
            try:
                cursor.execute(query)
                if query.strip().upper().startswith("SELECT"):
                    results = cursor.fetchall()
                    if not results:
                        print("No results found.")
                    else:
                        # Print headers
                        headers = [description[0] for description in cursor.description]
                        print(" | ".join(headers))
                        print("-" * (len(headers) * 10))
                        for row in results:
                            print(row)
                else:
                    conn.commit()
                    print(f"Query executed. Rows affected: {cursor.rowcount}")
            except sqlite3.Error as e:
                print(f"Error: {e}")
                
    except Exception as e:
        print(f"Failed to connect: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    run_shell()
