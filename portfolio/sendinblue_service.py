import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from django.conf import settings

def send_contact_email(contact):
    # Configurer le client Brevo (Sendinblue)
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    # Contenu de l'email
    subject = "Nouveau message de contact"
    html_content = f"""
    <p>Vous avez reçu un nouveau message :</p>
    <p><strong>Message :</strong> {contact.message}</p>
    <p><strong>De :</strong> {contact.email}</p>
    """
    
    sender = {"name": "Recruteur", "email": "saad.mazouzi@esi.ac.ma"}  # Remplace par ton nom et e-mail
    to = [{"email": "saadmaazouzi580@gmail.com"}]  # Remplace par l'adresse email où tu souhaites recevoir le message

    email = sib_api_v3_sdk.SendSmtpEmail(to=to, sender=sender, subject=subject, html_content=html_content)

    try:
        api_instance.send_transac_email(email)
        print("Email de contact envoyé avec succès")
    except ApiException as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")

