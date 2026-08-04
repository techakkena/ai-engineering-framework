/**
 * Application providers.
 *
 * Composes all global providers required by the application.
 */

import type { PropsWithChildren } from "react";

import { AuthProvider } from "./auth/AuthProvider";
import { QueryProvider } from "./QueryProvider";
import { RouterProvider } from "./RouterProvider";
import { ThemeProvider } from "../providers/theme";

/**
 * Root application providers.
 *
 * @param props Provider props.
 * @returns Wrapped application.
 */
export function AppProviders({
  children,
}: PropsWithChildren): React.JSX.Element {
  return (
    <ThemeProvider>
      <QueryProvider>
        <AuthProvider>
          <RouterProvider>{children}</RouterProvider>
        </AuthProvider>
      </QueryProvider>
    </ThemeProvider>
  );
}