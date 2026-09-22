# ==========================================
# STAGE 1: Build & Publish
# ==========================================
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Step 1: Copy project file and restore dependencies
# Leveraging Docker layer caching so restores only re-run when dependencies change
COPY MyDotnetApp.csproj ./
RUN dotnet restore

# Step 2: Copy remaining source code and publish release build
COPY . ./
RUN dotnet publish -c Release -o /app/publish --no-restore

# ==========================================
# STAGE 2: Minimal Chiseled Runtime
# ==========================================
# Using Microsoft's Chiseled (distroless) Ubuntu-based runtime for security & minimal footprint
FROM mcr.microsoft.com/dotnet/aspnet:8.0-jammy-chiseled AS final
WORKDIR /app

# Copy compiled binaries from the build stage
COPY --from=build /app/publish .

# Expose HTTP port (default non-root port for modern .NET containers is 8080)
EXPOSE 8080

# Configure non-root container environment
USER app

ENTRYPOINT ["dotnet", "MyDotnetApp.dll"]
