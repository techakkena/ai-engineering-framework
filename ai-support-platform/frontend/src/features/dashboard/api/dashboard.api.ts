/**
 * Dashboard API client.
 */

import { apiClient } from "../../../api/axios/client";

import type { DashboardResponse } from "../types/dashboard.types";

/**
 * Dashboard API.
 */
export class DashboardApi {
  /**
   * Get dashboard summary.
   */
  public static async getDashboard(): Promise<DashboardResponse> {
    const response = await apiClient.get<DashboardResponse>(
      "/dashboard",
    );

    return response.data;
  }

  /**
   * Refresh dashboard.
   */
  public static async refreshDashboard(): Promise<DashboardResponse> {
    const response = await apiClient.get<DashboardResponse>(
      "/dashboard?refresh=true",
    );

    return response.data;
  }
}