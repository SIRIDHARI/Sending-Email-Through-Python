# Sending-Email-Through-Python

Sure, here's a simple README file for your GitHub repository:

```markdown
# Email Sending through Python

This is a simple Python script to send an email using Gmail's SMTP server.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- `smtplib` library (comes with Python)
- `getpass` library (comes with Python)

## Working
 Certainly! Here's a brief explanation of the code:

1. **Importing Libraries**:
   - `smtplib`: This library provides functionality to send emails via SMTP (Simple Mail Transfer Protocol).
   - `getpass`: This library allows you to securely prompt the user for a password.
   - `MIMEText` from `email.mime.text`: This is used to create the body of the email.

2. **Defining the `send_email()` Function**:
   - This function encapsulates the logic to send an email.
   - It prompts the user to input their password securely.
   - It sets up the email message with sender, recipient, subject, and body.

3. **Setting Up Email Details**:
   - `sender_address`: The sender's email address.
   - `password`: The sender's email password (securely input by the user).
   - `subject`: The subject of the email.
   - `msg`: The body of the email.
   - `recipients`: The recipient's email address.

4. **Initializing SMTP Server**:
   - It creates an SMTP server object for Gmail at `smtp.gmail.com` on port `587`.
   - It starts TLS encryption for secure communication.

5. **Logging in to SMTP Server**:
   - It logs in to the SMTP server using the sender's email address and password.

6. **Drafting the Email**:
   - It creates a `MIMEText` object for the email body.
   - It sets the subject, sender, and recipient of the email.

7. **Sending the Email**:
   - It sends the email using the SMTP server to the specified recipient.
   - The email is converted to a string using `msg.as_string()`.

8. **Closing the Connection**:
   - It closes the connection to the SMTP server.

9. **Calling the `send_email()` Function**:
   - Finally, it calls the `send_email()` function to execute the sending process.

This code sends an email using Gmail's SMTP server, with the sender's email address specified in the `sender_address` variable, and the recipient's email address specified in the `recipients` variable. The email content, including subject and body, is also specified within the code.

## Configuration

Before running the script, make sure to update the following variables in `send_email.py`:

- `sender_address`: Your Gmail email address.
- `password`: Your Gmail password. It's recommended to use an App Password if you have 2-factor authentication enabled.
- `subject`: Subject of the email.
- `msg`: Content of the email.
- `recipients`: Email address of the recipient.


