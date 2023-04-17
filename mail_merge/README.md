# Description about the script
This is a simple Python program that merges a customized message with a list of names and saves each message in a separate file.


## Files you need before script execution

"names.txt" - This file will contain all the names you want to send email to with each name on separate line.
"body.txt" -  This file should contain the body of the email message.

The program will read the names from the "names.txt" file, merge them with the message in "body.txt", and save each customized message in a separate file named after the person's name.

## How to execute the script
```
python3 <file_name.py>
```

## After successful script execution
you will find separate text files for each person in the "Mails" folder, with a customized message for each person.