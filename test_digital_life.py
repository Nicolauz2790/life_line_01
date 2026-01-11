"""
Test script to verify Digital Life functionality
"""
from database.manager import DatabaseManager
from models.digital_life import DigitalSubscriptionModel, DigitalAccountModel, DigitalAssetModel

# Initialize database
db = DatabaseManager()

# Test Subscription Model
print("Testing Subscription Model...")
sub_model = DigitalSubscriptionModel(db)
subs = sub_model.get_subscriptions()
print(f"  Found {len(subs)} subscriptions")

# Test Account Model
print("\nTesting Account Model...")
acc_model = DigitalAccountModel(db)
accounts = acc_model.get_accounts()
print(f"  Found {len(accounts)} accounts")

# Test Asset Model
print("\nTesting Asset Model...")
asset_model = DigitalAssetModel(db)
assets = asset_model.get_assets()
print(f"  Found {len(assets)} digital assets")

print("\n✓ All models working correctly!")
print("\nDatabase tables verified:")
print("  - digital_subscriptions")
print("  - digital_accounts")
print("  - digital_assets")
