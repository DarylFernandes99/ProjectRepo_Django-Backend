# ProjectRepo_Django-Backend
This repository consists of Backend for the ProjectRepo(<a href="https://github.com/DarylFernandes99/ProjectRepo">Link</a>) website. The backend is developed on Django and Rest API. It consists of three Projects
<ul>
  <li>Colorize Image</li>
  <li>Low-Light Image Enhancement using GAN</li>
  <li>Phrase based Poem Generation</li>
</ul>

<h4>Steps to run:</h4>
<ol>
  <li>Clone both this and ProjectRepo repository using "git clone <git url>"</li>
  <li>Paste the Django secret key in Keras_models>randomKey.txt file</li>
  <li>Add model links to colorize, llie, poem > models.py</li>
  <li>Add email id and pwd of mail account in the keras_models>settings.py, if you want the feedback form to send a mail.</li>
  <li>Run "python manage.py makemigrations"</li>
  <li>Run "python manage.py migrate"</li>
  <li>Run "python manage.py createsuperuser"</li>
  <li>FInally run "python manage.py runserver"</li>
</ol>
