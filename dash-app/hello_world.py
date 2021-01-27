import dash
from dash_html_components import Div
from dash_embedded import Embeddable
app = dash.Dash(
    plugins=[Embeddable(origins=['https://<your-host-application-hostname>', r'^.+dash.tests(:\d+)?'])]
)

# Origins can be a string or a regex. 
# Flask Cors' implementation of the recognition of a string vs a regex is a little tricky, but the rough rules are: 
# - if our string contains one of these characters `['*', '\\', ']', '?', '$', '^', '[', ']', '(', ')']`, it will be recognized as a
#   regex, and Python's `re.match` rule will be used to evaluate whether or not the requesting origin is allowed access. `re.match` matches from
#   the start of a string, so if you provide a regex that does not match the beginning of the origin string, it will be refused.
# - if you provide a string that doesn't contain the above characters, an exact, non case sensitive, origin match will be made to determine 
#   if requesting origin is allowed access.
# - you can set '*' as your origin, and this will allow all origins to access your app, but this is a [security vulnerability](https://blog.securelayer7.net/owasp-top-10-security-misconfiguration-5-cors-vulnerability-patch/)

app.layout = Div(['Hello from Dash!'])
app.run_server(debug=True)
