# Active Directory User Information Export Script

## Overview

This PowerShell script is designed to extract comprehensive user information from an Active Directory environment, including checking if users are members of the "Administrators" group. The collected data is then exported to a CSV file for further analysis or documentation.

## Prerequisites

- Windows Server 2012 R2 or a compatible operating system with PowerShell installed.
- Active Directory PowerShell module.
- Sufficient permissions to query Active Directory.

## Usage

1. **Open PowerShell as Administrator**: Right-click on PowerShell and choose "Run as Administrator" to ensure the necessary permissions for querying Active Directory.

2. **Set Execution Policy** (if required): If your PowerShell execution policy is restricted, you might need to allow script execution by running:

   ```powershell
   Set-ExecutionPolicy RemoteSigned
   ```

3. **Copy and Paste the Script**: Copy the provided PowerShell script and paste it into the PowerShell terminal.

4. **Run the Script**: Press Enter to execute the script.

5. **Review Output**: The script will extract user information and check if users are members of the "Administrators" group.

6. **Exported Data**: The collected data will be exported to a CSV file located on your desktop.

## Output

The exported CSV file, named `AD_Users_FullInfo.csv`, will contain the following user information:

- Name
- SamAccountName
- DistinguishedName
- Enabled (Account Status)
- Given Name
- Surname
- Email Address
- Office
- Department
- Title
- Description
- Street Address
- City
- State
- Postal Code
- Country
- Employee ID
- Employee Number
- Manager
- Member Of (Groups)
- Is Administrator (True/False)

## Disclaimer

Use this script responsibly and ensure that you have the necessary permissions to access and export data from Active Directory.