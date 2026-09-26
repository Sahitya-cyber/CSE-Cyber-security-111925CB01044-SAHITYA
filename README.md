Cybersecurity Asset Inventory System

A simple Cybersecurity Asset Inventory System designed to help organizations maintain and monitor information about their IT assets such as workstations, servers, routers, switches, and applications.

The system allows a security administrator to add, search, update, delete, and display assets, while also classifying them based on risk level and security status.

📌 Problem Statement

Organizations manage a large number of IT assets, including computers, servers, network devices, and software applications. Managing these assets manually can make it difficult to:

Identify and track organizational assets
Monitor the security status of assets
Identify high-risk and critical assets
Detect vulnerable systems
Maintain accurate asset information
This project provides a centralized Cybersecurity Asset Inventory System to manage asset information and identify assets that require immediate security attention.

🎯 Objectives

Maintain a structured inventory of IT assets
Store important asset information in one place
Classify assets according to their type
Assign security risk levels
Track the security status of assets
Identify critical and high-risk assets
Identify vulnerable assets
Provide CRUD operations for asset management
🖥️ Asset Information

Each asset contains the following information:

Field	Description
Asset ID	Unique identifier of the asset
Asset Name	Name assigned to the asset
Asset Type	Type of IT asset
IP Address	Network address of the asset
Operating System	OS installed on the asset
Department	Department responsible for the asset
Risk Level	Security risk associated with the asset
Security Status	Current security condition
🗂️ Asset Types

The system supports the following asset types:

🖥️ Workstation
🗄️ Server
🌐 Router
🔀 Switch
💻 Application
⚠️ Risk Levels

Each asset is classified into one of four risk levels:

Risk Level	Description
Low	Minimal security risk
Medium	Moderate security risk
High	Significant security risk
Critical	Very high security risk requiring immediate attention
🛡️ Security Status

The security status of an asset can be:

✅ Secure – Asset is currently considered secure
⚠️ Warning – Potential security concern exists
🔴 Vulnerable – Asset has a significant security weakness
⚙️ System Features

Add Asset
Allows the administrator to add a new asset to the inventory.

Search Asset
Allows assets to be searched using information such as Asset ID or Asset Name.

Update Asset
Allows existing asset information to be modified.

Delete Asset
Allows an asset to be removed from the inventory.

Display Assets
Displays all registered assets with their complete information.

Risk Classification
Assets are classified as Low, Medium, High, or Critical based on their risk level.

Security Monitoring
The system identifies assets that are Secure, under Warning, or Vulnerable.

Security Summary
The system provides a summary containing:

Total number of assets
Number of Critical assets
Number of High-risk assets
Number of Medium-risk assets
Number of Vulnerable assets
📊 Sample Asset

Asset ID : A102 Asset Name : Web-Server Asset Type : Server IP Address : 192.168.1.20 OS : Ubuntu Department : IT Risk Level : Critical Status : Vulnerable

📈 Sample Summary

========================================= CYBERSECURITY ASSET INVENTORY
Total Assets : 3 Critical Assets : 1 High Risk Assets : 1 Medium Risk Assets : 1 Vulnerable Assets : 1

=========================================

📁 Project Structure

Cybersecurity-Asset-Inventory/ │ ├── assets/ │ └── asset.json │ ├── src/ │ └── main.py │ ├── tests/ │ └── testcases.md │ ├── README.md │ └── requirements.txt


> The exact file structure can be modified depending on the implementation.

🧪 Testing

The system should be tested for:

* Adding valid assets
* Searching existing assets
* Searching non-existing assets
* Updating asset information
* Deleting assets
* Validating asset types
* Validating risk levels
* Validating security status
* Identifying critical assets
* Identifying vulnerable assets
* Generating the correct asset summary

Test cases are documented in:

tests/testcases.md

🔒 Cybersecurity Relevance

This project demonstrates basic concepts of *cybersecurity asset management*.

Maintaining an asset inventory is important because an organization cannot effectively protect systems that it does not know about. By tracking asset types, ownership, network information, risk levels, and security status, security administrators can identify assets that may require additional security controls or investigation.

🚀 Future Enhancements

The project can be extended with:

* 🔍 Automated vulnerability scanning
* 📊 Security dashboard
* 🔐 User authentication
* 📧 Security alert notifications
* 🗃️ Database integration
* 🌐 Web-based interface
* 📈 Risk visualization and charts
* 🔄 Automatic asset discovery
* 🛡️ Integration with vulnerability databases
* 📝 Exporting inventory reports

🛠️ Technologies

The project can be implemented using:

* Python
* JSON
* Git & GitHub
* Unit Testing

👩‍💻 Author

Sahitya R S

Cybersecurity Student
