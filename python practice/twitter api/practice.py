import urllib.request, urllib.parse, urllib.error
import oauth
import hidden

def augment(url, parameters):
    secrets = hidden.oauth()
    conusmer = oauth.OAuthConsumer(secrets['consumer_key'],secrets['consumer_secrets'])
    token = oauth.oauthToken(secrets['token_key'],secrets['token_secrets'])
    oauth_request = oauth.OAuthRequest.form_consumer_and_token(consumer, token=token, http_method='GET', http_url=url, parameters='parameters')
    oauth.request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
    return oatuh.request.to_url()