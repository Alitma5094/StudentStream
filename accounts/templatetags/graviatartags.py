from django import template
import hashlib

register = template.Library()

@register.filter
def gravatar_url(email):
    default_image_url = "https://example.com/default_avatar.jpg"  # Provide a default image URL here

    # Generate the MD5 hash of the email
    email_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()

    # Build the Gravatar URL
    gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}?d={default_image_url}"

    return gravatar_url