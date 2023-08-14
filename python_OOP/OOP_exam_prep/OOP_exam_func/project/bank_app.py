from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")
        new_loan = self.LOAN_TYPES[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        new_client = self.CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = [l for l in self.loans if l.__class__.__name__ == loan_type][0]
        client = [c for c in self.clients if c.client_id == client_id][0]
        if loan_type == "StudentLoan" and client.__class__.__name__ == "Adult":
            raise Exception("Inappropriate loan type!")
        if loan_type == "MortgageLoan" and client.__class__.__name__ == "Student":
            raise Exception("Inappropriate loan type!")
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = [c for c in self.clients if c.client_id == client_id]
        if not client:
            raise Exception("No such client!")
        if client[0].loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client[0])
        return f"Successfully removed {client[0].name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loans_increased = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                loans_increased += 1
        return f"Successfully changed {loans_increased} loans."

    def increase_clients_interest(self, min_rate: float):
        clients_changed = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                clients_changed += 1
        return f"Number of clients affected: {clients_changed}."

    def get_statistics(self):
        result = f"Active Clients: {len(self.clients)}\n"
        total_income = sum([c.income for c in self.clients])
        result += f"Total Income: {total_income:.2f}\n"
        granted_loans = sum([len(c.loans) for c in self.clients])
        granted_sum = 0
        for client in self.clients:
            for c in client.loans:
                granted_sum += c.amount
        result += f"Granted Loans: {granted_loans}, Total Sum: {granted_sum:.2f}\n"
        not_granted_sum = sum([l.amount for l in self.loans])
        result += f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n"
        if self.clients:
            avg_client_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients)
        else:
            avg_client_interest_rate = 0
        result += f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        return result

bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))


print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())





