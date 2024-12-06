# ASP.Net Core Middleware Check

## Summary

This uses reflection to evaluate the registered middleware pipeline fpr ASP.Net Core.

```csharp
    //Stage
    var config = new ConfigurationBuilder()
        .AddJsonStream(this.GetResourceStream("appsettings.json"))
        .Build();

    var properties = new Dictionary<string, object>();

    var serviceCollection = new ServiceCollection();
    serviceCollection.AddSingleton<IConfiguration>(_ => config);


    //Mock
    var mock = new MockRepository(MockBehavior.Strict);
    var mockWebHostEnvironment = mock.Create<IWebHostEnvironment>(MockBehavior.Loose);
    var mockHostEnvironment = mock.Create<IHostingEnvironment>(MockBehavior.Loose);
    var mockDiagnosticListener = mock.Create<DiagnosticListener>(MockBehavior.Loose, "test");
    var mockFeatureCollection = mock.Create<IFeatureCollection>();


    mockFeatureCollection.Setup(i => i.Get<IServerAddressesFeature>()).Returns((IServerAddressesFeature)null);
    serviceCollection.AddSingleton(mockHostEnvironment.Object);
    serviceCollection.AddSingleton(mockWebHostEnvironment.Object);
    serviceCollection.AddSingleton(mockDiagnosticListener.Object);

    //Test
    var service = new Startup(config);
    service.ConfigureServices(serviceCollection);

    var serviceProvider = serviceCollection.BuildServiceProvider();
    var applicationBuilder = ActivatorUtilities.CreateInstance<ApplicationBuilder>(serviceProvider);
    applicationBuilder.Properties["server.Features"] = mockFeatureCollection.Object;

    service.Configure(applicationBuilder, mockWebHostEnvironment.Object);

    var def = applicationBuilder.GetType();
    var middlewarePipeline = from field in def.GetFields(BindingFlags.NonPublic | BindingFlags.Instance)
                                where field.FieldType == typeof(IList<Func<RequestDelegate, RequestDelegate>>)
                                let value = field.GetValue(applicationBuilder)
                                let list = (IList<Func<RequestDelegate, RequestDelegate>>)value
                                from chainLink in list
                                let middlewareField = chainLink.Target.GetType().GetField("middleware")
                                let middleware =(Type) middlewareField.GetValue(chainLink.Target)
                                select middleware;

    foreach(var mw in middlewarePipeline.Select((v,i)=> new { Order = i, Name = v.Name,  } ))
    {
        this.TestContext.WriteLine(mw.ToString());
    }

    //Assert
    Assert.IsTrue(middlewarePipeline.Contains(typeof(OAuthAuthorizationMiddleware)), $"{nameof(OAuthAuthorizationMiddleware)} is not registered");

    //Verify
    mock.Verify();
```