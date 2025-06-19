// src/components/ExpenseCard.tsx
type ExpenseCardProps = {
  total: number;
  onAddExpense: () => void;
};

export default function ExpenseCard({ total, onAddExpense }: ExpenseCardProps) {
  return (
    <div className="border rounded-xl p-4 w-full max-w-sm shadow">
      <h2 className="text-lg font-semibold">Total Expenses</h2>
      <p className="text-2xl font-bold mb-2">₹{total}</p>
      <button 
        onClick={onAddExpense} 
        className="bg-blue-500 text-white px-4 py-1 rounded"
      >
        Add Expense +
      </button>
    </div>
  );
}
