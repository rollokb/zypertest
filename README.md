# Zyper Test

This is a solution to the test:

        https://gist.github.com/AndreaOrru/9ac5c2a67527dfbca8141dae3198fe3e


# Rundown

Django by default is great for HTML forms based websites. 
It can be good for APIs to, but in my view has too many
'batteries included'. This is a very stripped down django
application with only one application `zyper.images` installed.

# Setup

Python3 or greater. Docker to setup rabbitmq.

        pip install requirements.txt
        python manage.py migrate
        docker run -d --name rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management
        DEBUG=True AWS...=<aws creds> python manage.py runserver


# Usage 

List:

        curl localhost:8000/images/

        [{
                "id": 17,
                "file_thumb": null,
                "file_original": "https://zypertest.s3.amazonaws.com/Screenshot_from_2019-01-30_22-13-10.png",
                "name": "'test'",
                "created_at": "2019-02-01T16:01:01.150386Z"
        }]

Instance:
        curl localhost:8000/images/1/

Post:

        curl -X POST \
             http://localhost:8000/images/ \
             -H 'Content-Type: application/x-www-form-urlencoded' \
             -H 'cache-control: no-cache' \
             -H 'content-type: multipart/form-data; boundary=Boundry' \
             -F 'name='\''test'\''' \
             -F 'file_original=@/path/to/file.png'


# Testing

        pip install requirements_test.txt
        pytest
