/**
 * Authentication provider.
 *
 * Provides the authentication context for the application.
 */

import type { PropsWithChildren } from "react";
import {
  createContext,
  useCallback,
  useContext,
  useMemo,
  useState,
} from "react";

export interface AuthUser {
  readonly id: string;
  readonly email: string;
  readonly fullName: string;
  readonly roles: readonly string[];
}

export interface AuthContextValue {
  readonly user: AuthUser | null;
  readonly isAuthenticated: boolean;
  readonly isLoading: boolean;

  login: (user: AuthUser) => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextValue | null>(null);

/**
 * Authentication provider component.
 */
export function AuthProvider({
  children,
}: PropsWithChildren): React.JSX.Element {
  const [user, setUser] = useState<AuthUser | null>(null);

  const login = useCallback((authUser: AuthUser): void => {
    setUser(authUser);
  }, []);

  const logout = useCallback((): void => {
    setUser(null);
  }, []);

  const value = useMemo<AuthContextValue>(
    () => ({
      user,
      isAuthenticated: user !== null,
      isLoading: false,
      login,
      logout,
    }),
    [user, login, logout],
  );

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}

/**
 * Returns the authentication context.
 */
export function useAuth(): AuthContextValue {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error("useAuth must be used within AuthProvider.");
  }

  return context;
}