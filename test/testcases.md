# Test Cases – Cybersecurity Asset Inventory System

## 1. Introduction

This document contains the test cases used to verify the functionality of the Cybersecurity Asset Inventory System.

The system is tested for:

- Adding assets
- Displaying assets
- Searching for assets
- Updating asset information
- Deleting assets
- Generating security summary
- Validating user input
- Handling invalid asset IDs

---

## 2. Test Case Format

| Field | Description |
|---|---|
| Test Case ID | Unique identifier for the test |
| Feature | Functionality being tested |
| Input | Data provided to the system |
| Expected Result | Expected system behavior |
| Actual Result | Observed system behavior |
| Status | Pass/Fail |

---

## 3. Add Asset Test Cases

### TC-01: Add a Valid Asset

**Feature:** Add Asset

**Input:**
- Asset ID: A001
- Name: Office Laptop
- Type: Computer
- IP Address: 192.168.1.10
- Security Status: Secure

**Expected Result:**
The asset should be successfully added to the inventory.

**Actual Result:**
Asset A001 was added successfully.

**Status:** PASS

---

### TC-02: Add Another Valid Asset

**Feature:** Add Asset

**Input:**
- Asset ID: A002
- Name: Web Server
- Type: Server
- IP Address: 192.168.1.20
- Security Status: At Risk

**Expected Result:**
The asset should be added successfully.

**Actual Result:**
Asset A002 was added successfully.

**Status:** PASS

---

### TC-03: Add Asset with Duplicate ID

**Feature:** Add Asset

**Input:**
- Asset ID: A001
- Name: Another Laptop

**Expected Result:**
The system should reject the asset because the asset ID already exists.

**Actual Result:**
Duplicate asset ID was rejected.

**Status:** PASS

---

## 4. Display Asset Test Cases

### TC-04: Display All Assets

**Feature:** Display Assets

**Input:**
Select the "Display Assets" option.

**Expected Result:**
All assets stored in `assets.json` should be displayed with their details.

**Actual Result:**
All available assets were displayed successfully.

**Status:** PASS

---

### TC-05: Display Empty Inventory

**Feature:** Display Assets

**Input:**
Inventory contains no assets.

**Expected Result:**
The system should display a suitable message such as:

`No assets found.`

**Actual Result:**
The system displayed that no assets were available.

**Status:** PASS

---

## 5. Search Asset Test Cases

### TC-06: Search Existing Asset

**Feature:** Search Asset

**Input:**
Asset ID: A001

**Expected Result:**
The details of asset A001 should be displayed.

**Actual Result:**
Asset A001 was found and its details were displayed.

**Status:** PASS

---

### TC-07: Search Non-Existing Asset

**Feature:** Search Asset

**Input:**
Asset ID: A999

**Expected Result:**
The system should display a message indicating that the asset was not found.

**Actual Result:**
The system displayed `Asset not found.`

**Status:** PASS

---

## 6. Update Asset Test Cases

### TC-08: Update Existing Asset

**Feature:** Update Asset

**Input:**
- Asset ID: A001
- Security Status: At Risk

**Expected Result:**
The security status of asset A001 should be updated from Secure to At Risk.

**Actual Result:**
Asset A001 was updated successfully.

**Status:** PASS

---

### TC-09: Update Non-Existing Asset

**Feature:** Update Asset

**Input:**
Asset ID: A999

**Expected Result:**
The system should display an error message because the asset does not exist.

**Actual Result:**
The system displayed `Asset not found.`

**Status:** PASS

---

## 7. Delete Asset Test Cases

### TC-10: Delete Existing Asset

**Feature:** Delete Asset

**Input:**
Asset ID: A002

**Expected Result:**
Asset A002 should be removed from the inventory.

**Actual Result:**
Asset A002 was deleted successfully.

**Status:** PASS

---

### TC-11: Delete Non-Existing Asset

**Feature:** Delete Asset

**Input:**
Asset ID: A999

**Expected Result:**
The system should display an error message indicating that the asset does not exist.

**Actual Result:**
The system displayed `Asset not found.`

**Status:** PASS

---

## 8. Security Summary Test Cases

### TC-12: Generate Security Summary

**Feature:** Security Summary

**Input:**
Inventory contains assets with different security statuses.

Example:

- A001 – Secure
- A002 – At Risk
- A003 – Critical

**Expected Result:**
The system should count and display the number of assets according to their security status.

**Actual Result:**
The security summary was generated successfully.

**Status:** PASS

---

### TC-13: Security Summary with No Assets

**Feature:** Security Summary

**Input:**
Inventory contains no assets.

**Expected Result:**
The system should display an appropriate message indicating that there are no assets to analyze.

**Actual Result:**
The system handled the empty inventory successfully.

**Status:** PASS

---

## 9. Input Validation Test Cases

### TC-14: Empty Asset ID

**Feature:** Input Validation

**Input:**
Asset ID: Empty

**Expected Result:**
The system should reject the input and request a valid asset ID.

**Actual Result:**
Empty asset ID was rejected.

**Status:** PASS

---

### TC-15: Empty Asset Name

**Feature:** Input Validation

**Input:**
Asset Name: Empty

**Expected Result:**
The system should reject the input and request a valid asset name.

**Actual Result:**
Empty asset name was rejected.

**Status:** PASS

---

### TC-16: Invalid IP Address

**Feature:** Input Validation

**Input:**
IP Address: `999.999.999.999`

**Expected Result:**
The system should reject the invalid IP address.

**Actual Result:**
Invalid IP address was rejected.

**Status:** PASS

---

### TC-17: Invalid Security Status

**Feature:** Input Validation

**Input:**
Security Status: `Unknown`

**Expected Result:**
The system should reject the value if it is not one of the allowed security statuses.

**Actual Result:**
Invalid security status was rejected.

**Status:** PASS

---

## 10. Data Persistence Test

### TC-18: Verify Data Saved to JSON

**Feature:** Data Persistence

**Input:**
Add a new asset and close/restart the program.

**Expected Result:**
The newly added asset should remain stored in `assets.json`.

**Actual Result:**
The asset data was successfully stored and loaded from `assets.json`.

**Status:** PASS

---

## 11. Test Summary

| Test Case | Feature | Status |
|---|---|---|
| TC-01 | Add valid asset | PASS |
| TC-02 | Add another asset | PASS |
| TC-03 | Duplicate asset ID | PASS |
| TC-04 | Display assets | PASS |
| TC-05 | Empty inventory | PASS |
| TC-06 | Search existing asset | PASS |
| TC-07 | Search non-existing asset | PASS |
| TC-08 | Update existing asset | PASS |
| TC-09 | Update non-existing asset | PASS |
| TC-10 | Delete existing asset | PASS |
| TC-11 | Delete non-existing asset | PASS |
| TC-12 | Security summary | PASS |
| TC-13 | Empty security summary | PASS |
| TC-14 | Empty asset ID | PASS |
| TC-15 | Empty asset name | PASS |
| TC-16 | Invalid IP address | PASS |
| TC-17 | Invalid security status | PASS |
| TC-18 | JSON data persistence | PASS |

## 12. Conclusion

The Cybersecurity Asset Inventory System was tested for its major functionalities, including asset management, searching, updating, deletion, security analysis, input validation, and data persistence.

The test cases demonstrate that the system can manage cybersecurity assets and handle both valid and invalid inputs appropriately.