
# =========================================
#   CYBERSECURITY ASSET INVENTORY SYSTEM
# =========================================
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FILE = os.path.join(BASE_DIR, "data", "assets.json")

def load_assets():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_assets():
    with open(DATA_FILE, "w") as file:
        json.dump(assets, file, indent=4)
assets = []

# Allowed values
ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]


# Function to display one asset
def display_asset(asset):
    print("-----------------------------------------")
    print("Asset ID     :", asset["id"])
    print("Asset Name   :", asset["name"])
    print("Asset Type   :", asset["type"])
    print("IP Address   :", asset["ip"])
    print("OS           :", asset["os"])
    print("Department   :", asset["department"])
    print("Risk Level   :", asset["risk"])
    print("Status       :", asset["status"])


# Function to choose a valid option
def get_choice(prompt, options):
    while True:
        print("\n" + prompt)

        for i, option in enumerate(options, 1):
            print(i, ".", option)

        choice = input("Enter choice: ").strip()

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(options):
                return options[choice - 1]

        print("Invalid choice! Please try again.")


# Function to add an asset
def add_asset():
    print("\n========== ADD NEW ASSET ==========")

    asset_id = input("Asset ID: ").strip()

    # Check duplicate ID
    for asset in assets:
        if asset["id"] == asset_id:
            print("Asset ID already exists!")
            return

    asset_name = input("Asset Name: ").strip()
    if asset_name=="":
        print("asset name cant be empty")

    asset_type = get_choice("Select Asset Type:", ASSET_TYPES)

    ip_address = input("IP Address: ").strip()

    operating_system = input("Operating System: ").strip()

    department = input("Owner/Department: ").strip()

    risk_level = get_choice("Select Risk Level:", RISK_LEVELS)

    security_status = get_choice(
        "Select Security Status:",
        SECURITY_STATUSES
    )

    asset = {
        "id": asset_id,
        "name": asset_name,
        "type": asset_type,
        "ip": ip_address,
        "os": operating_system,
        "department": department,
        "risk": risk_level,
        "status": security_status
    }

    assets.append(asset)
    save_assets()

    print("\nAsset added successfully!")


# Function to display all assets
def display_all_assets():
    print("\n=========================================")
    print("       CYBERSECURITY ASSET INVENTORY")
    print("=========================================")

    if len(assets) == 0:
        print("No assets found.")
        return

    for asset in assets:
        display_asset(asset)
        
    print("-----------------------------------------")
    print( " S E C U R I T Y   S U M M A R Y ")
    print("-----------------------------------------")
    print("Total Assets       :", len(assets))
    print("Critical Assets    :", count_risk("Critical"))
    print("High Risk Assets   :", count_risk("High"))
    print("Medium Risk Assets :", count_risk("Medium"))
    print("Vulnerable Assets  :", count_status("Vulnerable"))
 
    print("=========================================")


# Function to count risk levels
def count_risk(level):
    count = 0

    for asset in assets:
        if asset["risk"] == level:
            count += 1

    return count


# Function to count security status
def count_status(status):
    count = 0

    for asset in assets:
        if asset["status"] == status:
            count += 1

    return count


# Function to search an asset
def search_asset():
    print("\n========== SEARCH ASSET ==========")

    search_id = input("Enter Asset ID: ").strip()

    for asset in assets:
        if asset["id"] == search_id:
            print("\nAsset Found!")
            display_asset(asset)
            return

    print("Asset not found!")


# Function to update an asset
def update_asset():
    print("\n========== UPDATE ASSET ==========")

    update_id = input("Enter Asset ID to update: ").strip()

    for asset in assets:
        if asset["id"] == update_id:

            print("\nAsset Found!")
            display_asset(asset)

            print("\nEnter new details:")

            asset["name"] = input(
                "Asset Name: "
            ).strip()

            asset["type"] = get_choice(
                "Select Asset Type:",
                ASSET_TYPES
            )

            asset["ip"] = input(
                "IP Address: "
            ).strip()

            asset["os"] = input(
                "Operating System: "
            ).strip()

            asset["department"] = input(
                "Owner/Department: "
            ).strip()

            asset["risk"] = get_choice(
                "Select Risk Level:",
                RISK_LEVELS
            )

            asset["status"] = get_choice(
                "Select Security Status:",
                SECURITY_STATUSES
            )

            save_assets()

            print("\nAsset updated successfully!")
            return

    print("Asset not found!")


# Function to delete an asset
def delete_asset():
    print("\n========== DELETE ASSET ==========")

    delete_id = input("Enter Asset ID to delete: ").strip()

    for asset in assets:
        if asset["id"] == delete_id:
            assets.remove(asset)
            save_assets()
            print("Asset deleted successfully!")
            return

    print("Asset not found!")


# Main menu
def main():

    global assets

    assets = load_assets()
    while True:

        print("\n=========================================")
        print("   CYBERSECURITY ASSET INVENTORY SYSTEM")
        print("=========================================")

        print("1. Add Asset")
        print("2. Search Asset")
        print("3. Update Asset")
        print("4. Delete Asset")
        print("5. Display All Assets")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_asset()

        elif choice == "2":
            search_asset()

        elif choice == "3":
            update_asset()

        elif choice == "4":
            delete_asset()

        elif choice == "5":
            display_all_assets()

        elif choice == "6":
            print("Thank you for using Asset Inventory System!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()
