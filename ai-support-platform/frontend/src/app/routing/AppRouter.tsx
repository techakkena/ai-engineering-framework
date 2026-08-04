/**
 * Application router.
 *
 * Defines the application's route tree.
 */

import { Navigate, Route, Routes } from "react-router-dom";

import { ProtectedRoute } from "./ProtectedRoute";
import { PublicRoute } from "./PublicRoute";
import {
  PROTECTED_ROUTES,
  PUBLIC_ROUTES,
} from "./route-config";

/**
 * Application router component.
 *
 * @returns Route tree.
 */
export function AppRouter(): React.JSX.Element {
  return (
    <Routes>
      {/* Public Routes */}

      <Route
        path={PUBLIC_ROUTES.LOGIN}
        element={
          <PublicRoute>
            <div>Login Page</div>
          </PublicRoute>
        }
      />

      <Route
        path={PUBLIC_ROUTES.FORGOT_PASSWORD}
        element={
          <PublicRoute>
            <div>Forgot Password</div>
          </PublicRoute>
        }
      />

      <Route
        path={PUBLIC_ROUTES.RESET_PASSWORD}
        element={
          <PublicRoute>
            <div>Reset Password</div>
          </PublicRoute>
        }
      />

      {/* Protected Routes */}

      <Route
        path={PROTECTED_ROUTES.DASHBOARD}
        element={
          <ProtectedRoute>
            <div>Dashboard</div>
          </ProtectedRoute>
        }
      />

      {/* Catch All */}

      <Route
        path="*"
        element={
          <Navigate
            replace
            to={PROTECTED_ROUTES.DASHBOARD}
          />
        }
      />
    </Routes>
  );
}