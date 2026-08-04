/**
 * Protected route component.
 *
 * Restricts unauthenticated users from accessing
 * protected application routes.
 */

import type { ReactNode } from "react";

import { Navigate } from "react-router-dom";

import { useAuth } from "../providers/AuthProvider";
import { PUBLIC_ROUTES } from "./route-config";

interface ProtectedRouteProps {
  /**
   * Child elements.
   */
  readonly children: ReactNode;
}

/**
 * Protected route wrapper.
 *
 * @param props Route props.
 * @returns Protected page or redirect.
 */
export function ProtectedRoute({
  children,
}: ProtectedRouteProps): React.JSX.Element {
  const {
    isAuthenticated,
    isLoading,
  } = useAuth();

  if (isLoading) {
    return <>Loading...</>;
  }

  if (!isAuthenticated) {
    return (
      <Navigate
        replace
        to={PUBLIC_ROUTES.LOGIN}
      />
    );
  }

  return <>{children}</>;
}