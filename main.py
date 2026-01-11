import sys
import traceback
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.components.error_dialog import ErrorDialog

def exception_hook(exc_type, exc_value, exc_traceback):
    """
    Global function to catch unhandled exceptions.
    """
    error_msg = str(exc_value)
    traceback_str = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    
    # Print to console as well
    print("Uncaught Exception:", error_msg)
    print(traceback_str)
    
    # Ensure QApplication exists before showing dialog
    if QApplication.instance():
        dialog = ErrorDialog(error_msg, traceback_str)
        dialog.exec()
    else:
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

if __name__ == "__main__":
    sys.excepthook = exception_hook
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
