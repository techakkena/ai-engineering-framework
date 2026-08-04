/**
 * Theme provider for the application.
 *
 * Provides the global theme context and manages
 * application theme state.
 */

import type { PropsWithChildren } from "react";
import {
  createContext,
  useContext,
  useEffect,
  useMemo,
  useState,
} from "react";

export type Theme = "light" | "dark";

interface ThemeContextValue {
  readonly theme: Theme;
  readonly setTheme: (theme: Theme) => void;
  readonly toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextValue | null>(null);

const STORAGE_KEY = "app-theme";

/**
 * Theme provider component.
 *
 * @param props Provider props.
 * @returns Wrapped application.
 */
export function ThemeProvider({
  children,
}: PropsWithChildren): React.JSX.Element {
  const [theme, setThemeState] = useState<Theme>("light");

  useEffect(() => {
    const storedTheme = localStorage.getItem(STORAGE_KEY) as Theme | null;

    if (storedTheme) {
      setThemeState(storedTheme);
    }
  }, []);

  useEffect(() => {
    document.documentElement.dataset.theme = theme;
    localStorage.setItem(STORAGE_KEY, theme);
  }, [theme]);

  const setTheme = (value: Theme): void => {
    setThemeState(value);
  };

  const toggleTheme = (): void => {
    setThemeState((current) =>
      current === "light" ? "dark" : "light",
    );
  };

  const value = useMemo<ThemeContextValue>(
    () => ({
      theme,
      setTheme,
      toggleTheme,
    }),
    [theme],
  );

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
}

/**
 * Returns the current theme context.
 *
 * @returns Theme context.
 * @throws Error if used outside ThemeProvider.
 */
export function useTheme(): ThemeContextValue {
  const context = useContext(ThemeContext);

  if (!context) {
    throw new Error("useTheme must be used within ThemeProvider.");
  }

  return context;
}