
# Small Azure app to steal Fragment Parameters

This is a minimal Flask app that can be deployed to Azure App Service on Linux which can be used to catch OAuth redirects. 


Example deploy using Azure Cli:

```
az webapp up --sku F1 --name nameofthing
```

The `nameofthing` gets appended to `.azurewebsites.net` and also gives SSL and all the goodness. 

To get the Tokens and codes that I am sure will be flying in, make sure to setup logging on the app service so that you can view weblogs and the service logs.

The code gets printed to stdout by the application which is viewable in the logs. 