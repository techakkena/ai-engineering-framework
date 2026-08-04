/**
 * Dashboard hook.
 *
 * React Query hook for dashboard data.
 */

import { useQuery } from "@tanstack/react-query";

import { DashboardService } from "../services/dashboard.service";
import type { DashboardResponse } from "../types/dashboard.types";

/**
 * Dashboard query keys.
 */
export const dashboardQueryKeys = {
  all: ["dashboard"] as const,
};

/**
 * Dashboard hook.
 */
export function useDashboard() {
  return useQuery<DashboardResponse>({
    queryKey: dashboardQueryKeys.all,
    queryFn: DashboardService.getDashboard,
    staleTime: 5 * 60 * 1000,
    gcTime: 10 * 60 * 1000,
    retry: 2,
    refetchOnWindowFocus: false,
  });
}