/**
 * Dashboard domain types.
 */

export interface DashboardStats {
  readonly totalOrganizations: number;
  readonly totalTeams: number;
  readonly totalUsers: number;
  readonly totalProjects: number;
  readonly totalCustomers: number;
  readonly totalTickets: number;
  readonly openTickets: number;
  readonly closedTickets: number;
}

export interface DashboardSummary {
  readonly stats: DashboardStats;
}

export interface DashboardActivity {
  readonly id: string;
  readonly title: string;
  readonly description: string;
  readonly createdAt: string;
}

export interface DashboardChartData {
  readonly label: string;
  readonly value: number;
}

export interface DashboardResponse {
  readonly summary: DashboardSummary;
  readonly activities: readonly DashboardActivity[];
  readonly charts: readonly DashboardChartData[];
}