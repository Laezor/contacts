# Contacts

Simple command-line contact book in `contacts.py`. Contacts are stored in memory for the current run only.

## Run

```bash
python contacts.py
```

The menu is in Greek.

## Menu

1. **Add a contact** — name and phone number
2. **Search** — find a contact by exact name
3. **View all** — list every saved contact
4. **Delete all** — clear the list after confirmation (`Ν` / `Ο`)
5. **Exit**

## Validation

- **Name:** letters only, spaces and hyphens allowed (for example `John Doe`, `Jean-Pierre`). Numbers in the name are rejected.
- **Phone:** digits only, or `+` followed by digits. Spaces are removed.

Contacts are not saved to a file. Closing the program clears the list.
