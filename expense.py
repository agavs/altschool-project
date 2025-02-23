# Object-oriented programming concept in Python: Class
# Import the necessary packages
import uuid
from datetime import datetime, timezone
# Expense Class
class Expense:
    def __init__(self, title: str, amount: float):
        self.id = str(uuid.uuid4()) # Generate unique id
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc) # Expense creation timestamp
        self.updated_at = self.created_at # Expense update timestamp

    def update(self, title: str = None, amount: float = None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        if title is not None or amount is not None:
            self.updated_at = datetime.now(timezone.utc)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
    
    # Expense Database Class
    class ExpenseDB:
        def __init__(self):
            self.expenses = []

        def add_expense(self, expense):
            self.expenses.append(expense)

        def remove_expense(self, expense_id: str):
            self.expenses = [expense for expense in self.expenses if expense.id != expense_id]

        def get_expense_by_id(self, expense_id: str):
            for expense in self.expenses:
                if expense.id == expense_id:
                    return expense
            return None
        
        def get_expense_by_title(self, title: str):
            return [expense for expense in self.expenses if expense.title.lower() == title.lower()]
        
        def to_dict(self):
            return [expense.to_dict() for expense in self.expenses]
        
         # Example
    if __name__ == "__main__":
        db = ExpenseDB()

        # Generate expenses
        exp_1 = db('Transport', 55.87)
        exp_2 = db('Lunch', 30.23)

        # Add to database
        db.add_expense(exp_1)
        db.add_expense(exp_2)
        
        # Update an expense
        exp_2.update(amount=320.50)
        print("\nUpdated exp_2:")
        print(db.get_expense_by_id(exp_2.id).to_dict())
    
        # Print expenses
        print("All expenses:")
        for expense_dict in db.to_dict():
            print(expense_dict)

        # Get expense by title
        transport_expenses = db.get_expense_by_title("Transport")
        print("\nTransport expenses:")
        for exp in transport_expenses:
            print(exp.to_dict())
        
   







        