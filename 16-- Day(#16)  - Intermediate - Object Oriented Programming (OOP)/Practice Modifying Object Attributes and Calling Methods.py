# Practice Modifying Object Attributes and Calling Methods
# import prettytable
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("DATA C ", ["AI ", "SE", "MP", "ARV"])
table.add_column("Macro care ", ["Medical", "Tourism", "In", "Egypt"])
table.add_column("DATA C ", ["AI ", "SE", "MP", "ARV"])
table.add_column("Macro care ", ["Medical", "Tourism", "In", "Egypt"])
table.add_column("DATA C ", ["AI ", "SE", "MP", "ARV"])
table.add_column("Macro care ", ["Medical", "Tourism", "In", "Egypt"])
table.add_column("DATA C ", ["AI ", "SE", "MP", "ARV"])
table.add_column("Macro care ", ["Medical", "Tourism", "In", "Egypt"])

# TO Align Table "L" or "R", Default mode is Middle
table.align = "l"

print(table)
