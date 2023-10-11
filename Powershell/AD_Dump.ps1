# Define the output CSV file path
$csvPath = "$env:USERPROFILE\Desktop\AD_Users_FullInfo.csv"

# Create an array to store the data
$exportData = @()

# Retrieve all users from Active Directory
$users = Get-ADUser -Filter *

foreach ($user in $users) {
    # Create a custom object to store user information
    $userObject = New-Object PSObject -Property @{
        "Name" = $user.Name
        "SamAccountName" = $user.SamAccountName
        "DistinguishedName" = $user.DistinguishedName
        "Enabled" = $user.Enabled
        "GivenName" = $user.GivenName
        "Surname" = $user.Surname
        "EmailAddress" = $user.EmailAddress
        "Office" = $user.Office
        "Department" = $user.Department
        "Title" = $user.Title
        "Description" = $user.Description
        "StreetAddress" = $user.StreetAddress
        "City" = $user.City
        "State" = $user.State
        "PostalCode" = $user.PostalCode
        "Country" = $user.Country
        "EmployeeID" = $user.EmployeeID
        "EmployeeNumber" = $user.EmployeeNumber
        "Manager" = (Get-ADUser $user.Manager -Properties DisplayName).DisplayName
        "MemberOf" = ($user | Get-ADPrincipalGroupMembership | Select-Object -ExpandProperty Name -join ", ")
        "IsAdministrator" = $false
    }

    # Check membership in the "Administrators" group
    $group = Get-ADGroup -Filter {Name -eq "Administrators"}
    if ($user.MemberOf -contains $group.DistinguishedName) {
        $userObject.IsAdministrator = $true
    }

    # Add the object to the list of exported data
    $exportData += $userObject
}

# Export the data to a CSV file
$exportData | Export-Csv -Path $csvPath -NoTypeInformation

Write-Host "Export completed. Data has been saved to $csvPath."
