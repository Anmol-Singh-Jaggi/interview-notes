[Source](https://stackoverflow.com/a/26272833/1925388)

OAuth is a protocol with which a 3-party app can access your data stored in another website without your account and password. For a more official definition, refer to the Wiki or specification. 

Here is a use case demo:

1. I login to LinkedIn and want to connect some friends who are in my Gmail contacts. LinkedIn supports this.  It will request a secure resource (my gmail contact list) from gmail.  So I click this button:  
![Add Connection](https://i.stack.imgur.com/hSmux.png)  

2. A web page pops up, and it shows the Gmail login page, when I enter my account and password:  
![Add Connection](https://i.stack.imgur.com/3QvQo.png)  

3. Gmail then shows a consent page where I click "Accept":  
![Add Connection](https://i.stack.imgur.com/lQjip.png)  

4. Now LinkedIn can access my contacts in Gmail:  
![Add Connection](https://i.stack.imgur.com/ymoap.png)  

Below is a flowchart of the example above:

![Add Connection](https://i.stack.imgur.com/bt7k0.png)  

Step 1: LinkedIn requests a token from Gmail's Authorization Server.

Step 2: The Gmail authorization server authenticates the resource owner and shows the user the consent page. (the user needs to login to Gmail if they are not already logged-in)

Step 3: User grants the request for LinkedIn to access the Gmail data.

Step 4: the Gmail authorization server responds back with an access token.

Step 5: LinkedIn calls the Gmail API with this access token.

Step 6: The Gmail resource server returns your contacts if the access token is valid. (The token will be verified by the Gmail resource server)

You can get more from details about OAuth [here][1].


  [1]: http://helloowen.com/blog/Tech-What-is-OAuth.html


# Alternate explanation:

[Source](https://gist.github.com/mziwisky/10079157)

## The Problem
I’m a web app that wants to allow other web apps access to my users’ information, but I want to ensure that the user says it’s ok.
 
## The Solution
I can’t trust the other web apps, so I must interact with my users directly.  I’ll let them know that the other app is trying to get their info, and ask whether they want to grant that permission.  Oauth defines a way to initiate that permission verification from the other app’s site so that the user experience is smooth.  If the user grants permission, I issue an AuthToken to the other app which it can use to make requests for that user's info.
 
### Note on encryption
Oauth2 has nothing to do with encryption -- it relies upon SSL to keep things (like the client app’s shared_secret) secure.
 
## Example Scenario:
Gmail wants to allow some 3rd party app, PrettyMail, to do stuff with its users’ information.
 
```
Gmail stores server-side:      PrettyMail stores server-side:      Note: client_id tracks the user of the
  oauth_clients: [               client_id: ABC                    oauth privileges, i.e., PrettyMail or 
    pretty_mail: {               shared_secret: XYZ                other web app -- not the end-users
      client_id: ABC
      shared_secret: XYZ
    }, ...]
```
 
1. I visit PrettyMail and click “Login thru GMail”

2. PrettyMail responds REDIRECT gmail.com/oauth2/auth?client_id=ABC&redirect_uri=prettymail.com/oauth_response
  -- note: also common to include ‘scopes’ in query -- i.e., the scope of the information that PrettyMail is asking to access

3. gmail makes a session in which it stores provider (PrettyMail, based on client_id -- if client_id doesn’t refer to an authorized oauth_client, render an error) and redirect_uri and then responds:

    a. REDIRECT gmail.com/login (for a login form) if the user isn’t logged in, otherwise

    b. REDIRECT directly to step (4)

4. gmail shows a page saying “PrettyMail (got that from the aforementioned session) wants to access this, that, and the other thing (again, ‘scope’ of access was stored in the session) about your Gmail account.  Do you authorize?”  You click “yup” and gmail:

5. generates a one-time-use code that it associates with PrettyMail and the specified user and the requested scope (so it persists it until the next step) and REDIRECTs to the ‘redirect_uri’ it got in the first place, passing along that code: prettymail.com/oauth_response?code=big_long_thing

    Question: why not pass the AuthToken itself along at that step?  Answer: so gmail can ensure that PrettyMail is indeed the requester of the access -- so far, all the requests gmail has gotten have come directly from the user, and the only information that identified PrettyMail was its client_id, which isn’t “secret” (i.e. an attacker could guess it).  So GMail so far is confident that the user is ok with everything, but isn’t yet convinced that PrettyMail is really going to be the one using the Token.  That’s where the next request comes in, in which PrettyMail identifies itself by including the shared secret.
    
    Other Question: rather than redirecting to a URL containing the code as a param, why not just send the final AccessToken to PrettyMail right then and there?  Answer: (i’m guessing) the redirect basically “gives control” of the browser back to PrettyMail, so they can handle the request any way they want.

6. PrettyMail takes the code and directly (i.e., not via a REDIRECT in the user’s browser, but via a server-to-server request) queries GMail with both code and shared secret, to prove its identity: GET gmail.com/oauth2/token?client_id=ABC&client_secret=XYZ&code=big_long_thing

7. gmail verifies and then invalidates the code, and responds with an AccessToken, which PrettyMail can then use (until it expires) to make API requests on the user’s behalf (i.e., to get info about the user, and possibly to perform actions on behalf of the user, if that was in the agreed-upon ‘scope’ of the arrangement)