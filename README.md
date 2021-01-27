# Dash Embedded

### Embedding in a simple React application
This example demonstrates embedding a simple [Dash Enterprise template application](http://localhost:8000/Docs/templates/sample-app) in a basic React application using [`create-react-app`](https://create-react-app.dev/docs/getting-started/).
This directory contains the source code for the React example in `react-app` and a directory `dash-app` containing the example Dash applications. 
> Note: This example requires python and node as well as React version > 16.2 (16.13 recommended).

##### Run the Dash Application
There are two Dash applications in `./dash-app`: the most simple example `hello_world.py` and the Dash application from the [Dash Enterprise template documentation](http://localhost:8000/Docs/templates/). To make these applications embeddable, we've added `plugins=[dash_embedded.Embeddable(...)]` to the `dash.Dash` constructor as per the official [usage](/Docs/embedded-middleware/usage).

1. Ensure that you have mapped localhost to dash.tests as per the [usage](http://localhost:8000/Docs/embedded-middleware/usage) chapter.
2. Update `Embeddable(origins=['https://<your-host-application-hostname>'])`  in `app.py` with the name of your host application's host name.
3. `pip install -r requirements.txt` to install the python requirements to run the Dash application. This includes the open source `dash` library as well as the proprietary packages `dash-design-kit` and `dash-embedded` which will be downloaded from the Dash Enterprise server.
4. Enter the dash-app folder: `cd dash-app`
5. Run `python index.py` to run the application locally (or `python hello_world.py` for the minimal example). You can verify the app is running locally at [http://dash.tests:8050](http://dash.tests:8050).

##### Run the Host Application
This React application was created with `npx create-react-app` then modified slightly for compatibility with Dash Embedded. The modifications include: the import of the `dash-embedded-component` tarball and the modification of the `index.js` file to remove `React.StrictMode`. 
1. Enter the react app folder: `cd react-app`
2. `npm install` note: this will create a node_modules folder 
3. Make sure that in `App.js` your `url_base_pathname` url points to the dash app you want to embed
4. `BROWSER=none npm start` this will start the application on your localhost. Visit the application at [http://dash.tests:3000](http://dash.tests:3000). The command will print out http://localhost:3000 but you must visit http://dash.tests:3000 in order for the CORS requests to the embedded Dash app to work.
