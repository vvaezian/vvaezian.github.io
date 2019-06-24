-  **grep** Equivalent: `findstr "test"` (case insensetive: `findstr /I`)  
Similar function: `find str "test"` (cases insensetive: `find str -i`)

- Help: `<command> /?`


### Process Email

````Powershell
# Read emails of email addres 'test$test.com' from folder 'testDir'
Add-Type -Assembly "Microsoft.Office.Interop.Outlook"
$Outlook = New-Object -ComObject Outlook.Application
$namespace = $Outlook.GetNameSpace("MAPI")
$dir = $namespace.Folders.Item('test$test.com').Folders.Item('testDir')

# Get the list of emails in the folder defined above and reversing the order of emails (by default starts with the oldest)
$emails = $dir.Items | Sort-Object -Descending ReceivedTime # | convertTo-Json | Out-File test.json -Encoding UTF8


````
