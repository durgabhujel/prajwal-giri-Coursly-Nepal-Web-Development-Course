# Password Change and Reset
Let's add password change and reset functionality to our project.

## Password Change
Django Provides a built-in method for changing a user's password, located at
http://127.0.0.1:8000/accounts/password_change/

## Customizing Password Change
Django has already created the views and URLs for password change and reset.
We only need to add the templates and forms.
1. Create two new templates in the templates/registration directory:
    * password_change_form.html
    * password_change_done.html
```
#templates/registration/password_change_form.html

{% extends 'base.html' %}
{% block title %}Password Change{% endblock title %}
{% block content %}
<h1 class="hero-title">Password change</h1>
<p class="">Please enter your old password, for security's sake, and then enter
your new password twice so we can verify you typed it in correctly.</p>
<form method="POST" class="form">
{% csrf_token %}
{{ form.as_p }}
<button class="btn" type="submit"
value="Change my password">Change my password</button>
</form>
{% endblock content %}
``` 

```
#templates/registration/password_change_done.html
{% extends 'base.html' %}
{% block title %}Password Change Successful{% endblock title %}
{% block content %}
<h1 class="hero-title">Password change successful</h1>
<p>Your password was changed.</p>
{% endblock content %}

```


2.Go ahead and refresh the page at http://127.0.0.1:8000/accounts/password_change/ to see
our changes.
3.Now you can set a link to the password change page in the navbar
4.And then set the URL for change password and create a password change view to render the password change template.

## Password Reset
Password reset handles the common case of users forgetting their passwords.
Django already provides a default implementation of password reset.
The only thing we need to do is tell Django how to send emails.
In production, we will use SendGrid to send emails.
In development, we will use the built-in Django email backend.

1. Update the settings.py file to include the django email backend.
```
# config/settings.py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

```
2.That's it! Now we can send emails to users. Django will use the console backend to send emails in development.

3.Navigate to the http://127.0.0.1:8000/accounts/password_reset/ to view the default password reset page and enter your email address.
4.Make sure the email address you enter matches one of your user accounts. Upon submission
you’ll then be redirected to the password reset done page at:
http://127.0.0.1:8000/accounts/password_reset/done/

5.Since we’ve told Django to send emails to the command line
console, the email text will now be there. This is what I see in my console.
```
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 8bit
Subject: Password reset on 127.0.0.1:8000
From: webmaster@localhost
To: user1@gmail.com
Date: Wed, 26 Jan 2022 08:33:24 -0000
Message-ID: <164318600421.30899.10751158105551357115@fedora-35>


You're receiving this email because you requested a password reset for your user account at 127.0.0.1:8000.

Please go to the following page and choose a new password:

http://127.0.0.1:8000/accounts/reset/Mg/azunro-91a1ac7e0c64437aabb74d4e568b34b3/

Your username, in case you’ve forgotten: user1

Thanks for using our site!

The 127.0.0.1:8000 team
```
Your email text should be identical except for three lines:
• the “To” on the sixth line contains the email address of the user
• the URL link contains a secure token that Django randomly generates for us and can be
used only once
• Django helpfully reminds us of our username



6. Now enter the new password twice and submit the form.

## Custom Templates
Now will create custom templates for password reset as well.
We will create fours new templates in the templates/registration directory:
1.Create 4 new templates in the templates/registration directory:
    * password_reset_form.html
    * password_reset_done.html
    * password_reset_confirm.html
    * password_reset_complete.html


URL -> http://127.0.0.1:8000/accounts/password_reset/
Template
```
#templates/registration/password_reset_form.html

{% extends 'base.html' %}
{% block title %}Forgot Your Password?{% endblock title %}
{% block content %}
<h1 class="hero-title">Forgot your password?</h1>
<p class="blog-card-subtitle">Enter your email address below, and we'll email instructions
for setting a new one.</p>
<form method="POST" class="form">
{% csrf_token %}
{{ form.as_p }}
<button class="btn" type="submit"
value="Send me instructions!">Send</button>
</form>
{% endblock content %}

```
```
#templates/registration/password_reset_done.html
{% extends 'base.html' %}
{% block title %}Email Sent{% endblock title %}
{% block content %}
<h1 class="hero-title">Check your inbox.</h1>
<p class="blog-card-subtitle">We've emailed you instructions for setting your password.
You should receive the email shortly!</p>
{% endblock content %}

```


In the command line grab the URL link from the email outputted to the console and you’ll see
the following.

```
#templates/registration/password_reset_confirm.html

{% extends 'base.html' %}
{% block title %}Enter new password{% endblock title %}
{% block content %}
<h1 class="title">Set a new password!</h1>
<form method="POST" class="form">
{% csrf_token %}
{{ form.as_p }}
<button class="btn" type="submit" value="Change my password">Change my password</button>
</form>
{% endblock content %}

```

You can view it at http://127.0.0.1:8000/accounts/reset/done/.
``` 
#templates/registration/password_reset_complete.html

{% extends 'base.html' %}
{% block title %}Password reset complete{% endblock title %}
{% block content %}
<h1 class="hero-title">Password reset complete</h1>
<p class="blog-card-subtitle">Your new password has been set. You can log in now on the
<a href="{% url 'login' %}" class="nav-links underline">Log In page</a>.</p>
{% endblock content %}

```
 
2. That’s it! Now we can send emails to users to reset password. Django will use the console backend to send emails in development.

