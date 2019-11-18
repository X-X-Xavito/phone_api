# Phone Recharges

This a Django Rest Framework API for phone recharging.  It is possible to:

  - Create Companies and their products 
  - Create a recharge for a specific phone number

### Installation

The API requires [Python3](https://www.python.org/), [Django2](https://www.djangoproject.com/) and [Django Rest Framework](https://www.django-rest-framework.org/) and [Git](https://git-scm.com/) to run.

Clone this project: 

```sh
$ git clone https://github.com/X-X-Xavito/phone_api.git
```
Create a new virtual enviroment:
```sh
$ python3 -m venv myenv
```
And activate it:
```sh
$ source myenv/bin/activate
```
Go to the phone_api directory:
```sh
(myenv) ~$ cd phone_api/ 
```
And install the libraries in the requirements.txt file:
```sh
(myenv) ~$ pip install -r requirements.txt 
```
Then, lets connect our database:
```sh
(myenv) ~$ python manage.py makemigrations 
```
```sh
(myenv) ~$ python manage.py migrate --run-syncdb
```
And create a superuser:
```sh
(myenv) ~$ python manage.py createsuperuser 
```
And now you have all you need to the API.

### How to use
#### Companies and Products

This API works with HTTP requests and methods. So, for the proper use, we are going to use the [HTTPie](https://httpie.org/) program (already installed via requirements).

First, lets start the server
```sh
(myenv) ~$ python manage.py runserver 
```
Open another instance of the terminal and activate the virtual enviroment. And let's create a company:
In the new terminal, just type:
```sh
(myenv) ~$ http POST localhost:8000/CreateCompany/ company_id="vivo_11" -a xavito:12345
```
This is the HTTPie command: starts with the http, then the method, the url. 
Since it is a POST you need to pass the argument to the url. The -a argument is to use the credentials created as the super user.
The response should be:
```sh
HTTP/1.1 201 Created
Allow: POST, OPTIONS
Content-Length: 38
Content-Type: application/json
Date: Mon, 18 Nov 2019 01:02:35 GMT
Server: WSGIServer/0.2 CPython/3.6.8
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "company_id": "vivo_11",
    "products": []
}
```
Now, we can create some products to that company:
```sh
(myenv) ~$ http POST localhost:8000/vivo_11/CreateProduct/  product_id="vivo_10" value=10 -a xavito:12345
```
And the response, should be: 
```sh
HTTP/1.1 201 Created
Allow: POST, OPTIONS
Content-Length: 37
Content-Type: application/json
Date: Mon, 18 Nov 2019 01:14:15 GMT
Server: WSGIServer/0.2 CPython/3.6.8
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "product_id": "vivo_10",
    "value": 10.0
}
```
Let's create more products:
```sh
(myenv) ~$ http POST localhost:8000/vivo_11/CreateProduct/  product_id="vivo_20" value=20 -a xavito:12345
```
```sh
(myenv) ~$ http POST localhost:8000/vivo_11/CreateProduct/  product_id="vivo_50" value=50 -a xavito:12345
```

Great. Now, we will create another company and its products:
```sh
(myenv) ~$ http POST localhost:8000/CreateCompany/ company_id="claro_11" -a xavito:12345
```
```sh
(myenv) ~$ http POST localhost:8000/claro_11/CreateProduct/  product_id="claro_10" value=10 -a xavito:12345
```
```sh
(myenv) ~$ http POST localhost:8000/claro_11/CreateProduct/  product_id="claro_20" value=20 -a xavito:12345
```
```sh
(myenv) ~$ http POST localhost:8000/claro_11/CreateProduct/  product_id="claro_50" value=50 -a xavito:12345
```

To check all the companies and their products:
```sh
(myenv) ~$ http GET localhost:8000/CompanyProducts/ -a xavito:12345
```
The output should be:
```sh
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Content-Length: 309
Content-Type: application/json
Date: Mon, 18 Nov 2019 01:25:54 GMT
Server: WSGIServer/0.2 CPython/3.6.8
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

[
    {
        "company_id": "claro_11",
        "products": [
            {
                "product_id": "claro_10",
                "value": 10.0
            },
            {
                "product_id": "claro_20",
                "value": 20.0
            },
            {
                "product_id": "claro_50",
                "value": 50.0
            }
        ]
    },
    {
        "company_id": "vivo_11",
        "products": [
            {
                "product_id": "vivo_10",
                "value": 10.0
            },
            {
                "product_id": "vivo_20",
                "value": 20.0
            },
            {
                "product_id": "vivo_50",
                "value": 50.0
            }
        ]
    }
]
```
But, to check the products of a specific company:
```sh
(myenv) ~$ http GET localhost:8000/CompanyProducts/vivo_11/ -a xavito:12345
```
The output:
```sh
HTTP/1.1 200 OK
Allow: GET, DELETE, HEAD, OPTIONS
Content-Length: 151
Content-Type: application/json
Date: Mon, 18 Nov 2019 01:29:08 GMT
Server: WSGIServer/0.2 CPython/3.6.8
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "company_id": "vivo_11",
    "products": [
        {
            "product_id": "vivo_10",
            "value": 10.0
        },
        {
            "product_id": "vivo_20",
            "value": 20.0
        },
        {
            "product_id": "vivo_50",
            "value": 50.0
        }
    ]
}
```
To update a product:
```sh
(myenv) ~$ http PATCH localhost:8000/UpdateProduct/vivo_50/ value=100 -a xavito:12345
```
```sh
HTTP/1.1 200 OK
Allow: PUT, PATCH, OPTIONS
Content-Length: 38
Content-Type: application/json
Date: Mon, 18 Nov 2019 01:33:33 GMT
Server: WSGIServer/0.2 CPython/3.6.8
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "product_id": "vivo_50",
    "value": 100.0
}
```
If you want to delete a Product: 
```sh
(myenv) ~$ http DELETE localhost:8000/DeleteProduct/vivo_20/ -a xavito:12345
```
And check the company:
```sh
(myenv) ~$ http GET localhost:8000/CompanyProducts/vivo_11/ -a xavito:12345
```
```sh
HTTP/1.1 200 OK
Allow: GET, DELETE, HEAD, OPTIONS
Content-Length: 114
Content-Type: application/json
Date: Mon, 18 Nov 2019 01:44:52 GMT
Server: WSGIServer/0.2 CPython/3.6.8
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "company_id": "vivo_11",
    "products": [
        {
            "product_id": "vivo_10",
            "value": 10.0
        },
        {
            "product_id": "vivo_50",
            "value": 100.0
        }
    ]
}
```
Now, to delete an entire company:
```sh
(myenv) ~$ http DELETE localhost:8000/CompanyProducts/vivo_11/ -a xavito:12345
```
And check the companies:
```sh
(myenv) ~$ http GET localhost:8000/CompanyProducts/ -a xavito:12345
```
```sh
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Content-Length: 157
Content-Type: application/json
Date: Mon, 18 Nov 2019 01:47:26 GMT
Server: WSGIServer/0.2 CPython/3.6.8
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

[
    {
        "company_id": "claro_11",
        "products": [
            {
                "product_id": "claro_10",
                "value": 10.0
            },
            {
                "product_id": "claro_20",
                "value": 20.0
            },
            {
                "product_id": "claro_50",
                "value": 50.0
            }
        ]
    }
]
```
#### Phone recharges
The phone recharges only allows two methods: GET and POST.
To make a new phone recharge:
```sh
(myenv) ~$ http POST localhost:8000/PhoneRecharges/ company="claro_11" product="claro_10" value=10 phone_number="5511999999999" -a xavito:12345
```
```sh
HTTP/1.1 201 Created
Allow: POST, OPTIONS
Content-Length: 137
Content-Type: application/json
Date: Mon, 18 Nov 2019 01:57:35 GMT
Server: WSGIServer/0.2 CPython/3.6.8
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "company": "claro_11",
    "created_at": "2019-11-18T01:57:35.357138Z",
    "id": 1,
    "phone_number": "5511999999999",
    "product": "claro_10",
    "value": 10.0
}
```
So let's create a few more recharges:
```sh
(myenv) ~$ http POST localhost:8000/PhoneRecharges/ company="claro_11" product="claro_20" value=20 phone_number="5511999999999" -a xavito:12345
```
```sh
(myenv) ~$ http POST localhost:8000/PhoneRecharges/ company="claro_11" product="claro_20" value=20 phone_number="5511911111111" -a xavito:12345
```
```sh
(myenv) ~$ http POST localhost:8000/PhoneRecharges/ company="claro_11" product="claro_10" value=10 phone_number="5511922222222" -a xavito:12345
```
There's two ways of getting the phone recharges: filtering them with the phone number or the id.
To use the phone number: 
```sh
(myenv) ~$ http GET localhost:8000/PhoneRecharges/5511999999999/ -a xavito:12345
```
And you wil get all the phone recharges for that phone number:
```sh
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Content-Length: 277
Content-Type: application/json
Date: Mon, 18 Nov 2019 02:05:51 GMT
Server: WSGIServer/0.2 CPython/3.6.8
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

[
    {
        "company": "claro_11",
        "created_at": "2019-11-18T01:57:35.357138Z",
        "id": 1,
        "phone_number": "5511999999999",
        "product": "claro_10",
        "value": 10.0
    },
    {
        "company": "claro_11",
        "created_at": "2019-11-18T02:03:57.041795Z",
        "id": 2,
        "phone_number": "5511999999999",
        "product": "claro_20",
        "value": 20.0
    }
]
```
Or type the id of the recharge:
```sh
(myenv) ~$ http GET localhost:8000/PhoneRecharges/id/3/ -a xavito:12345
```
```sh
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Content-Length: 137
Content-Type: application/json
Date: Mon, 18 Nov 2019 02:11:39 GMT
Server: WSGIServer/0.2 CPython/3.6.8
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "company": "claro_11",
    "created_at": "2019-11-18T02:04:20.753414Z",
    "id": 3,
    "phone_number": "5511911111111",
    "product": "claro_20",
    "value": 20.0
}
```