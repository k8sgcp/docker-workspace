# --- STAGE 1: Build & Publish ---
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS builder
WORKDIR /src

# Copy project file and restore dependencies (Optimizes Docker Layer Caching)
COPY *.csproj ./
RUN dotnet restore

# Copy remaining source code and publish release build
COPY . ./
RUN dotnet publish -c Release -o /app/publish /p:UseAppHost=false

# --- STAGE 2: Lightweight Production Runtime ---
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final
WORKDIR /app

# Copy published binaries from the builder stage
COPY --from=builder /app/publish .

# Set non-root user for container security
USER app

EXPOSE 8081
ENTRYPOINT ["dotnet", "dotnet-app.dll"]
