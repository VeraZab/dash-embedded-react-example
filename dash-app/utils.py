import os

# Specify the deployed URL path where the Dash application will be embedded 
# on the host application. 
# For example, if the Dash app is embedded on https://acme.com/analytics, then this would be '/analytics' 
# If the Dash app is embedded on the "home page" at https://acme.com/, then this would be `/`
HOST_APP_PATHNAME = '/'

# work arounds for handling the redirect of pages in dash-app
def get_host_relative_path(path):
    """
     Return a path that is prefixed with `HOST_APP_PATHNAME`.
     Use this method when specifying the `href` in `dcc.Link` or `html.A`.
     ```
     # Consider HOST_APP_PATHNAME='/analytics'
     >>> get_host_relative_path('/weekly-report')
     '/analytics/weekly-report'
     >>> get_host_relative_path('/weekly-report/monday/')
     'analytics/weekly-report/monday'
     ```     
     """
    if HOST_APP_PATHNAME == "/" and path == "":
        return "/"
    elif HOST_APP_PATHNAME != "/" and path == "":
        return HOST_APP_PATHNAME
    elif not path.startswith("/"):
        raise Exception(
            "Paths that aren't prefixed with a leading / are not supported.\n"
            + "You supplied: {}".format(path)
        )
    return "/".join([HOST_APP_PATHNAME.rstrip("/"), path.lstrip("/")])

def strip_host_relative_path(path):
    """
     Strip the `HOST_APP_PATHNAME` from the beginning of the path.
     Use this method when parsing `pathname` supplied by the `dcc.Location` component.
     ```
     # Consider HOST_APP_PATHNAME='/analytics'
     >>> strip_host_relative_path('/analytics/weekly-report')
     'weekly-report'
     >>> strip_host_relative_path('/analytics/weekly-report/monday/')
     'weekly-report/monday'
     >>> strip_host_relative_path(None)
     None
     ```
     """
    if path is None:
        return None
    elif (
        HOST_APP_PATHNAME != "/" and not path.startswith(HOST_APP_PATHNAME.rstrip("/"))
    ) or (HOST_APP_PATHNAME == "/" and not path.startswith("/")):
        raise Exception(
            "Paths that aren't prefixed with a leading "
            + "HOST_APP_PATHNAME are not supported.\n"
            + "You supplied: {} and HOST_APP_PATHNAME was {}".format(
                path, HOST_APP_PATHNAME
            )
        )
    elif HOST_APP_PATHNAME != "/" and path.startswith(HOST_APP_PATHNAME.rstrip("/")):
        path = path.replace(
            # handle the case where the path might be `/my-dash-app`
            # but the HOST_APP_PATHNAME is `/my-dash-app/`
            HOST_APP_PATHNAME.rstrip("/"),
            "",
            1,
        )
        return path.strip("/")
    else: return path.strip("/")

def embedded_asset_url(resource):
    """
    Return a complete URL that specifies the location of a file (resource) inside
    the assets folder of your Dash app.
    Use this method when constructing any path that uses a file from assets, like the `src` attribute of
    `html.Img`
    ```
    # If the Dash app was deployed on a Dash Enterprise instance with the domain dash.acme.com
    # and the name of the app was "weekly-report"
    >>> embedded_asset_url('logo.png')
    https://dash.acme.com/weekly-report/assets/logo.png
    ```
    """
    if 'DASH_DOMAIN_BASE' in os.environ:
        # Assume the app is deployed or in a workspace
        if os.getenv('DASH_ENTERPRISE_ENV', '').upper() == 'WORKSPACE':
            # Get asset URL from the app running inside the workspace
            asset_str = 'https://{domain}/Workspaces/view/{app_name}/assets/{resource}'
        else:
            asset_str = 'https://{domain}/{app_name}/assets/{resource}'
        return asset_str.format(
            domain=os.environ['DASH_DOMAIN_BASE'],
            app_name=os.environ['DASH_APP_NAME'],
            resource=resource
        )
    # Assume running on localhost:8050
    # This will not work when running locally with gunicorn unless
    # you use `gunicorn app:server -b localhost:8050`
    return 'http://localhost:8050/assets/{resource}'.format(
        resource=resource
    )
