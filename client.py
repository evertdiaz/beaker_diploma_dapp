import contract
from pyteal import *
from beaker import *

# Open the file where we're saving the app ID
text_file = open("./artifacts/app_id", "r")
app_id = int(text_file.read())
text_file.close()

# Get the accounts trough the sandbox client
creator = sandbox.get_accounts().pop()
account = sandbox.get_accounts()[0]

# Create the Application Client
app_client = client.ApplicationClient(
  client = sandbox.get_algod_client(),
  app = contract.DiplomaApp(version=6),
  app_id = app_id,
  signer = creator.signer,
)

## Opt in wallet to the app
# app_client.opt_in()

# Call the register_diploma method, only callable by creator
# app_client.call(contract.DiplomaApp.register_diploma, title="Beaker workshop diploma", accounts=[account.address])

## Call the change_teacher method, only callable by creator
# app_client.call(contract.DiplomaApp.change_teacher, accounts=[account.address])
