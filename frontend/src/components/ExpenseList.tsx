// src/components/ExpenseList.tsx

type Expense = {
  category: string;
  amount: number;
};

type ExpenseListProps = {
  expenses: Expense[];
};

export default function ExpenseList({ expenses }: ExpenseListProps) {
  return (
    <div className="border rounded-xl p-4 w-full max-w-md shadow">
      <h2 className="text-lg font-semibold mb-2">This Month's Expenses</h2>
      <ul className="list-disc pl-5 space-y-1">
        {expenses.length === 0 ? (
          <li className="text-gray-500">No expenses added.</li>
        ) : (
          expenses.map((exp, idx) => (
            <li key={idx} className="flex justify-between">
              <span>{exp.category}</span>
              <span>₹{exp.amount}</span>
            </li>
          ))
        )}
      </ul>
    </div>
  );
}
