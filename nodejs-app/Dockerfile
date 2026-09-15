# ==========================================
# Stage 1: Build & Dependencies
# ==========================================
FROM node:20-alpine AS builder

WORKDIR /app

# Copy dependency manifests first to leverage Docker layer caching
COPY package*.json ./

# Install ALL dependencies (including devDependencies needed for build/testing)
RUN npm ci

# Copy application source code
COPY . .

# Optional: Run build step if using TypeScript or bundlers (e.g., npm run build)
# RUN npm run build

# Prune devDependencies to keep the production node_modules minimal
RUN npm prune --production

# ==========================================
# Stage 2: Minimal Production Runtime
# ==========================================
FROM node:20-alpine AS runner

WORKDIR /app

# Set production environment
ENV NODE_ENV=production

# Run as non-root user for security (built into Alpine node image)
USER node

# Copy dependencies and built assets from builder stage
COPY --chown=node:node --from=builder /app/package*.json ./
COPY --chown=node:node --from=builder /app/node_modules ./node_modules
COPY --chown=node:node --from=builder /app/src ./src

# Expose app port
EXPOSE 3000

# Use node directly (avoids npm consuming signals like SIGTERM)
CMD ["node", "src/index.js"]
