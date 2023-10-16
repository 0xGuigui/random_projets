# Définition de l'encodage de PowerShell
$OutputEncoding = [System.Text.Encoding]::UTF8

# Spécifiez le chemin complet du fichier de sortie CSV
$OutputFile = [System.IO.Path]::Combine([System.Environment]::GetFolderPath('Desktop'), 'DUMP_AD.csv')

# Charger le module Active Directory si ce n'est pas déjà fait
if (-not (Get-Module -Name ActiveDirectory)) {
    Import-Module ActiveDirectory
    Write-Host "Module Active Directory chargé."
}

# Obtenir tous les utilisateurs de l'Active Directory
$Users = Get-ADUser -Filter *
Write-Host "Récupération des utilisateurs depuis Active Directory..."

# Créer un tableau pour stocker les données
$UserList = @()

# Parcourir chaque utilisateur et extraire les informations nécessaires
foreach ($User in $Users) {
    # Vérifier si le compte est actif
    $IsAccountActive = $User.Enabled

    # Obtenir tous les groupes auxquels l'utilisateur appartient
    $UserGroups = ($User | Get-ADPrincipalGroupMembership).Name -join ' - '

    # Obtenir le chemin complet de l'unité organisationnelle (OU) sous forme propre
    $OUs = $User.DistinguishedName -split ',' | Where-Object { $_ -match 'OU=' } | ForEach-Object { $_ -replace 'OU=', '' }
    $OUPath = $OUs -join ' - '

    # Obtenir la Fonction, le Service, la Ville et l'Adresse de messagerie de l'utilisateur
    $Function = $User.Title
    $Service = $User.Department
    $Ville = $User.L
    $AdresseEmail = $User.EmailAddress
    
    $UserObj = New-Object PSObject -Property @{
        "Compte actif" = $IsAccountActive
        "Login" = $User.SamAccountName
        "Nom" = $User.Surname
        "Prénom" = $User.GivenName
        "Email" = $AdresseEmail
        "Fonction" = $Function
        "Service" = $Service
        "Groupes" = $UserGroups
        "Role" = $OUPath
        "Ville" = $Ville
    }
    $UserList += $UserObj
    Write-Host "Données de l'utilisateur $($User.SamAccountName) traitées."
}

# Exporter le tableau vers un fichier CSV
$UserList | Export-Csv -Path $OutputFile -NoTypeInformation -Encoding UTF8
Write-Host "Les données de l'Active Directory ont été sauvegardées dans $OutputFile."
