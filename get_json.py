# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session

PROXIES = { "http": "http://127.0.0.1:1080", "https": "https://127.0.0.1:1080" } 

consumer_key = 'K4NFmrmpF3DY7JBvvCOIJDG36N5DUokCMFPU9e1OivvUzJ4kdD'
consumer_secret = 'KLcEY6A2oVb6qS6xaLg1oe1FSsCjXw3iLDTukqKMnSw0YCmc6e'

def new_oauth():

	print('Retrieve consumer key and consumer secret from http://www.tumblr.com/oauth/apps')

	request_token_url = 'http://www.tumblr.com/oauth/request_token'
	authorize_url = 'http://www.tumblr.com/oauth/authorize'
	access_token_url = 'http://www.tumblr.com/oauth/access_token'

	# STEP 1: Obtain request token
	oauth_session = OAuth1Session(consumer_key, client_secret=consumer_secret)
	fetch_response = oauth_session.fetch_request_token(request_token_url)
	resource_owner_key = fetch_response.get('oauth_token')
	resource_owner_secret = fetch_response.get('oauth_token_secret')
	print("step 1 pass");

	# STEP 2: Authorize URL + Rresponse
	full_authorize_url = oauth_session.authorization_url(authorize_url)

	# Redirect to authentication page
	print('\nPlease go here and authorize:\n{}'.format(full_authorize_url))
	redirect_response = input('Allow then paste the full redirect URL here:\n')

	# Retrieve oauth verifier
	oauth_response = oauth_session.parse_authorization_response(redirect_response)

	verifier = oauth_response.get('oauth_verifier')

	# STEP 3: Request final access token
	oauth_session = OAuth1Session(
	    consumer_key,
	    client_secret=consumer_secret,
	    resource_owner_key=resource_owner_key,
	    resource_owner_secret=resource_owner_secret,
	    verifier=verifier
	)
	oauth_tokens = oauth_session.fetch_access_token(access_token_url)

	tokens = {
	    'consumer_key': consumer_key,
	    'consumer_secret': consumer_secret,
	    'oauth_token': oauth_tokens.get('oauth_token'),
	    'oauth_token_secret': oauth_tokens.get('oauth_token_secret')
	}

if __name__ == '__main__':

	new_oauth()