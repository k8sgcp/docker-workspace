FROM nginx:alpine

# Copy custom reverse proxy config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy web page
COPY index.html /usr/share/nginx/html/

EXPOSE 80
