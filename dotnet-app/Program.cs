var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => new { Status = "Healthy", Message = "C# .NET Core Service Running in Docker!" });

app.Run();
