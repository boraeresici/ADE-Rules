---
id: "component-architecture-react"
title: "React Component Architecture"
description: "Best practices for designing reusable, testable, and maintainable React components with TypeScript, including output definitions and examples."
tags: ["react", "component-architecture", "typescript", "ui"]
severity: "high"
applies_to: ["frontend", "react", "ui-ux"]
automation_potential: ["linter", "static-analysis", "code-review"]
suggested_tools: ["ESLint-plugin-react", "React Testing Library", "Storybook"]
related_rules: ["ui-ux-fundamentals", "design-principles", "state-management"]
---

- Write functional components with TypeScript interfaces.
- Use descriptive component and prop names.
- Implement appropriate error boundaries for components that may fail.
- Export components as default exports.
- Use React hooks for state management and side effects.
- Write easily testable components.

**Rationale:** A well-defined component architecture promotes reusability, testability, and maintainability, especially in complex applications. TypeScript enhances type safety.

**Automation Potential:** Linters can enforce component naming and structure. Testing frameworks automate unit and integration tests.

### Output
- A complete React component with a props interface
- Styling solution (Tailwind classes or styled-components)
- State management implementation if needed
- Basic unit test structure
- Accessibility checklist for the component
- Performance considerations and optimizations

**Rationale:** Defining clear outputs ensures that development efforts are focused and deliver comprehensive, high-quality components.

### Example (React Component):
```typescript
// UserProfile.tsx
import React, { useState, useEffect, useCallback, useMemo } from 'react';
import styled from 'styled-components';

interface UserData {
  id: string;
  name: string;
  email: string;
  role: string;
}

interface UserProfileProps {
  userId: string;
  onUpdate: (userData: UserData) => void;
}

// Styled components
const ProfileContainer = styled.div`
  padding: 1rem;
  background-color: #f0f0f0;
  border-radius: 8px;
  max-width: 400px;
  margin: 0 auto;
`;

const ProfileHeader = styled.h2`
  color: #333;
  font-size: 1.5rem;
  margin-bottom: 1rem;
`;

const ProfileInfo = styled.p`
  color: #666;
  margin-bottom: 0.5rem;
`;

const UpdateButton = styled.button`
  background-color: #007bff;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;

  &:hover {
    background-color: #0056b3;
  }

  &:focus {
    outline: none;
    box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.5);
  }
`;

const ErrorMessage = styled.div`
  color: #dc3545;
  margin-top: 1rem;
`;

const LoadingSpinner = styled.div`
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: spin 1s linear infinite;
  margin: 20px auto;

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
`;

const UserProfile: React.FC<UserProfileProps> = ({ userId, onUpdate }) => {
  const [userData, setUserData] = useState<UserData | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Memoized function to fetch user data
  const fetchUserData = useCallback(async () => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await fetch(`/api/users/${userId}`);
      if (!response.ok) throw new Error('Failed to fetch user data');
      const data = await response.json();
      setUserData(data);
    } catch (err) {
      setError('An error occurred while fetching user data');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  }, [userId]);

  useEffect(() => {
    fetchUserData();
  }, [fetchUserData]);

  // Memoized update handler
  const handleUpdate = useCallback(() => {
    if (userData) {
      onUpdate(userData);
    }
  }, [userData, onUpdate]);

  // Memoized user role
  const userRole = useMemo(() => {
    return userData?.role.charAt(0).toUpperCase() + userData?.role.slice(1);
  }, [userData]);

  if (isLoading) return <LoadingSpinner aria-label="Loading user data" />;
  if (error) return <ErrorMessage role="alert">{error}</ErrorMessage>;
  if (!userData) return null;

  return (
    <ProfileContainer>
      <ProfileHeader>{userData.name}'s Profile</ProfileHeader>
      <ProfileInfo>Email: {userData.email}</ProfileInfo>
      <ProfileInfo>Role: {userRole}</ProfileInfo>
      <UpdateButton onClick={handleUpdate} aria-label="Update user profile">
        Update Profile
      </UpdateButton>
    </ProfileContainer>
  );
};

export default UserProfile;

// Usage example:
// <UserProfile userId="123" onUpdate={(userData) => console.log('Updated:', userData)} />
```

This example demonstrates the following features:
- Type safety with TypeScript
- React hooks (useState, useEffect, useCallback, useMemo)
- Styling with styled-components
- Performance optimizations (useCallback, useMemo)
- Accessibility features (ARIA labels)
- Error handling and loading states
- Ready structure for responsive design

By applying these rules and the example, you can develop user-friendly, performant, and maintainable UI/UX designs and applications.

These rules can be used to improve the code quality, security, performance, and user experience of ADE. These rules can be adapted and extended according to the specific needs of each project.
