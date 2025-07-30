## Task Overview

A product management team needs to efficiently retrieve user lists filtered by role (e.g., admin, customer) and status (e.g., active, inactive) from their internal user directory. Current endpoints do not combine filters correctly, resulting in incorrect results and frustrating end users. Your task is to implement a FastAPI backend with PostgreSQL that supports accurate multi-parameter filtering for user listings, ensuring robust backend logic and proper API design.

## Guidance

- Use environment variables for all sensitive database credentials and connection strings
- Structure your project into routers, models, services, core, and db modules for maintainability
- Apply async/await patterns for all database interactions to ensure scalability
- Use SQLAlchemy ORM for data modeling and query construction
- Ensure query parameters for filtering are handled with logical AND semantics
- Handle missing or invalid parameters with appropriate error responses
- Containerize both API and database using Docker and Docker Compose
- Use Pydantic models for all request and response validation
- Implement proper error handling and status code returns
- Ensure code is clean, modular, and well organized

## Objectives

- Implement API endpoints that allow clients to filter users by both role and status
- Ensure that when both parameters are provided, only users matching both are returned
- Integrate SQLAlchemy ORM and async session management for database operations
- Employ Pydantic models for response serialization
- Use environment-based configuration for database credentials and connection
- Set up Docker and Docker Compose for full stack deployment
- Provide robust error handling and clear HTTP responses

## How to Verify

- Start the services using Docker Compose and confirm the API is accessible
- Create multiple users with different roles and statuses in the database (manually or via migrations)
- Query the users endpoint with different combinations of role and status parameters
- Check that only users matching both parameters are returned
- Confirm that missing or invalid filters return correct error codes or empty lists
- Review OpenAPI documentation to ensure models and endpoints are described correctly
- Verify logs for correct query execution and no unhandled errors