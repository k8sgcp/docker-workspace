# Build Stage (Compile static binary)

FROM golang:1.22-alpine as builder
WORKDIR /app
COPY go.mod ./
RUN go mod download
COPY . .



# CGO_ENABLED=0 builds a statically linked binary (no dynamic C libraries)
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-w -s" -o main .


# # Production Stage (Ultra-minimal runtime)
FROM scratch
WORKDIR /
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /app/main /main
EXPOSE 8080
ENTRYPOINT ["/main"]



