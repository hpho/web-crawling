import win32com.client
mail_bot = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inboxfolder = mail_bot.GetDefaultFolder(6)
messages = inboxfolder.Items
print(messages.count)

[[str(i.ReceivedTime),i.Subject[9:-10],i.Body] for i in messages if i.SenderName == 'Google 학술검색 알리미']
