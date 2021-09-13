import structlog
from auth.application.usecases import refresh_token_usecase
from auth.application.usecases.login_user import login_user
from auth.presentation.schemas import RefreshTokenIn
from fastapi import APIRouter, HTTPException
from starlette.requests import Request
from starlette.responses import HTMLResponse

log = structlog.get_logger()
router = APIRouter()


@router.post("/login", name="auth:login")
@router.post("/login/", name="auth:login", include_in_schema=False)
async def login(request: Request):
    """
    Social login with Google.
    """

    body = await request.json()
    auth_code = body["token"]

    try:
        response = login_user(auth_code=auth_code)
    except ValueError as e:
        return HTTPException(status_code=400, detail=str(e))
    return response


@router.post("/refresh_token", name="auth:refresh_token")
@router.post("/refresh_token/", name="auth:refresh_token", include_in_schema=False)
async def refresh_token(refresh_token: RefreshTokenIn):
    """
    Refresh access token
    """
    try:
        response = refresh_token_usecase(refresh_token.refresh_token)
    except ValueError as e:
        raise HTTPException(status_code=400, detail="User does not exists")
    return response


google_login_javascript_client = f"""<!DOCTYPE html>
<html itemscope itemtype="http://schema.org/Article">
<head>
    <meta charset="UTF-8">
    <meta name="google-signin-client_id" content="42161830547-2tmeb3hsacdf5ri1eujvc9a2s105m629.apps.googleusercontent.com">
    <title>Google Login</title><script src="https://apis.google.com/js/platform.js" async defer></script>
    <body>
    <div class="g-signin2" data-onsuccess="onSignIn"></div>
    <script>function onSignIn(googleUser) {{
  
  var id_token = googleUser.getAuthResponse().id_token;
    var xhr = new XMLHttpRequest();
xhr.open('POST', '/api/login');
xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8"');
xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
xhr.setRequestHeader('X-Google-OAuth2-Type', 'client');
xhr.onload = function() {{
   console.log('Signed in as: ' + xhr.responseText);
}};
xhr.send(JSON.stringify({{"token": id_token}}));
}}</script>
<div><br></div>
<a href="#" onclick="signOut();">Sign out</a>
<script>
  function signOut() {{
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {{
      console.log('User signed out.');
    }});
  }}
</script>
</body>
</html>"""


@router.get("/google_login_client", tags=["security"])
def google_login_client():

    return HTMLResponse(google_login_javascript_client)
