"""
Comprehensive Dummy Data Population Script for Life Ledger
This script populates ALL modules with realistic sample data for testing and demonstration.
"""

from database.manager import DatabaseManager
from models.transaction import TransactionModel
from models.inventory import InventoryModel
from models.person import PersonModel
from models.finance import AssetModel, LoanModel, SavingsModel, InsuranceModel
from models.automation import AutomationModel
from models.event import EventModel
from models.goal import GoalModel
from models.health import HealthModel
from models.fitness import FitnessModel
from models.digital_life import DigitalSubscriptionModel, DigitalAccountModel, DigitalAssetModel
from datetime import datetime, timedelta
import random

def clear_all_data(db):
    """Clear existing data (optional - comment out if you want to keep existing data)"""
    print("Clearing existing data...")
    tables = [
        'transactions', 'inventory', 'contacts', 'debts', 'financial_assets',
        'loans', 'insurance', 'savings_goals', 'recurring_transactions', 'budgets',
        'events', 'event_tasks', 'goals', 'goal_logs', 'health_metrics', 
        'medications', 'fitness_logs', 'body_metrics',
        'digital_subscriptions', 'digital_accounts', 'digital_assets'
    ]
    for table in tables:
        try:
            db.execute_query(f"DELETE FROM {table}")
        except:
            pass
    print("  [OK] Data cleared\n")

def populate_finances(db):
    """Populate financial data: transactions, assets, loans, insurance, savings"""
    print("Populating Financial Data...")
    
    trans_model = TransactionModel(db)
    asset_model = AssetModel(db)
    loan_model = LoanModel(db)
    savings_model = SavingsModel(db)
    insurance_model = InsuranceModel(db)
    auto_model = AutomationModel(db)
    
    # Transactions (last 90 days)
    income_sources = [
        ("Salary", 5500, "Salary"),
        ("Freelance Project", 1200, "Freelance"),
        ("Investment Dividend", 350, "Investment"),
        ("Side Business", 800, "Business")
    ]
    
    expense_categories = [
        ("Rent", 1500, "Housing"),
        ("Groceries", 450, "Food"),
        ("Utilities", 180, "Utilities"),
        ("Internet & Phone", 120, "Utilities"),
        ("Transportation", 200, "Transport"),
        ("Dining Out", 280, "Food"),
        ("Entertainment", 150, "Entertainment"),
        ("Gym Membership", 60, "Health"),
        ("Shopping", 320, "Shopping"),
        ("Insurance Premium", 250, "Insurance"),
        ("Gas", 180, "Transport"),
        ("Coffee", 85, "Food"),
        ("Books", 45, "Education"),
        ("Healthcare", 120, "Health")
    ]
    
    today = datetime.now()
    
    # Add income (monthly)
    for month in range(3):
        for desc, amount, category in income_sources:
            date = (today - timedelta(days=30*month + random.randint(1, 5))).strftime('%Y-%m-%d')
            trans_model.add_transaction(date, amount, category, 'INCOME', desc)
    
    # Add expenses (spread over 90 days)
    for day in range(90):
        date = (today - timedelta(days=day)).strftime('%Y-%m-%d')
        # Random 2-4 expenses per day
        num_expenses = random.randint(2, 4)
        for _ in range(num_expenses):
            desc, base_amount, category = random.choice(expense_categories)
            amount = base_amount * random.uniform(0.7, 1.3)
            trans_model.add_transaction(date, amount, category, 'EXPENSE', desc)
    
    print("  [OK] Added transactions")
    
    # Financial Assets
    assets = [
        ("Savings Account - Chase", "Savings Account", 15000, "Chase Bank"),
        ("Checking Account - BofA", "Checking Account", 3500, "Bank of America"),
        ("Investment Portfolio", "Stocks", 45000, "Vanguard"),
        ("401(k) Retirement", "Retirement Account", 85000, "Fidelity"),
        ("Emergency Fund", "Savings Account", 12000, "Ally Bank"),
        ("Crypto Holdings", "Cryptocurrency", 8500, "Coinbase")
    ]
    
    for name, asset_type, value, institution in assets:
        asset_model.add_asset(name, asset_type, value, institution, "")
    
    print("  [OK] Added financial assets")
    
    # Loans
    loans = [
        ("Student Loan", "Education Loan", 25000, 18500, 4.5, "2028-06-15", "Sallie Mae"),
        ("Car Loan", "Auto Loan", 30000, 12000, 3.9, "2026-12-01", "Toyota Financial"),
        ("Personal Loan", "Personal Loan", 5000, 2800, 7.2, "2025-08-20", "Marcus")
    ]
    
    for name, loan_type, principal, balance, rate, due_date, institution in loans:
        loan_model.add_loan(name, loan_type, principal, balance, rate, due_date, institution)
    
    print("  [OK] Added loans")
    
    # Insurance
    insurance_policies = [
        ("Health Insurance", "Health", 450, "Monthly", 50000, "2026-12-31", "BCBS-12345"),
        ("Auto Insurance", "Auto", 180, "Monthly", 100000, "2026-06-30", "GEICO-67890"),
        ("Life Insurance", "Life", 85, "Monthly", 500000, "2045-01-15", "State Farm-11223"),
        ("Renters Insurance", "Property", 25, "Monthly", 50000, "2026-11-01", "Lemonade-44556")
    ]
    
    for name, ins_type, premium, frequency, coverage, renewal, policy_num in insurance_policies:
        insurance_model.add_insurance(name, ins_type, premium, frequency, coverage, renewal, policy_num)
    
    print("  [OK] Added insurance policies")
    
    # Savings Goals
    savings_goals = [
        ("Emergency Fund", 20000, 12000, "2026-12-31"),
        ("Vacation to Japan", 5000, 2800, "2026-08-01"),
        ("New Laptop", 2000, 1500, "2026-04-15"),
        ("House Down Payment", 50000, 15000, "2028-06-01")
    ]
    
    for name, target, current, deadline in savings_goals:
        savings_model.add_goal(name, target, current, deadline, "")
    
    print("  [OK] Added savings goals")
    
    # Budgets
    budgets = [
        ("Food", 600),
        ("Housing", 1500),
        ("Transport", 400),
        ("Entertainment", 200),
        ("Shopping", 300),
        ("Health", 250),
        ("Utilities", 200)
    ]
    
    for category, limit in budgets:
        auto_model.set_budget(category, limit)
    
    print("  [OK] Added budgets")
    
    # Recurring Transactions
    recurring = [
        ("Netflix Subscription", 15.99, "Entertainment", "EXPENSE", "Monthly", "2024-01-01"),
        ("Spotify Premium", 10.99, "Entertainment", "EXPENSE", "Monthly", "2024-02-15"),
        ("Gym Membership", 60, "Health", "EXPENSE", "Monthly", "2024-03-01"),
        ("Salary", 5500, "Salary", "INCOME", "Monthly", "2024-01-01")
    ]
    
    for name, amount, category, trans_type, frequency, start_date in recurring:
        # Model now supports type and start_date
        auto_model.add_recurring(name, amount, category, trans_type, frequency, start_date)
    
    print("  [OK] Added recurring transactions\n")

def populate_inventory(db):
    """Populate inventory/possessions"""
    print("Populating Inventory...")
    
    inv_model = InventoryModel(db)
    
    items = [
        ("MacBook Pro 16\"", 2800, 2400, "2023-06-15", "Electronics"),
        ("iPhone 15 Pro", 1200, 1000, "2023-09-20", "Electronics"),
        ("Sony WH-1000XM5", 400, 350, "2023-08-10", "Electronics"),
        ("Gaming PC", 2200, 1900, "2022-11-05", "Electronics"),
        ("LG OLED TV 65\"", 1800, 1500, "2023-01-20", "Electronics"),
        ("Herman Miller Chair", 1400, 1300, "2023-03-15", "Furniture"),
        ("Standing Desk", 800, 750, "2023-03-15", "Furniture"),
        ("Couch - Living Room", 2000, 1800, "2022-08-10", "Furniture"),
        ("Dining Table Set", 1200, 1100, "2022-08-10", "Furniture"),
        ("Mountain Bike", 1500, 1200, "2023-04-20", "Sports"),
        ("Camera - Canon EOS R6", 2500, 2200, "2023-07-01", "Electronics"),
        ("Watch - Apple Watch", 450, 380, "2023-09-20", "Electronics"),
        ("Bookshelf Collection", 800, 700, "2022-12-01", "Furniture"),
        ("Coffee Machine", 600, 550, "2023-05-10", "Appliances"),
        ("Air Purifier", 300, 280, "2023-06-01", "Appliances")
    ]
    
    for name, purchase_price, current_value, purchase_date, category in items:
        inv_model.add_item(name, purchase_price, current_value, purchase_date, category)
    
    print("  [OK] Added inventory items\n")

def populate_people(db):
    """Populate contacts and debts"""
    print("Populating People & Relationships...")
    
    person_model = PersonModel(db)
    
    contacts = [
        ("Alice Johnson", "alice.j@email.com", "+1-555-0101", "1990-05-15", "Friend"),
        ("Bob Smith", "bob.smith@email.com", "+1-555-0102", "1988-08-22", "Friend"),
        ("Carol Williams", "carol.w@email.com", "+1-555-0103", "1992-03-10", "Family"),
        ("David Brown", "david.b@email.com", "+1-555-0104", "1985-11-30", "Colleague"),
        ("Emma Davis", "emma.d@email.com", "+1-555-0105", "1995-07-18", "Friend"),
        ("Frank Miller", "frank.m@email.com", "+1-555-0106", "1987-12-05", "Business"),
        ("Grace Lee", "grace.lee@email.com", "+1-555-0107", "1993-09-25", "Friend"),
        ("Henry Wilson", "henry.w@email.com", "+1-555-0108", "1991-04-12", "Family")
    ]
    
    for name, email, phone, birthday, category in contacts:
        last_contacted = (datetime.now() - timedelta(days=random.randint(1, 60))).strftime('%Y-%m-%d')
        person_model.add_contact(name, email, phone, birthday, last_contacted, f"Notes about {name}")
    
    print("  [OK] Added contacts")
    
    # Get contact IDs for debts
    all_contacts = person_model.get_contacts()
    
    # Add some debts
    debts = [
        (all_contacts[0]['id'], 50, "OWED_TO_ME", "Lunch money", "2026-02-15", False),
        (all_contacts[1]['id'], 200, "I_OWE", "Concert tickets", "2026-01-20", False),
        (all_contacts[4]['id'], 150, "OWED_TO_ME", "Shared Airbnb", "2026-03-01", False),
        (all_contacts[5]['id'], 500, "I_OWE", "Business loan", "2026-06-30", False)
    ]
    
    for contact_id, amount, debt_type, description, due_date, settled in debts:
        person_model.add_debt(contact_id, amount, debt_type, description, due_date, settled)
    
    print("  [OK] Added debts\n")

def populate_health(db):
    """Populate health metrics and medications"""
    print("Populating Health Data...")
    
    health_model = HealthModel(db)
    
    # Health metrics over last 60 days
    today = datetime.now()
    
    for day in range(60):
        date = (today - timedelta(days=day)).strftime('%Y-%m-%d')
        
        # Blood Pressure (every 3 days)
        if day % 3 == 0:
            systolic = random.randint(115, 125)
            diastolic = random.randint(75, 85)
            health_model.add_metric("Blood Pressure", f"{systolic}/{diastolic}", "mmHg", date)
        
        # Heart Rate (every 2 days)
        if day % 2 == 0:
            hr = random.randint(65, 75)
            health_model.add_metric("Heart Rate", hr, "bpm", date)
        
        # Weight (weekly)
        if day % 7 == 0:
            weight = 75 + random.uniform(-2, 2)
            health_model.add_metric("Weight", round(weight, 1), "kg", date)
        
        # Blood Sugar (every 5 days)
        if day % 5 == 0:
            glucose = random.randint(85, 105)
            health_model.add_metric("Blood Sugar", glucose, "mg/dL", date)
    
    print("  [OK] Added health metrics")
    
    # Medications
    medications = [
        ("Vitamin D3", "2000 IU", "Daily", "2024-01-01"),
        ("Omega-3 Fish Oil", "1000mg", "Daily", "2024-01-01"),
        ("Multivitamin", "1 tablet", "Daily", "2024-02-01"),
        ("Allergy Medicine", "10mg", "As needed", "2024-03-15")
    ]
    
    for name, dosage, frequency, start_date in medications:
        health_model.add_medication(name, dosage, frequency, start_date, f"Taking {name}")
    
    print("  [OK] Added medications\n")

def populate_fitness(db):
    """Populate fitness logs and body metrics"""
    print("Populating Fitness Data...")
    
    fitness_model = FitnessModel(db)
    
    today = datetime.now()
    
    activities = [
        ("Running", 45, 450, 7.5),
        ("Cycling", 60, 520, 20),
        ("Swimming", 40, 380, 1.5),
        ("Weight Training", 50, 280, 0),
        ("Yoga", 35, 150, 0),
        ("Walking", 30, 180, 4),
        ("HIIT Workout", 25, 320, 0)
    ]
    
    # Add fitness logs (3-4 times per week for last 60 days)
    for day in range(60):
        date = (today - timedelta(days=day)).strftime('%Y-%m-%d')
        
        # 50% chance of workout on any given day
        if random.random() > 0.5:
            activity, duration, calories, distance = random.choice(activities)
            # Add some variation
            duration = int(duration * random.uniform(0.8, 1.2))
            calories = int(calories * random.uniform(0.9, 1.1))
            if distance > 0:
                distance = round(distance * random.uniform(0.8, 1.2), 2)
            else:
                distance = None
            
            fitness_model.add_log(date, activity, duration, calories, distance)
    
    print("  [OK] Added fitness logs")
    
    # Body metrics (weekly)
    for week in range(12):
        date = (today - timedelta(days=week*7)).strftime('%Y-%m-%d')
        weight = 75 + random.uniform(-3, 3)
        body_fat = 18 + random.uniform(-2, 2)
        muscle_mass = 35 + random.uniform(-1, 1)
        
        fitness_model.add_body_metric(date, round(weight, 1), round(body_fat, 1), round(muscle_mass, 1))
    
    print("  [OK] Added body metrics\n")

def populate_goals(db):
    """Populate personal and savings goals"""
    print("Populating Goals...")
    
    goal_model = GoalModel(db)
    
    goals = [
        ("Read 24 Books This Year", "HABIT", 24, 8, "2024-01-01", "2026-12-31", "Active"),
        ("Meditate Daily", "HABIT", 365, 45, "2024-01-01", "2026-12-31", "Active"),
        ("Learn Spanish", "HABIT", 100, 35, "2024-02-01", "2026-08-01", "Active"),
        ("Run a Marathon", "HABIT", 1, 0, "2024-01-01", "2026-10-15", "Active"),
        ("Save for Vacation", "SAVINGS", 5000, 2800, "2024-01-01", "2026-08-01", "Active"),
        ("Emergency Fund Goal", "SAVINGS", 20000, 12000, "2024-01-01", "2026-12-31", "Active"),
        ("Lose 10kg", "HABIT", 10, 4, "2024-01-01", "2026-06-30", "Active")
    ]
    
    for name, goal_type, target, current, start_date, end_date, status in goals:
        goal_model.add_goal(name, goal_type, target, current, start_date, end_date, None, status)
    
    print("  [OK] Added goals")
    
    # Add some goal logs
    all_goals = goal_model.get_goals()
    for goal in all_goals[:3]:  # Add logs for first 3 goals
        for i in range(5):
            date = (datetime.now() - timedelta(days=i*7)).strftime('%Y-%m-%d')
            value = random.uniform(0.5, 2) if goal['type'] == 'HABIT' else random.uniform(50, 200)
            goal_model.add_goal_log(goal['id'], value, date, f"Progress update {i+1}")
    
    print("  [OK] Added goal logs\n")

def populate_events(db):
    """Populate events and travel plans"""
    print("Populating Events...")
    
    event_model = EventModel(db)
    
    today = datetime.now()
    
    events = [
        ("Summer Vacation - Hawaii", "Vacation", 
         (today + timedelta(days=120)).strftime('%Y-%m-%d'),
         (today + timedelta(days=127)).strftime('%Y-%m-%d'),
         "Honolulu, Hawaii", 3500, "Planning"),
        
        ("Family Reunion", "Family Gathering",
         (today + timedelta(days=45)).strftime('%Y-%m-%d'),
         (today + timedelta(days=47)).strftime('%Y-%m-%d'),
         "Chicago, IL", 800, "Planning"),
        
        ("Tech Conference 2026", "Conference",
         (today + timedelta(days=90)).strftime('%Y-%m-%d'),
         (today + timedelta(days=93)).strftime('%Y-%m-%d'),
         "San Francisco, CA", 1200, "Confirmed"),
        
        ("Weekend Camping Trip", "Recreation",
         (today + timedelta(days=30)).strftime('%Y-%m-%d'),
         (today + timedelta(days=32)).strftime('%Y-%m-%d'),
         "Yosemite National Park", 400, "Planning"),
        
        ("Friend's Wedding", "Wedding",
         (today + timedelta(days=75)).strftime('%Y-%m-%d'),
         (today + timedelta(days=75)).strftime('%Y-%m-%d'),
         "New York, NY", 600, "Confirmed")
    ]
    
    for name, event_type, start_date, end_date, location, budget, status in events:
        event_model.add_event(name, event_type, start_date, end_date, location, budget, f"Notes for {name}", status)
    
    print("  [OK] Added events")
    
    # Add tasks for first event
    all_events = event_model.get_events()
    if all_events:
        event_id = all_events[0]['id']
        tasks = [
            "Book flights",
            "Reserve hotel",
            "Plan activities",
            "Pack luggage",
            "Arrange pet care"
        ]
        for task in tasks:
            event_model.add_task(event_id, task)
    
    print("  [OK] Added event tasks\n")

def populate_digital_life(db):
    """Populate digital subscriptions, accounts, and assets"""
    print("Populating Digital Life...")
    
    sub_model = DigitalSubscriptionModel(db)
    acc_model = DigitalAccountModel(db)
    asset_model = DigitalAssetModel(db)
    
    today = datetime.now()
    
    # Digital Subscriptions
    subscriptions = [
        ("Netflix", "Streaming (Video)", 15.99, "Monthly", (today + timedelta(days=15)).strftime('%Y-%m-%d'), "Netflix Inc.", True),
        ("Spotify Premium", "Streaming (Music)", 10.99, "Monthly", (today + timedelta(days=8)).strftime('%Y-%m-%d'), "Spotify", True),
        ("Amazon Prime", "Shopping", 139, "Yearly", (today + timedelta(days=180)).strftime('%Y-%m-%d'), "Amazon", True),
        ("Adobe Creative Cloud", "Software/SaaS", 54.99, "Monthly", (today + timedelta(days=22)).strftime('%Y-%m-%d'), "Adobe", True),
        ("GitHub Pro", "Software/SaaS", 4, "Monthly", (today + timedelta(days=12)).strftime('%Y-%m-%d'), "GitHub", True),
        ("Google One (2TB)", "Cloud Storage", 9.99, "Monthly", (today + timedelta(days=5)).strftime('%Y-%m-%d'), "Google", True),
        ("ChatGPT Plus", "Software/SaaS", 20, "Monthly", (today + timedelta(days=18)).strftime('%Y-%m-%d'), "OpenAI", True),
        ("Dropbox Plus", "Cloud Storage", 11.99, "Monthly", (today + timedelta(days=25)).strftime('%Y-%m-%d'), "Dropbox", True),
        ("New York Times Digital", "News/Media", 17, "Monthly", (today + timedelta(days=10)).strftime('%Y-%m-%d'), "NYT", True),
        ("LinkedIn Premium", "Productivity", 29.99, "Monthly", (today + timedelta(days=20)).strftime('%Y-%m-%d'), "LinkedIn", False)
    ]
    
    for name, category, cost, billing, renewal, provider, active in subscriptions:
        sub_model.add_subscription(name, category, cost, billing, renewal, provider, f"Subscription to {name}", active)
    
    print("  [OK] Added digital subscriptions")
    
    # Online Accounts
    accounts = [
        ("Google/Gmail", "personal@gmail.com", "Email", True, (today - timedelta(days=45)).strftime('%Y-%m-%d'), "personal@gmail.com"),
        ("Facebook", "user.name", "Social Media", True, (today - timedelta(days=90)).strftime('%Y-%m-%d'), "personal@gmail.com"),
        ("Twitter/X", "@username", "Social Media", True, (today - timedelta(days=120)).strftime('%Y-%m-%d'), "personal@gmail.com"),
        ("Instagram", "username", "Social Media", False, (today - timedelta(days=200)).strftime('%Y-%m-%d'), "personal@gmail.com"),
        ("LinkedIn", "professional.name", "Work/Professional", True, (today - timedelta(days=60)).strftime('%Y-%m-%d'), "work@email.com"),
        ("GitHub", "developer123", "Developer/Tech", True, (today - timedelta(days=30)).strftime('%Y-%m-%d'), "personal@gmail.com"),
        ("Amazon", "shopper@email.com", "Shopping", True, (today - timedelta(days=150)).strftime('%Y-%m-%d'), "personal@gmail.com"),
        ("Bank of America", "customer123", "Banking/Finance", True, (today - timedelta(days=45)).strftime('%Y-%m-%d'), "personal@gmail.com"),
        ("PayPal", "paypal@email.com", "Banking/Finance", True, (today - timedelta(days=90)).strftime('%Y-%m-%d'), "personal@gmail.com"),
        ("Dropbox", "user@email.com", "Cloud/Storage", False, (today - timedelta(days=220)).strftime('%Y-%m-%d'), "personal@gmail.com"),
        ("Netflix", "streaming@email.com", "Entertainment", False, (today - timedelta(days=180)).strftime('%Y-%m-%d'), "personal@gmail.com"),
        ("Healthcare Portal", "patient123", "Healthcare", True, (today - timedelta(days=75)).strftime('%Y-%m-%d'), "personal@gmail.com")
    ]
    
    for service, username, category, has_2fa, last_pwd_change, email in accounts:
        acc_model.add_account(service, username, category, has_2fa, last_pwd_change, email, f"Account for {service}")
    
    print("  [OK] Added online accounts")
    
    # Digital Assets
    assets = [
        ("myportfolio.com", "Domain Name", 15, (today + timedelta(days=320)).strftime('%Y-%m-%d'), "Namecheap", True),
        ("myblog.dev", "Website/Blog", 0, (today + timedelta(days=280)).strftime('%Y-%m-%d'), "Vercel", True),
        ("AWS Account", "Cloud Storage", 50, None, "Amazon Web Services", True),
        ("Personal Website Hosting", "Server/Hosting", 120, (today + timedelta(days=150)).strftime('%Y-%m-%d'), "DigitalOcean", True),
        ("SSL Certificate", "Digital Certificate", 80, (today + timedelta(days=200)).strftime('%Y-%m-%d'), "Let's Encrypt", True),
        ("Adobe License", "Software License", 600, (today + timedelta(days=365)).strftime('%Y-%m-%d'), "Adobe", True),
        ("Crypto Wallet", "Cryptocurrency", 2500, None, "Coinbase", True),
        ("NFT Collection", "NFT/Digital Art", 800, None, "OpenSea", True)
    ]
    
    for name, asset_type, value, renewal, provider, active in assets:
        asset_model.add_asset(name, asset_type, value, renewal, provider, f"Digital asset: {name}", active)
    
    print("  [OK] Added digital assets\n")

def main():
    """Main function to populate all dummy data"""
    print("=" * 60)
    print("LIFE LEDGER - COMPREHENSIVE DUMMY DATA POPULATION")
    print("=" * 60)
    print()
    
    # Initialize database
    db = DatabaseManager()
    
    # Optional: Clear existing data (comment out if you want to keep existing data)
    clear_all_data(db)
    
    # Populate all modules
    populate_finances(db)
    populate_inventory(db)
    populate_people(db)
    populate_health(db)
    populate_fitness(db)
    populate_goals(db)
    populate_events(db)
    populate_digital_life(db)
    
    print("=" * 60)
    print("[OK] ALL DUMMY DATA POPULATED SUCCESSFULLY!")
    print("=" * 60)
    print()
    print("Summary:")
    print("  • Financial transactions, assets, loans, insurance, savings")
    print("  • Inventory items and possessions")
    print("  • Contacts and debt relationships")
    print("  • Health metrics and medications")
    print("  • Fitness logs and body metrics")
    print("  • Personal and savings goals")
    print("  • Events and travel plans")
    print("  • Digital subscriptions, accounts, and assets")
    print()
    print("You can now launch the application to see all pages populated!")
    print("Run: python main.py")
    print()

if __name__ == "__main__":
    main()

