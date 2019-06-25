-  **grep** Equivalent: `findstr "test"` (case insensetive: `findstr /I`)  

- Help: `<command> /?`


### Process Email

````Powershell
# Connect to the email client
Add-Type -Assembly "Microsoft.Office.Interop.Outlook"
$Outlook = New-Object -ComObject Outlook.Application
$namespace = $Outlook.GetNameSpace("MAPI")

# get emails in the desired folder
$dir = $namespace.Folders.Item('vvaezian@markanthony.com').Folders.Item('Account Change')
$emails = $dir.Items | Sort-Object -Descending ReceivedTime 

# extract Lic numbers and Sales Rep names from email bodies
$Managers = "Lisa Anderson","Lesley Brown","Tracey Finlay","Andrew Leonard","Anita Webb","Kaity Mattsson","Charles Boisseau","Patrick Pelletier","Emily Altoft","Graham Kersch","Natasha Haubrich","Rocco D'Agostino","Tara Wallis","Steve Totten"
[System.Collections.ArrayList]$outputArray = @()

foreach ($email in $emails) {
  $nameLinesList = ""
  $LicNumsList = ""
  
  # limiting to emails received in the last hour
  if ($email.SentOn -lt (get-date).AddHours(-1)) {
    break
  }
  
  # Adding timestamp to the output array
  $outputArray.Add($email.SentOn)

  # Checking if the email is asking for any removing or replacing action
  if (($email.body -like '*remov*') -or ($email.body -like '*replac*') -or ($email.body -like '*switch*') ){
    $outputArray.Add("Remove, Replace or Switch Detected!")
    #continue
  }

  # Get Lic Numbers and add to the output array
  [regex]$regex = '[0-9][0-9][0-9][0-9][0-9][0-9]+'
  $LicNumsString = $regex.Matches($email.body)| foreach-object {$_.Value}
  $LicNumsList = $LicNumsString.Split("`n`r");
  $outputArray.Add($LicNumsList)

  # Get Sales Rep Name and add to the output array
  $nameLinesString = $email.body | findstr ' | ' | findstr /V 'direct mobile Anthony http'
  $nameLinesList = $nameLinesString.Split("`n`r");
  # echo "nameLinesList: " $nameLinesList

  [regex]$regex = '.* \|'
  foreach($nameLine in $nameLinesList){
    $name = $regex.Matches($nameLine) | foreach-object {$_.Value}
    $cleanName = $name.substring(0, $name.length -2)   
    if (-Not($Managers -contains $cleanName)){
      $outputArray.Add($cleanName)
    }
  }
  write-output "------------------------------------------------------"
  $outputArray.Add('---------')
}
$outputArray | Out-File -Append AccountChange.log

###########
### Important attributes:
# SenderName
# To
# SentOn
# Subject
# Body
# HTMLBody
# AutoForwarded


# $m1=$dir.items
# $m2=$dir.items.getlast()
# write-output $m1.count
# $emails = $dir.Items | Sort-Object -Descending ReceivedTime # | convertTo-Json | Out-File test.json -Encoding UTF8
````
