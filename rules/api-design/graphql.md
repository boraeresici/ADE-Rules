---
id: "graphql"
title: "GraphQL API Design"
description: "Guidelines for designing GraphQL APIs, focusing on client-driven queries, a strong type system, and avoiding over-fetching."
tags: ["api", "graphql", "schema"]
severity: "high"
applies_to: ["backend", "frontend", "api"]
automation_potential: ["graphql-validation", "code-review"]
suggested_tools: ["Apollo Server", "GraphQL Playground", "GraphQL Code Generator"]
related_rules: ["restful-api", "grpc", "api-selection-process"]
---

GraphQL is an API query language and runtime that allows clients to query exactly the data they need.

### Core Principles:
1. Use a single endpoint.
2. Create client-driven queries.
3. Use a strong type system.
4. Effectively query relational data.
5. Be independent of the data source with resolver functions.

**Rationale:** GraphQL addresses the over-fetching and under-fetching problems common in REST APIs by allowing clients to specify their data requirements precisely. Its strong type system improves data consistency and developer experience.

**Automation Potential:** GraphQL tools can validate queries against the schema.

### Example:
```graphql
type Query {
  user(id: ID!): User
  posts(userId: ID!): [Post]
}

type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post]
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
}

# Query example
query {
  user(id: "123") {
    name
    email
    posts {
      title
    }
  }
}
```

### When to Use:
- In applications with complex, nested data structures.
- In situations where bandwidth is important, such as mobile applications.
- When rapid prototyping and frontend development are needed.
