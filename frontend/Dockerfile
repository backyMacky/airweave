FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy application code
COPY . .

# Build and serve the application
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"] 