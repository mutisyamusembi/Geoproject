FROM tutum/nginx

RUN rm /etc/nginx/sites-enabled/default

COPY sites-enabled/ /etc/nginx/sites-enabled

COPY sites-enabled/default.conf /etc/nginx/conf.d/default.conf