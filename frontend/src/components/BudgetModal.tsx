// src/components/BudgetCard.tsx
type BudgetCardProps = {
  budget: number;
  onSetBudget: () => void;
};

export default function BudgetCard({ budget, onSetBudget }: BudgetCardProps) {
  return (
    <div className="border rounded-xl p-4 w-full max-w-sm shadow">
      <h2 className="text-lg font-semibold">Budget</h2>
      <p className="text-2xl font-bold mb-2">₹{budget}</p>
      <button 
        onClick={onSetBudget} 
        className="bg-blue-500 text-white px-4 py-1 rounded"
      >
        Set Budget +
      </button>
    </div>
  );
}
