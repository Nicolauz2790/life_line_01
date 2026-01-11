import sqlite3

conn = sqlite3.connect('life_ledger.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [row[0] for row in cursor.fetchall()]
print("Tables in database:")
for table in tables:
    print(f"  - {table}")

# Check for digital life tables
digital_tables = ['digital_subscriptions', 'digital_accounts', 'digital_assets']
print("\nDigital Life tables:")
for table in digital_tables:
    if table in tables:
        print(f"  ✓ {table} exists")
    else:
        print(f"  ✗ {table} MISSING")

conn.close()
