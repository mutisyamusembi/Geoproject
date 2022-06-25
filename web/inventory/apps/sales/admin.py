from django.contrib import admin
from .models import Product, Category, Order, OrderItem

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)



#  location / {
#      return 301 https://127.0.0.1$request_uri;
#  }
#  server {
#      listen 443 default_server ssl;
#      listen [::]:443 ssl;
#      server_name 127.0.0.1;
#      ssl_certificate /etc/nginx/ssl/live/127.0.0.1/fullchain.pem;
#      ssl_certificate_key /etc/nginx/ssl/live/127.0.0.1/privkey.pem;
#      location / {
#          proxy_pass http://web:8000;
#          proxy_set_header Host $host;
#          proxy_set_header X-Real-IP $remote_addr;
#          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#      }
#  }