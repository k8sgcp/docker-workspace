# ==========================================
# Stage 1: Build Stage (JDK + Maven)
# ==========================================

FROM gradle:8.14-jdk17 AS builder

WORKDIR /app


# Copy build configuration files first for layer caching
COPY build.gradle settings.gradle ./
COPY gradle ./gradle


# Copy source code and build the executable JAR
COPY src ./src
RUN gradle bootJar --no-daemon


# ==========================================
# Stage 2: Runtime Stage (JRE only)
# ==========================================
FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

# Create a non-root system user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup


# Copy the built JAR from the Gradle build output folder
COPY --from=builder /app/build/libs/*.jar app.jar


# Change ownership to non-root user
RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
