package main

import (
	"fmt"
	"net/http"
	"time"
)

func main() {
	// Root route providing system info and status
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		currentTime := time.Now().Format(time.RFC1123)
		fmt.Fprintf(w, "=== Welcome to DevOps App v2.0 ===\n")
		fmt.Fprintf(w, "Status: Running smoothly inside Docker\n")
		fmt.Fprintf(w, "Container Time: %s\n", currentTime)
	})

	// Dedicated health check endpoint
	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		fmt.Fprintln(w, `{"status": "UP"}`)
	})

	fmt.Println("Server initialized on port :8080...")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Printf("Server failed to start: %v\n", err)
	}
}
