
# ==========================================
# STAGE 1: Build the Go Binary
# ==========================================

FROM golang:1.22-alpine AS builder


# Set the working directory inside container

WORKDIR /app


# Copy dependency files first

COPY go.mod ./



# Copy the source code

COPY main.go .


# Build a statically linked Go Binary

RUN CGO_ENABLED=0 GOOS=linux go build -o server main.go


# ==========================================
# STAGE 2: Minimal Production Image
# ==========================================

FROM scratch


# Set the working directory in final image

WORKDIR /root/


# Copy the compiled binary from stage 1

COPY --from=builder /app/server .


# Export 8080

EXPOSE 8080


# Run the binary

ENTRYPOINT ["./server"]
