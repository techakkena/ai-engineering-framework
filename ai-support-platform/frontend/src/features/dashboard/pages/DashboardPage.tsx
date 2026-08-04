/**
 * Dashboard page.
 *
 * Enterprise dashboard overview.
 */

import {
  Building2,
  FolderKanban,
  Ticket,
  Users,
} from "lucide-react";

import { PageContainer } from "../../../layouts";
import { PageLoader } from "../../../layouts";
import { Topbar } from "../../../layouts";

import { useDashboard } from "../hooks/useDashboard";

import { DashboardCharts } from "../components/DashboardCharts";
import { RecentCustomers } from "../components/RecentCustomers";
import { RecentTickets } from "../components/RecentTickets";
import { StatCard } from "../components/StatCard";

/**
 * Dashboard page.
 */
export function DashboardPage(): React.JSX.Element {
  const {
    data,
    isLoading,
    error,
  } = useDashboard();

  if (isLoading) {
    return (
      <PageLoader message="Loading dashboard..." />
    );
  }

  if (error || !data) {
    return (
      <PageContainer title="Dashboard">
        <div className="rounded-lg border border-red-200 bg-red-50 p-6 text-red-700">
          Failed to load dashboard data.
        </div>
      </PageContainer>
    );
  }

  return (
    <PageContainer>
      <Topbar
        title="Dashboard"
        subtitle="Enterprise AI Support Platform Overview"
      />

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
        <StatCard
          title="Organizations"
          value={data.summary.stats.totalOrganizations}
          icon={<Building2 size={28} />}
        />

        <StatCard
          title="Users"
          value={data.summary.stats.totalUsers}
          icon={<Users size={28} />}
        />

        <StatCard
          title="Projects"
          value={data.summary.stats.totalProjects}
          icon={<FolderKanban size={28} />}
        />

        <StatCard
          title="Tickets"
          value={data.summary.stats.totalTickets}
          icon={<Ticket size={28} />}
        />
      </div>

      <DashboardCharts
        data={data.charts}
        title="Support Analytics"
      />

      <div className="grid gap-6 xl:grid-cols-2">
        <RecentTickets tickets={[]} />

        <RecentCustomers customers={[]} />
      </div>
    </PageContainer>
  );
}