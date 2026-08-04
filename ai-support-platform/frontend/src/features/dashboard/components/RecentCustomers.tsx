/**
 * Recent customers component.
 *
 * Displays recently added customers.
 */

export interface RecentCustomer {
  /**
   * Customer identifier.
   */
  readonly id: string;

  /**
   * Customer name.
   */
  readonly name: string;

  /**
   * Customer email.
   */
  readonly email: string;

  /**
   * Customer status.
   */
  readonly status: string;
}

export interface RecentCustomersProps {
  /**
   * Recent customers.
   */
  readonly customers: readonly RecentCustomer[];
}

/**
 * Recent customers.
 */
export function RecentCustomers({
  customers,
}: RecentCustomersProps): React.JSX.Element {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
      <h2 className="mb-6 text-xl font-semibold text-slate-900">
        Recent Customers
      </h2>

      <div className="overflow-x-auto">
        <table className="min-w-full text-left">
          <thead className="border-b">
            <tr>
              <th className="py-3 text-sm font-semibold">
                Name
              </th>

              <th className="py-3 text-sm font-semibold">
                Email
              </th>

              <th className="py-3 text-sm font-semibold">
                Status
              </th>
            </tr>
          </thead>

          <tbody>
            {customers.length === 0 ? (
              <tr>
                <td
                  colSpan={3}
                  className="py-8 text-center text-slate-500"
                >
                  No customers found.
                </td>
              </tr>
            ) : (
              customers.map((customer) => (
                <tr
                  key={customer.id}
                  className="border-b last:border-0"
                >
                  <td className="py-4 font-medium">
                    {customer.name}
                  </td>

                  <td className="py-4 text-slate-600">
                    {customer.email}
                  </td>

                  <td className="py-4">
                    <span className="rounded-full bg-green-100 px-3 py-1 text-xs font-medium text-green-700">
                      {customer.status}
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