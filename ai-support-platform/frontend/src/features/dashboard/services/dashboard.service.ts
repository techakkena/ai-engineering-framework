/**
 * Dashboard service.
 *
 * Contains business logic for dashboard operations.
 */

import { DashboardApi } from "../api/dashboard.api";
import { dashboardResponseSchema } from "../schemas/dashboard.schema";
import type { DashboardResponse } from "../types/dashboard.types";

/**
 * Dashboard service.
 */
export class DashboardService {
  /**
   * Get dashboard data.
   */
  public static async getDashboard(): Promise<DashboardResponse> {
    const response = await DashboardApi.getDashboard();

    return dashboardResponseSchema.parse(response);
  }

  /**
   * Refresh dashboard data.
   */
  public static async refreshDashboard(): Promise<DashboardResponse> {
    const response = await DashboardApi.refreshDashboard();

    return dashboardResponseSchema.parse(response);
  }
}