from main import app

sample = {
    "name": "new cafe",
    "map_url": "https://goo.gl/maps/DWnwaeeiwdYsBkEH9",
    "img_url": "https://lh3.googleusercontent.com/p/AF1QipN-C650VmJ1XZhzOIBTg1bUu3_to_GHpyrmUplt=s0",
    "loc": "noida",
    "seats": "40+",
    "sockets": "1",
    "toilet": "0",
    "wifi": "1",
    "calls": "1",
    "coffee_price": "$20",
}

with app.test_client() as c:
    resp1 = c.post('/add', data=sample)
    print('First POST ->', resp1.status_code, resp1.get_json())

    resp2 = c.post('/add', data=sample)
    print('Second POST ->', resp2.status_code, resp2.get_json())
