### Why we install CORS ?

Adding CORS headers allows your resources to be accessed on other domains.It’s important you understand the implications before adding the headers, since you could be unintentionally opening up your site’s private data to others.

### Why in middleware it's should be on top?
`CorsMiddleware` should be placed as high as possible, especially before any middleware that can generate responses such as Django’s CommonMiddleware or Whitenoise’s WhiteNoiseMiddleware. If it is not before, it will not be able to add the CORS headers to these responses.
Also if you are using `CORS_REPLACE_HTTPS_REFERER` it should be placed before Django’s `CsrfViewMiddleware`