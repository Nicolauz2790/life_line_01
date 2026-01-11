import sys
import os
from PyQt6.QtWidgets import QApplication

# Mock UI to prevent show() blocking
def test_all_modules():
    print(">>> STARTING SYSTEM HEALTH CHECK <<<")
    
    app = QApplication(sys.argv)
    
    try:
        from database.manager import DatabaseManager
        db = DatabaseManager('test_health.db')
        print("[PASS] Database Connection")
    except Exception as e:
        print(f"[FAIL] Database Connection: {e}")
        return

    # Helper to test view instantiation
    def test_view(name, class_ref):
        try:
            view = class_ref(db)
            # Try loading data if method exists
            if hasattr(view, 'load_data'): view.load_data()
            if hasattr(view, 'refresh_data'): view.refresh_data()
            print(f"[PASS] {name}")
        except Exception as e:
            print(f"[FAIL] {name}: {e}")
            import traceback
            traceback.print_exc()

    # Import and Test Views
    try:
        from ui.views.dashboard_view import DashboardView
        test_view("DashboardView", DashboardView)

        from ui.views.finance_view import FinanceView
        test_view("FinanceView", FinanceView)

        from ui.views.inventory_view import InventoryView
        test_view("InventoryView", InventoryView)

        from ui.views.time_view import TimeView
        test_view("TimeView", TimeView)
        
        from ui.views.project_view import ProjectView
        test_view("ProjectView", ProjectView)
        
        from ui.views.library_view import LibraryView
        test_view("LibraryView", LibraryView)
        
        from ui.views.vault_view import VaultView
        test_view("VaultView", VaultView)
        
        from ui.views.meal_view import MealView
        test_view("MealView", MealView)

        from ui.views.digital_life_view import DigitalLifeView
        test_view("DigitalLifeView", DigitalLifeView)

        from ui.views.health_view import HealthView
        test_view("HealthView", HealthView)

        from ui.views.fitness_view import FitnessView
        test_view("FitnessView", FitnessView)
        
        from ui.views.people_view import PeopleView
        test_view("PeopleView", PeopleView)

        from ui.views.goal_view import GoalView
        test_view("GoalView", GoalView)

        from ui.views.insights_view import InsightsView
        test_view("InsightsView", InsightsView)

        from ui.views.event_view import EventView
        test_view("EventView", EventView)
        
        from ui.views.settings_view import SettingsView
        test_view("SettingsView", SettingsView)
        
    except ImportError as e:
        print(f"[CRITICAL FAIL] Import Error: {e}")

    print(">>> CHECKS COMPLETE <<<")
    # Clean up test db
    if os.path.exists("test_health.db"):
        os.remove("test_health.db")

if __name__ == "__main__":
    test_all_modules()
