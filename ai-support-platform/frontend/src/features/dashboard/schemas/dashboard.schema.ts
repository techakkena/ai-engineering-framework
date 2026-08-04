/**
 * Dashboard validation schemas.
 */

import { z } from "zod";

export const dashboardStatsSchema = z.object({
  totalOrganizations: z.number().nonnegative(),
  totalTeams: z.number().nonnegative(),
  totalUsers: z.number().nonnegative(),
  totalProjects: z.number().nonnegative(),
  totalCustomers: z.number().nonnegative(),
  totalTickets: z.number().nonnegative(),
  openTickets: z.number().nonnegative(),
  closedTickets: z.number().nonnegative(),
});

export const dashboardSummarySchema = z.object({
  stats: dashboardStatsSchema,
});

export const dashboardActivitySchema = z.object({
  id: z.string(),
  title: z.string(),
  description: z.string(),
  createdAt: z.string(),
});

export const dashboardChartDataSchema = z.object({
  label: z.string(),
  value: z.number(),
});

export const dashboardResponseSchema = z.object({
  summary: dashboardSummarySchema,
  activities: z.array(dashboardActivitySchema),
  charts: z.array(dashboardChartDataSchema),
});

export type DashboardStatsSchema = z.infer<typeof dashboardStatsSchema>;

export type DashboardSummarySchema = z.infer<
  typeof dashboardSummarySchema
>;

export type DashboardActivitySchema = z.infer<
  typeof dashboardActivitySchema
>;

export type DashboardChartDataSchema = z.infer<
  typeof dashboardChartDataSchema
>;

export type DashboardResponseSchema = z.infer<
  typeof dashboardResponseSchema
>;