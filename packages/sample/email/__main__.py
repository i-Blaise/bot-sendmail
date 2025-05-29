import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

def main(event, context):
    # Parse input parameters from the event (HTTP request data)
    sender = os.environ.get("SENDER_EMAIL")
    recipient = os.environ.get("RECIPIENT_EMAIL")  
    subject = event.get("subject", "!D AI Chatbot Email")
    full_name = event.get("full_name", "Anonymous")
    phone_number = event.get("phone_number", "Not provided")
    user_email = event.get("user_email", "Not provided")
    message = event.get("message", "No content provided")
    composed_email = f"""
    <html>
    <body>
        <p>Hello !D Admin,</p>
        <p>This is a message from the !D website chatbot.</p>
        <p><strong>Details:</strong></p>
        <ul>
            <li><strong>Name:</strong> {full_name}</li>
            <li><strong>Phone Number:</strong> {phone_number}</li>
            <li><strong>User Email:</strong> {user_email}</li>
            <li><strong>Message:</strong> {message}</li>
        </ul>
    </body>
    </html>
    """  

    # Compose the email using SendGrid's helper
    email = Mail(
    from_email=Email(email=sender, name="!D Chatbot"),
    to_emails=To(email=recipient),
    subject=subject,
    html_content=Content("text/html", composed_email)
)
    
    try:
        # Retrieve API key from environment variable
        sg_client = SendGridAPIClient(os.environ.get("API_KEY"))
        response = sg_client.send(email)
        # Check response (for example, 202 is success in SendGrid API)
        if response.status_code == 202:
            return { "body": "Email sent successfully." }
        else:
            return { "body": f"SendGrid API returned status {response.status_code}", "status": response.status_code }
    except Exception as e:
        # Log and return the error
        if hasattr(e, 'body'):
            print("SendGrid Error Body:", e.body)
        return { "body": f"Error sending email: {str(e)}", "status": 500 }
