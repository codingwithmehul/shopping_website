from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'mehul_secret_key'  # Required for flash messages

# 👉 Replace with your real Gmail & app password
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Google App Password (not normal password)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        sender_email = request.form['email']
        message = request.form['message']

        try:
            # Compose the email
            msg = EmailMessage()
            msg['Subject'] = f'New Message from {name}'
            msg['From'] = sender_email
            msg['To'] = EMAIL_ADDRESS
            msg.set_content(f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message}")

            # Send email using Gmail's SMTP
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash(f'Error sending message: {e}', 'danger')

        return redirect('/contact')

    return render_template('contact.html')

if __name__ == '__main__':
    # Accessible from other devices on your Wi-Fi
    app.run(host='0.0.0.0', port=5000, debug=True)
