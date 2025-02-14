# IOC Wrapper for .Net

## Features

- Redirect all requests from IServiceProvider
- By intercepting ISerivceProvide the option to not register explicitly will be possible
- Using a code generator it would be possible to ensure that all  classes are correctly defined or registered
- DispatchProxy allows for controlling interception on calls to any class
- Creating an interface for proxies classes would allow for selection of actual inner class
- Interceptors could be added directly to interface classes allowing for aspect oriented programming
- Intercepting Task functions would allow for dispatch redirection… you could serialize the request, pass it off to a Queue and return coordination key
- Using mef? Is it possible to dynamically scan deployed assemblies to allow for dispatch?
- Use code generators to create host.json and do your own dotnet 5 wrapper for azure functions?
- Is it possible to recompose queries from different dB context as long as they share a connection string?
- It it possible to use code generators to db context from database schema?
- Do data access security declaratively though attributes on  models and parameters?
- Can transaction scope be controlled declaratively? Is it possible to create a global scope then opt out explicitly?

## Links

- https://stackoverflow.com/questions/14341782/cross-database-querying-in-ef
- https://www.tabsoverspaces.com/233841-how-entity-framework-core-query-cache-works

## Architecture

    Post -> Queue -> Authorize -> Persist & Emit
    Receive -> 
    Authenticate -> Verb(payload) -> Authenticate -> Queue -> Translate,Emit
