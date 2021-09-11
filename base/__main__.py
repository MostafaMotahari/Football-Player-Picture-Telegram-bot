# Imports
from pyrogram import Client, filters

# Variables
api_hash = "8b8e85465f15d1100b1e464e2f894ca6"
api_id = 5133796

# Main
app = Client(
    "HadsfutBot",
    api_hash=api_hash,
    api_id=api_id,
    plugins=dict(root="base/plugins")
)

app.run()