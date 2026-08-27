# --- Stage 1: Build Stage ---

FROM eclipse-temurin:17-jdk-alpine AS builder


# Setting up work directory

WORKDIR /app


# Copy source code and compile

COPY Main.java .
RUN javac Main.java && jar cfe app.jar Main Main.class


# # --- Stage 2: Runtime Stage ---

FROM eclipse-temurin:17-jre-alpine

WORKDIR /app


# Create a non-root user and group for security best practices

RUN addgroup -S appgroup && adduser -S appuser -G appgroup


# Copy compiled JAR from builder stage

COPY --from=builder /app/app.jar /app/app.jar


# Set ownership to non root user

RUN chown -R appuser:appgroup /app


USER appuser

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]


