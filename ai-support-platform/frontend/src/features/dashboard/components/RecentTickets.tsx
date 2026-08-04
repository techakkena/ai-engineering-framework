/**
 * Recent tickets component.
 *
 * Displays the latest support tickets.
 */

export interface RecentTicket {
  /**
   * Ticket identifier.
   */
  readonly id: string;

  /**
   * Ticket title.
   */
  readonly title: string;

  /**
   * Ticket status.
   */
  readonly status: string;

  /**
   * Customer name.
   */
  readonly customer: string;
}

export interface RecentTicketsProps {
  /**
   * Recent tickets.
   */
  readonly tickets: readonly RecentTicket[];
}

/**
 * Recent tickets.
 */
export function RecentTickets({
  tickets,
}: RecentTicketsProps): React.JSX.Element {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
      <h2 className="mb-6 text-xl font-semibold text-slate-900">
        Recent Tickets
      </h2>

      <div className="overflow-x-auto">
        <table className="min-w-full text-left">
          <thead className="border-b">
            <tr>
              <th className="py-3 text-sm font-semibold">
                Ticket
              </th>

              <th className="py-3 text-sm font-semibold">
                Customer
              </th>

              <th className="py-3 text-sm font-semibold">
                Status
              </th>
            </tr>
          </thead>

          <tbody>
            {tickets.length === 0 ? (
              <tr>
                <td
                  colSpan={3}
                  className="py-8 text-center text-slate-500"
                >
                  No tickets found.
                </td>
              </tr>
            ) : (
              tickets.map((ticket) => (
                <tr
                  key={ticket.id}
                  className="border-b last:border-0"
                >
                  <td className="py-4">
                    {ticket.title}
                  </td>

                  <td className="py-4">
                    {ticket.customer}
                  </td>

                  <td className="py-4">
                    <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-medium">
                      {ticket.status}
                    </span>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}