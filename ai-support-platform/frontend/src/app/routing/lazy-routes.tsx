/**
 * Lazy-loaded application routes.
 *
 * Centralizes all lazy route imports.
 */

import { lazy } from "react";

/**
 * Authentication pages.
 */
export const LoginPage = lazy(async () => ({
  default: () => <div>Login Page</div>,
}));

export const ForgotPasswordPage = lazy(async () => ({
  default: () => <div>Forgot Password Page</div>,
}));

export const ResetPasswordPage = lazy(async () => ({
  default: () => <div>Reset Password Page</div>,
}));

/**
 * Dashboard.
 */
export const DashboardPage = lazy(async () => ({
  default: () => <div>Dashboard</div>,
}));