# ---- Build stage ----
FROM golang:1.22-alpine AS builder

WORKDIR /app

# Copy dependency files first (optimizes layer caching)
COPY go.mod ./

RUN go mod download


# Copy source code and build a statically linked binary
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o main .

# ---- Runtime stage ----
FROM alpine:latest

WORKDIR /app


# Copy the compiled binary from the builder stage
COPY --from=builder /app/main .

EXPOSE 8080
CMD ["./main"]
